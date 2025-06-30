#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
import yaml
import time
from collections import OrderedDict

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from drone_ros2_centralized_control.msg import UavCmd, UavState  # 自定义消息类型
from transforms3d.euler import quat2euler

from utils2.vis import print_c, format_logger
from utils2.PID import PID_Position
from utils2.apf import apf_collision_avoidance
from utils2.functions import saturation, dead_zone
from utils2.waypts import load_waypoints_from_yaml, load_transitions_from_yaml, extract_states_for_all_robots, format_waypoint_table_4_single_agent, format_waypoints_table_with_costs_4_single_agent

import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

from functools import cmp_to_key
from subprocess import check_output
from MDP_Planner.Map.example_20250506_grid_single_agent import construct_single_agent_mdp, observation_func_0506, control_observable_dict
from MDP_Planner.Map.example_20250506_team_mdp import run_2_observations_seqs, observation_seq_2_inference, calculate_cost_from_runs    # TODO
from MDP_Planner.MDP_TG.mdp import Motion_MDP
from MDP_Planner.MDP_TG.dra import Dra
from MDP_Planner.MDP_TG.lp  import syn_full_plan_rex
from MDP_Planner.User.dra3 import product_mdp3
from MDP_Planner.User.lp3  import synthesize_full_plan_w_opacity3
from MDP_Planner.User.grid_utils import sort_team_numerical_states
from MDP_Planner.User.vis2 import print_c, print_colored_sequence, print_highlighted_sequences
from MDP_Planner.User.plot import plot_cost_hist, plot_cost_hists_multi


UAV_SPEED_X_DEAD_ZONE = 0.0
UAV_MAX_SPEED_X = 1.0
UAV_MAX_SPEED_Y = 1.0
UAV_MAX_SPEED_Z = 2.0

