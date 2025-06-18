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
from utils2.functions import saturation, dead_zone
from utils2.waypts import load_waypoints_from_yaml, extract_states_from_x_u_lists, format_waypoint_table_4_single_agent, format_waypoints_table_with_costs_4_single_agent

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

        self.declare_parameter('drone_id', 1)
        self.declare_parameter('map_file', '')
        ctrl_dt = 0.1

        drone_id = self.get_parameter('drone_id').get_parameter_value().integer_value
        self.drone_id = drone_id

        ns = f"/px4_{self.drone_id}"
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        #
        # Parameters
        self.cost_multipliers            = 2. 
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

        # 加载航点
        # TODO 地图要放大
        map_file = self.get_parameter('map_file').value

        # 
        # 读取的transition cost不对
        self.get_logger().info(format_logger(f"[UAV{drone_id}] Loading waypoints from {map_file}", color='green'))
        # with open(map_file, 'r') as f:
        #     self.waypoints = yaml.safe_load(f)['waypoint']
        self.waypoints = load_waypoints_from_yaml(map_file)

        #
        # TODO
        # MODIFY HERE
        x_u_list = """'15' '('u',)' '10' '('u',)' '5' '('r',)' '6' '('d',)' '11' '('r',)' '12' '('l',)' '11' '('r',)' '12' '('l',)' '11' '('d',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('r',)' '17' '('l',)' '16' '('u',)' '11' '('d',)' '16' '('l',)' '15' '('d',)' '20' '('u',)' '15' '('d',)' '20' '('u',)' '15' '('r',)' '16' '('r',)' '17' '('l',)' '16' '('d',)' '21' '('l',)' '20' '('u',)' '15' '('d',)' '20' '('r',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('u',)' '1' '('d',)' '6' '('l',)' '5' '('u',)' '0' '('r',)' '1' '('d',)' '6' '('l',)' '5' '('d',)' '10' '('r',)' '11' '('d',)' '16' '('l',)' '15' '('u',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('d',)' '21' '('r',)' '17' '('l',)' '16' '('r',)' '17' '('u',)' '12' '('u',)' '7' '('u',)' '2' '('l',)' '1' '('r',)' '2' '('l',)' '1' '('l',)' '0' '('r',)' '1' '('d',)' '6' '('r',)' '7' '('l',)' '6' '('u',)' '1' '('d',)' '6' '('r',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('l',)' '7' '('d',)' '12' '('r',)' '13' '('r',)' '14' '('l',)' '13' '('u',)' '8' '('u',)' '3' '('l',)' '2' '('l',)' '1' '('l',)' '0' '('d',)' '5' '('d',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('r',)' '17' '('r',)' '18' '('u',)' '13' '('r',)' '14' '('l',)' '13' '('d',)' '18' '('u',)' '13' '('u',)' '8' '('u',)' '3' '('d',)' '8' '('d',)' '13' '('l',)' '12' '('u',)' '7' '('u',)' '2' '('d',)' '7' '('r',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('l',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('u',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('l',)' '2' '('d',)' '7' '('d',)' '12' '('u',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('d',)' '13' '('d',)' '18' '('r',)' '19' '('u',)' '14' '('l',)' '13' '('r',)' '14'"""
        x_list = extract_states_from_x_u_lists(x_u_list)
        # x_list = list(map(int, x_list))

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
            pos_last = self.sorted_waypoints[i - 1][1]
            pos_curr = self.sorted_waypoints[i][1]
            #
            dx = pos_curr[0] - pos_last[0]
            dy = pos_curr[1] - pos_last[1]
            dz = pos_curr[2] - pos_last[2]            
            cost_t = math.sqrt(dx**2 + dy**2 + dz**2) * self.cost_multipliers
            acc_cost_t = self.accumulated_time_list[self.accumulated_time_list.__len__() - 1] + cost_t
            self.transition_cost_list.append(cost_t)
            self.accumulated_time_list.append(acc_cost_t)

        formatted_table = format_waypoints_table_with_costs_4_single_agent(self.sorted_waypoints, self.transition_cost_list, self.accumulated_time_list)
        self.get_logger().info("\n" + formatted_table)

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

        # 自动解锁
        self.get_logger().info(format_logger(f"[UAV{drone_id}] Arming UAV...", color='green', styles='bold'))
        for _ in range(10):
            self.arm_disarm_pub.publish(self.set_arm_disarm_message(True))
            time.sleep(0.1)

    def uav_odom_callback(self, msg):
        self.uav_pose = msg
        self.is_uav_pose_updated = True

    def uav_state_callback(self, msg):
        self.uav_state = msg
        self.is_uav_state_updated = True

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
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Taking off...", color='cyan'))

        # === 起飞后导航至初始路点（等待就位阶段） ===
        elif not self.ready_flag:
            # 飞到第一个路点
            key, target = self.sorted_waypoints[0]
            px = self.uav_pose.pose.pose.position.x
            py = self.uav_pose.pose.pose.position.y
            pz = self.uav_pose.pose.pose.position.z
            vx, vy, vz = self.calculate_velocity(px, py, pz, target[0], target[1], -self.target_altitude)
            self.publish_velocity(vx, vy, vz)

            err_x = target[0] - px
            err_y = target[1] - py
            dist = math.sqrt(err_x**2 + err_y**2)

            if dist < self.waypt_radius:
                self.ready_flag = True
                self.task_start_instant = now
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Reached initial waypoint {key}", color='green', styles='bold'))

            else:
                if int(self.ctrl_cntr) % 10 == 0:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Moving to start point {key}", color='blue'))

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
            self.publish_velocity(vx, vy, vz)

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
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Tgt id:x/y/z: {key}: {target[0]} / {target[1]} / {self.target_altitude} | Fbk x/y/z: {px} / {py} / {pz} | Vel x/y/z: {vx} / {vy} / {vz}", color='blue', styles='italic'))

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