#
# --------------------------------------------------------------------------------------------------
class MultiDroneController(Node):

    def __init__(self):
        super().__init__('multi_drone_control')

        self.declare_parameter('drone_id',  1)
        self.declare_parameter('drone_num', 2)
        self.declare_parameter('map_file', '')
        for i in range(1, 11):
            self.declare_parameter(f'initial_pose_{i}_x', 0.0)
            self.declare_parameter(f'initial_pose_{i}_y', 0.0)
            self.declare_parameter(f'initial_pose_{i}_z', 0.83)
            self.declare_parameter(f'initial_pose_{i}_yaw', 0.0)

        ctrl_dt = 0.1

        drone_id  = self.get_parameter('drone_id').get_parameter_value().integer_value
        drone_num = self.get_parameter('drone_num').get_parameter_value().integer_value
        self.drone_id = drone_id

        self.initial_poses = {}
        for i in range(1, 11):
            x   = self.get_parameter(f'initial_pose_{i}_x').get_parameter_value().double_value
            y   = self.get_parameter(f'initial_pose_{i}_y').get_parameter_value().double_value
            z   = self.get_parameter(f'initial_pose_{i}_z').get_parameter_value().double_value
            yaw = self.get_parameter(f'initial_pose_{i}_yaw').get_parameter_value().double_value

            if i == drone_id:
                self.x_offset = x               # in NED frame
                self.y_offset = y
                self.z_offset = z
                self.yaw_offset = yaw
            else:
                self.initial_poses[i] = {
                    'x': x,                     # in NED frame
                    'y': y,
                    'z': z,
                    'yaw': yaw
                }

        self.get_logger().info(format_logger(f"[Drone {self.drone_id}] Offsets: x={self.x_offset:.2f}, y={self.y_offset:.2f}, z={self.z_offset:.2f}, yaw={self.yaw_offset:.2f}", color='bright_green', styles='bold'))

        ns = f"/px4_{self.drone_id}"
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        #
        # Parameters
        self.cost_multipliers            = 7.5 
        self.waypt_radius                = 0.25
        self.target_altitude             = 0.8
        self.current_waypoint_index      = 0
        self.is_wait_until_time_exceeded = True
        #
        # PID 控制器
        self.pid_x = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_X, UAV_MAX_SPEED_X)
        self.pid_y = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_Y, UAV_MAX_SPEED_Y)
        self.pid_z = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_Z, UAV_MAX_SPEED_Z)
        #
        # UAV 状态变量
        self.uav_pose = Odometry()
        self.uav_state = UavState()
        self.is_uav_pose_updated = False
        self.is_uav_state_updated = False

        # 订阅与发布
        self.arm_disarm_pub = self.create_publisher(UavCmd, f"/cmd_arm_disarm_{drone_id}", qos)
        self.cmd_vel_pub = self.create_publisher(Twist, f"/cmd_vel_{drone_id}", qos)

        self.create_subscription(Odometry, f"/mavrouter/drone_pose_{drone_id}", self.uav_odom_callback, qos)
        self.create_subscription(UavState, f"/mavrouter/drone_state_{drone_id}", self.uav_state_callback, qos)

        self.other_drone_subscribers = []
        for i in range(1, drone_num + 1):
            if i == drone_id:
                continue
            topic_name = f'/mavrouter/drone_pose_{i}'
            subscriber = self.create_subscription(
                Odometry,
                topic_name,
                lambda msg, rid=i: self.other_uav_pos_callback(msg, rid),
                qos
            )
            self.other_drone_subscribers.append(subscriber)
            self.get_logger().info(f"Subscribed to {topic_name}")        

        # 加载航点
        # TODO 地图要放大
        map_file = self.get_parameter('map_file').value

        # 
        # 读取的transition cost不对
        self.get_logger().info(format_logger(f"[UAV{drone_id}] Loading waypoints from {map_file}", color='green'))
        # with open(map_file, 'r') as f:
        #     self.waypoints = yaml.safe_load(f)['waypoint']
        self.waypoints = load_waypoints_from_yaml(map_file)
        self.edges     = load_transitions_from_yaml(map_file)

        #
        # TODO
        # MODIFY HERE
        # x_u_list_all = ''' '('0', '5')' '(('a',), ('a',))' '('1', '4')' '(('a',), ('a',))' '('0', '3')' '(('a',), ('b',))' '('1', '0')' '(('a',), ('b',))' '('0', '3')' '(('b',), ('b',))' '('3', '0')' '(('b',), ('a',))' '('0', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')' '(('b',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '3')' '(('a',), ('b',))' '('1', '0')' '(('a',), ('b',))' '('0', '3')' '(('b',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '3')' '(('a',), ('b',))' '('1', '0')' '(('a',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('0', '3')' '(('a',), ('b',))' '('1', '0')' '(('a',), ('a',))' '('0', '1')' '(('b',), ('a',))' '('3', '0')' '(('b',), ('a',))' '('4', '1')' '(('a',), ('a',))' '('5', '0')' '(('b',), ('b',))' '('6', '3')' '(('b',), ('b',))' '('6', '0')' '(('a',), ('a',))' '('4', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('a',))' '('3', '1')' '(('b',), ('a',))' '('4', '0')' '(('b',), ('a',))' '('2', '1')' '(('a',), ('a',))' '('3', '0')' '(('b',), ('a',))' '('0', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')' '(('a',), ('b',))' '('1', '0')' '(('a',), ('b',))' '('0', '3')' '(('b',), ('b',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')' '(('b',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '3')' '(('a',), ('b',))' '('1', '4')' '(('a',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '4')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '3')' '''
        x_u_list_all = ''' '('0', '5')' '(('a',), ('a',))' '('1', '4')' '(('a',), ('a',))' '('0', '5')' '(('b',), ('b',))' '('3', '6')' '(('b',), ('a',))' '('0', '4')' '(('a',), ('b',))' '('1', '2')' '(('a',), ('a',))' '('0', '3')' '(('a',), ('b',))' '('1', '4')' '(('a',), ('a',))' '('0', '3')' '(('b',), ('b',))' '('3', '0')' '(('b',), ('a',))' '('0', '1')' '(('a',), ('a',))' '('1', '0')' '(('a',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('a',))' '('0', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('4', '3')' '(('b',), ('b',))' '('2', '0')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('a',))' '('4', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')' '(('b',), ('b',))' '('2', '4')' '(('a',), ('a',))' '('3', '5')' '(('b',), ('a',))' '('0', '4')' '(('b',), ('a',))' '('3', '5')' '(('b',), ('a',))' '('0', '4')' '(('b',), ('a',))' '('2', '5')' '(('a',), ('a',))' '('3', '4')' '(('b',), ('a',))' '('0', '3')' '(('b',), ('b',))' '('3', '4')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('a',))' '('0', '1')' '(('b',), ('a',))' '('3', '0')' '(('b',), ('a',))' '('0', '1')' '(('b',), ('a',))' '('3', '0')' '(('b',), ('a',))' '('0', '1')' '(('a',), ('a',))' '('1', '0')' '(('a',), ('a',))' '('0', '1')' '(('b',), ('a',))' '('3', '0')' '(('b',), ('a',))' '('4', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')' '(('a',), ('b',))' '('1', '0')' '(('a',), ('a',))' '('0', '1')' '''

        x_lists = extract_states_for_all_robots(x_u_list_all)
        if type(drone_id) == int:
            x_list  = x_lists[drone_id - 1]
        else:
            raise TypeError(f"Drone ID not received: {type(drone_id).__name__}")
        # x_list = list(map(int, x_list))

        # TODO
        # 可以增加一个变量, 增加完成的路点数量

        self.sorted_waypoints = []  # list of (id_str, pos)
        for key in x_list:
            key_str = str(key)
            for wp in self.waypoints:
                if wp["id"] == key_str:
                    # ('id', [x, y, z, yaw(deg)])
                    self.sorted_waypoints.append((key_str, wp['pos']))
                    break

        # formatted_table = format_waypoint_table_4_single_agent(self.sorted_waypoints)
        # self.get_logger().info("\n" + formatted_table)         

        # 
        # calculate transition
        self.transition_cost_list  = [ 0. ]
        self.accumulated_time_list = [ 0. ]
        for i in range(1, self.sorted_waypoints.__len__()):
            id_last = self.sorted_waypoints[i - 1][0]  # 节点 ID
            id_curr = self.sorted_waypoints[i][0]
            #
            try:
                edge_info = self.edges[id_last][id_curr]
                #cost_t = edge_info['weight'] * self.cost_multipliers
                cost_t = 1. * self.cost_multipliers

                acc_cost_t = self.accumulated_time_list[self.accumulated_time_list.__len__() - 1] + cost_t
                self.transition_cost_list.append(cost_t)
                self.accumulated_time_list.append(acc_cost_t)
            except KeyError:
                raise ValueError(f"No edge from {id_last} to {id_curr} in map.")

        formatted_table = format_waypoints_table_with_costs_4_single_agent(self.sorted_waypoints, self.transition_cost_list, self.accumulated_time_list)
        self.get_logger().info("\n" + formatted_table)

        # Added
        # Calculate other drone initial pos
        self.other_drone_initial_pos = {}       # id : (waypt_id, [x, y, z])
        self.is_other_drone_reach_initial_pos = {}
        self.is_all_other_drone_reach_inital_pos = False
        for i in range(1, drone_num + 1):
            if i == drone_id:
                continue
            wp_t = str(x_lists[i - 1][0])
            # self.get_logger().info(format_logger(f"[UAV{drone_id}] {wp_t} | {str(i)}", color='red', styles='italic'))
            found = False
            for wp in self.waypoints:
                if wp["id"] == wp_t:
                    self.other_drone_initial_pos[i] = (wp_t, wp['pos'])  # ✅ 用 wp_t 而不是未定义的 key_str
                    self.is_other_drone_reach_initial_pos[i] = False
                    found = True
                    break
            if not found:
                self.get_logger().warn(f"[UAV{drone_id}] Did not find waypoint id == {wp_t} in waypoints")
        #
        # self.get_logger().info(format_logger(f"[UAV{drone_id}] drone_num: {drone_num} | " + str(self.other_drone_initial_pos), color='red', styles='bold'))

        # Added
        # for APF collision avoidance
        self.other_uav_pos = dict()         # 只记录x和y

        # 控制流程变量
        self.create_timer(ctrl_dt, self.control_loop)
        self.start_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.ctrl_cntr             = 0
        self.takeoff_duration      = 10.0
        self.task_start_instant    = self.takeoff_duration
        self.task_finished_instant = self.takeoff_duration
        self.task_duration = self.accumulated_time_list[self.accumulated_time_list.__len__() - 1]
        #
        self.task_start_time = None
        self.task_flag       = False
        self.ready_flag      = False
        self.landing_flag    = False
        self.finished_flag   = False

        # Added
        self.other_uav_cb_idxs = {}
        for i in range(1, drone_num + 1):
            if i == self.drone_id:
                continue
            self.other_uav_cb_idxs[i] = 0

        # 自动解锁
        self.get_logger().info(format_logger(f"[UAV{drone_id}] Arming UAV...", color='green', styles='bold'))
        for _ in range(10):
            self.arm_disarm_pub.publish(self.set_arm_disarm_message(True))
            time.sleep(0.1)

    def uav_odom_callback(self, msg):
        self.uav_pose = msg
        self.uav_pose.pose.pose.position.x += self.x_offset
        self.uav_pose.pose.pose.position.y += self.y_offset
        self.uav_pose.pose.pose.position.z += self.z_offset
        # TODO yaw offset
        self.is_uav_pose_updated = True

    def uav_state_callback(self, msg):
        self.uav_state = msg
        self.is_uav_state_updated = True

    def other_uav_pos_callback(self, msg, robot_id):
        #
        # Task 1
        # check for reaching position
        if not self.ready_flag:
            px_t = msg.pose.pose.position.x + self.initial_poses[robot_id]['x']
            py_t = msg.pose.pose.position.y + self.initial_poses[robot_id]['y']
            pz_t = msg.pose.pose.position.z + self.initial_poses[robot_id]['z']
            
            target_x = self.other_drone_initial_pos[robot_id][1][0]     # drone_id : (key_str, wp['pos'])
            target_y = self.other_drone_initial_pos[robot_id][1][1]

            err_x = target_x - px_t
            err_y = target_y - py_t
            dist = math.sqrt(err_x**2 + err_y**2)

            if dist < self.waypt_radius:
                self.is_other_drone_reach_initial_pos[robot_id] = True

            if self.other_uav_cb_idxs[robot_id] % 50 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] -- UAV{robot_id} Tgt x/y/dist: {target_x} / {target_y} /  {dist} | Fbk x/y: {px_t} / {py_t}", color='green', styles='italic'))

        is_all_reached = True
        for key_t in self.is_other_drone_reach_initial_pos.keys():
            if self.is_other_drone_reach_initial_pos[key_t] == False:
                is_all_reached = False
                break
        self.is_all_other_drone_reach_inital_pos = is_all_reached

        # Task 2
        self.other_uav_pos[robot_id] = [msg.pose.pose.position.x + self.initial_poses[robot_id]['x'], 
                                        msg.pose.pose.position.y + self.initial_poses[robot_id]['y']]

        self.other_uav_cb_idxs[robot_id] += 1

    def set_arm_disarm_message(self, arm, disarm=False):
        msg = UavCmd()
        msg.header.stamp = self.get_clock().now().to_msg()
        #msg.id = self.drone_id
        msg.id = -1
        msg.is_arm = 1 if arm else -1 if disarm else 0
        return msg

    def publish_velocity(self, vx, vy, vz):
        twist = Twist()
        twist.linear.x = float(vx)
        twist.linear.y = float(vy)
        twist.linear.z = float(vz)
        self.cmd_vel_pub.publish(twist)

    def calculate_velocity(self, x, y, z, x_tgt, y_tgt, z_tgt):
        self.pid_x.ref = x_tgt
        self.pid_y.ref = y_tgt
        self.pid_z.ref = z_tgt
        vx = saturation(self.pid_x.get_new_ctrl(x), UAV_MAX_SPEED_X, -UAV_MAX_SPEED_X)
        vy = saturation(self.pid_y.get_new_ctrl(y), UAV_MAX_SPEED_Y, -UAV_MAX_SPEED_Y)
        vz = saturation(self.pid_z.get_new_ctrl(z), UAV_MAX_SPEED_Z, -UAV_MAX_SPEED_Z)
        vx = dead_zone(vx, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)
        vy = dead_zone(vy, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)
        return vx, vy, vz

    def control_loop(self):
        if not self.is_uav_pose_updated:
            self.get_logger().info(format_logger(f"[UAV{self.drone_id}] pose NOT received...", color='yellow'))
            return

        if self.finished_flag:
            return

        now = self.get_clock().now().seconds_nanoseconds()[0] - self.start_time


        if now < self.takeoff_duration:
            # 起飞
            vx, vy, vz = self.calculate_velocity(0., 0., self.uav_pose.pose.pose.position.z, 0., 0., -self.target_altitude)
            self.publish_velocity(vx, vy, vz)
            if int(self.ctrl_cntr) % 10 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Taking off...", color='bright_cyan', styles='bold'))

        # === 起飞后导航至初始路点（等待就位阶段） ===
        elif not self.ready_flag:
            # 飞到第一个路点
            key, target = self.sorted_waypoints[0]
            px = self.uav_pose.pose.pose.position.x
            py = self.uav_pose.pose.pose.position.y
            pz = self.uav_pose.pose.pose.position.z
            vx, vy, vz = self.calculate_velocity(px, py, pz, target[0], target[1], -self.target_altitude)
            # Added, apf
            #self.get_logger().info(format_logger(f"[UAV{self.drone_id}] other_uav_pos: {self.other_uav_pos}", color='cyan'))
            vx_p, vy_p = apf_collision_avoidance([px, py], self.other_uav_pos , [vx, vy], k=4.5, radius=2.25)         # 不要让apf参数进入PID反馈
            #
            self.publish_velocity(vx_p, vy_p, vz)

            err_x = target[0] - px
            err_y = target[1] - py
            dist = math.sqrt(err_x**2 + err_y**2)

            if self.is_all_other_drone_reach_inital_pos and dist < self.waypt_radius:
                self.ready_flag = True
                self.task_start_instant = now
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Reached initial waypoint {key}", color='green', styles='bold'))

            else:
                if int(self.ctrl_cntr) % 10 == 0:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Moving to start point {key}", color='blue'))
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Other {str(self.is_other_drone_reach_initial_pos)} \n", color='blue'))

            if int(self.ctrl_cntr) % 20 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Tgt id:x/y/z/dist: {key}: {target[0]} / {target[1]} / {self.target_altitude} / {dist} | Fbk x/y/z: {px} / {py} / {pz} | Vel x/y/z: {vx} / {vy} / {vz} | FinalV x/y: {vx_p} / {vy_p}", color='cyan', styles='italic'))


        elif not self.landing_flag and now < self.task_start_instant + self.task_duration:
            # 飞行任务
            if not self.task_flag:
                self.task_flag = True
                self.task_start_time = now
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Mission started...", color='cyan'))

            key, target = self.sorted_waypoints[self.current_waypoint_index]
            limited_time = self.accumulated_time_list[self.current_waypoint_index]
            #
            if self.current_waypoint_index >= len(self.sorted_waypoints) - 1:
                self.get_logger().info(f"[UAV{self.drone_id}] All waypoints reached.")
                self.landing_flag = True
                self.task_finished_instant = now

            px = self.uav_pose.pose.pose.position.x
            py = self.uav_pose.pose.pose.position.y
            pz = self.uav_pose.pose.pose.position.z

            vx, vy, vz = self.calculate_velocity(px, py, pz, target[0], target[1], -self.target_altitude)
            # Added, apf
            vx_p, vy_p = apf_collision_avoidance([px, py], self.other_uav_pos, [vx, vy], k=4.5, radius=2.25)
            #
            # for debugging
            if self.drone_id == 2 and int(self.ctrl_cntr) % 20 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] uav2 pos: x/y/z: {px} / {py} / {pz}", color='bright_magenta', styles='italic'))
            if self.drone_id == 1 and int(self.ctrl_cntr) % 20 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] uav2 pos: x/y/z: {self.other_uav_pos}", color='bright_magenta', styles='italic'))
            #   
            self.publish_velocity(vx_p, vy_p, vz)

            err_x = target[0] - px
            err_y = target[1] - py
            err_z = self.target_altitude - pz
            dist = math.sqrt(err_x**2 + err_y**2)
            #
            # Decision
            should_switch_waypoint = False

            if self.is_wait_until_time_exceeded:
                # 要等到时间到了再换点
                if dist < self.waypt_radius and now > limited_time + self.task_start_instant:
                    should_switch_waypoint = True
            else:
                # 提前到达或时间到了都可以换点
                if dist < self.waypt_radius or now > limited_time + self.task_start_instant:
                    should_switch_waypoint = True
            #
            #
            if should_switch_waypoint:
                #
                if dist < self.waypt_radius:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Reached waypoint {key} ({self.current_waypoint_index} / {len(self.sorted_waypoints) - 1}) | t: {now:.2f} / {limited_time + self.task_start_instant:.2f}", color='green',  styles='bold'))
                else:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] NOT Reach waypoint {key} ({self.current_waypoint_index} / {len(self.sorted_waypoints) - 1}) | t: {now:.2f} / {limited_time + self.task_start_instant:.2f}, time exceeded", color='yellow', styles='bold'))
                #
                if self.current_waypoint_index < len(self.sorted_waypoints) - 1:
                    self.current_waypoint_index += 1

            if int(self.ctrl_cntr) % 20 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Tgt id:x/y/z: {key}: {target[0]} / {target[1]} / {self.target_altitude} | Fbk x/y/z: {px} / {py} / {pz} | Vel x/y/z: {vx} / {vy} / {vz} | FinalV x/y: {vx_p} / {vy_p}", color='blue', styles='italic'))

        elif now < self.task_finished_instant + 15.0:
            # 降落
            err_z = 0.0 - self.uav_pose.pose.pose.position.z
            vx, vy, vz = 0.0, 0.0, saturation(self.pid_z.get_new_ctrl(err_z), UAV_MAX_SPEED_Z, -UAV_MAX_SPEED_Z)
            self.publish_velocity(vx, vy, vz)
            self.get_logger().info(f"[UAV{self.drone_id}] Landing...")

        else:
            # 上锁
            self.arm_disarm_pub.publish(self.set_arm_disarm_message(False, disarm=True))
            self.get_logger().info(f"[UAV{self.drone_id}] Disarmed.")
            self.finished_flag = True

        self.ctrl_cntr += 1

#
# --------------------------------------------------------------------------------------------------

def main(args=None):
    rclpy.init(args=args)
    node = MultiDroneController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
