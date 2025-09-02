#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import os
import math
import threading

import rospy
import rospkg

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from transforms3d.euler import quat2euler, euler2quat
from drone_ros_centeralized_control.msg import UavCmd, UavState
from utils.PID       import PID_Position
from utils.functions import saturation, dead_zone
from utils.vis       import print_c, format_logger
from utils.waypts    import (
    load_waypoints_from_yaml,
    load_transitions_from_yaml,
    extract_states_from_joint_x_u_lists,
    format_waypoint_table_4_single_agent,
    format_waypoints_table_with_costs_4_single_agent
)

UAV_SPEED_X_DEAD_ZONE = 0.0
UAV_MAX_SPEED_X = 0.35
UAV_MAX_SPEED_Y = 0.35
UAV_MAX_SPEED_Z = 1.0


class MultiDroneController(object):
    def __init__(self, drone_id=-1, target_altitude=0.8):
        """Initialize drone controller

        Args:
            drone_id (int): ID of the controlled drone
            target_altitude (float): Target altitude for this drone (meters)
        """
        if not isinstance(drone_id, int):
            rospy.logerr("Drone ID must be integer!")
            raise ValueError

        if drone_id < 0:
            self.drone_id = rospy.get_param('~drone_id', 2)
        else:
            self.drone_id = drone_id

        pkg_path = rospkg.RosPack().get_path('drone_ros_centeralized_control')
        default_map = os.path.join(pkg_path, 'map/mdp_planner/yaml/20250426_map_w_edges.yaml')
        self.map_file = rospy.get_param('~map_file', default_map)
        self.cost_multipliers = rospy.get_param('~cost_multipliers', 3.5)

        if not os.path.isfile(self.map_file):
            rospy.logerr("Map file not found: %s" % self.map_file)
            rospy.signal_shutdown("Missing map file")

        # Drone state variables
        self.uav_pose = Odometry()
        self.uav_state = UavState()
        self.is_uav_pose_updated = False
        self.is_uav_state_updated = False

        # Waypoint variables
        self.x_list    = []
        self.waypoints = []
        self.sorted_waypoints = []
        self.transition_cost_list = []
        self.accumulated_time_list = []

        # 控制流程变量
        self.start_time = rospy.Time.now().to_sec()
        self.ctrl_cntr = 0
        self.waypt_radius = 0.225
        self.takeoff_duration = 3.5
        self.target_altitude = target_altitude
        self.task_start_instant = 0.
        self.task_finished_instant = 0.
        self.current_waypoint_index = 0
        self.is_wait_until_time_exceeded = True         # TODO Critical single-agent可以关掉, multi-agent必须要打开
        self.task_start_time = None
        self.task_flag = False
        self.ready_flag = False
        self.landing_flag = False
        self.finished_flag = False

        # PID 控制器
        self.ctrl_dt = 0.05
        self.pid_x = PID_Position(0, 0.185, 0.25, 0.0,  self.ctrl_dt, -UAV_MAX_SPEED_X, UAV_MAX_SPEED_X)
        self.pid_y = PID_Position(0, 0.185, 0.25, 0.0,  self.ctrl_dt, -UAV_MAX_SPEED_Y, UAV_MAX_SPEED_Y)
        self.pid_z = PID_Position(0, 0.875, 0.005, 0.05, self.ctrl_dt, -UAV_MAX_SPEED_Z, UAV_MAX_SPEED_Z, max_int=UAV_MAX_SPEED_Z * 0.5)

        # Publishers
        self.arm_disarm_pub = rospy.Publisher(
            "/cmd_arm_disarm_{0}".format(self.drone_id),
            UavCmd,
            queue_size=1
        )
        self.cmd_vel_pub = rospy.Publisher(
            "/cmd_vel_{0}".format(self.drone_id),
            Twist,
            queue_size=1
        )

        # Subscribers
        rospy.Subscriber(
            "/mavrouter/drone_pose_" + str(self.drone_id),
            Odometry,
            self.uav_odom_callback
        )
        rospy.Subscriber(
            "/mavrouter/drone_state_" + str(self.drone_id),
            UavState,
            self.uav_state_callback
        )

        rospy.loginfo("Controller for drone {} initialized with altitude {}m".format(self.drone_id, self.target_altitude))

    def uav_odom_callback(self, msg):
        self.uav_pose = msg
        self.is_uav_pose_updated = True

    def uav_state_callback(self, msg):
        self.uav_state = msg
        self.is_uav_state_updated = True

    def set_arm_disarm_message(self, arm, disarm=False):
        msg = UavCmd()
        if disarm:
            command = -1
        elif arm:
            command = 1
        else:
            command = 0

        msg.header.stamp = rospy.Time.now()
        msg.id = -1
        msg.is_arm = command
        return msg

    def arm_drone(self, duration=5):
        rate = rospy.Rate(5)
        for i in range(duration):
            try:
                arm_msg = self.set_arm_disarm_message(True)
                self.arm_disarm_pub.publish(arm_msg)
                print_c("[Controller-{}] try ARMING UAV !".format(self.drone_id),
                        color='yellow', bold=True)
                rate.sleep()
            except rospy.ROSInterruptException:
                rospy.logwarn("Arming interrupted")
                return

    def load_waypts(self, x_list=None):
        """Load and process waypoints from YAML file"""
        if not self.map_file:
            rospy.logerr("No map file specified!")
            return False
        if x_list is None:
            rospy.logerr("No trajectory (x_list) provided for UAV {}".format(self.drone_id))
            return False

        try:
            rospy.loginfo(format_logger(
                "[UAV{}] Loading waypoints from {}".format(self.drone_id, self.map_file),
                color='green'
            ))

            self.waypoints = load_waypoints_from_yaml(self.map_file)
            if not self.waypoints:
                rospy.logerr("No waypoints loaded!")
                return False

            self.edges     = load_transitions_from_yaml(self.map_file)
            if not self.waypoints:
                rospy.logerr("No edges loaded!")
                return False

            #x_list = extract_states_from_x_u_lists(x_u_list)           # has been done outside
            self.sorted_waypoints = []  # list of (id_str, pos)

            for key in x_list:
                key_str = str(key)
                for wp in self.waypoints:
                    if wp["id"] == key_str:
                        self.sorted_waypoints.append((key_str, wp['pos']))
                        break

            # calculate transition
            self.transition_cost_list  = [ 0. ]
            self.accumulated_time_list = [ 0. ]
            for i in range(1, self.sorted_waypoints.__len__()):
                id_last = self.sorted_waypoints[i - 1][0]  # 节点 ID
                id_curr = self.sorted_waypoints[i][0]
                #
                try:
                    edge_info = self.edges[id_last][id_curr]
                    cost_t = edge_info['weight'] * self.cost_multipliers
                    #cost_t = 1. * self.cost_multipliers

                    acc_cost_t = self.accumulated_time_list[self.accumulated_time_list.__len__() - 1] + cost_t
                    self.transition_cost_list.append(cost_t)
                    self.accumulated_time_list.append(acc_cost_t)
                except KeyError:
                    raise ValueError("No edge from %s to %s in map..." % (str(id_last), str(id_curr), ))

            formatted_table = format_waypoints_table_with_costs_4_single_agent(
                self.sorted_waypoints,
                self.transition_cost_list,
                self.accumulated_time_list
            )
            rospy.loginfo("\n" + formatted_table)

            self.task_duration = self.accumulated_time_list[-1]
            return True

        except Exception as e:
            rospy.logerr("Waypoint loading failed: {}".format(str(e)))
            return False

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

    def _takeoff_phase(self, cmd, current_time, target_altitude):
        """Handle takeoff phase control logic"""
        default_vz = 0.85               # should be larger
        # TODO
        if self.uav_pose.pose.pose.position.z <= -0.5 or current_time < 0.5 / default_vz:
            cmd.linear.z = -default_vz
        else:
            px = self.uav_pose.pose.pose.position.x
            py = self.uav_pose.pose.pose.position.y
            pz = self.uav_pose.pose.pose.position.z
            tx = px
            ty = py
            vx, vy, vz = self.calculate_velocity(px, py, pz, tx, ty, -self.target_altitude)
            cmd.linear.z = vz
            if cmd.linear.z < 0:
                cmd.linear.z *= 1.25

            # cmd.linear.z = -cmd.linear.z  # NED frame conversion
        print_c(
            "[Controller-%d] Taking off... Current: %.2fm | Target: %.2fm | Speed: %.2fm/s | Time: %.2fs" % (
                self.drone_id,
                self.uav_pose.pose.pose.position.z,
                target_altitude,
                cmd.linear.z,
                current_time
            ),
            color='green',
            bold=True
        )
        return cmd

    def _goto_phase(self, cmd, current_time, target_altitude):
        # 飞到第一个路点
        key, target = self.sorted_waypoints[0]
        px = self.uav_pose.pose.pose.position.x
        py = self.uav_pose.pose.pose.position.y
        pz = self.uav_pose.pose.pose.position.z
        vx, vy, vz = self.calculate_velocity(px, py, pz, target[0], target[1], -self.target_altitude)
        
        cmd.linear.x = vx
        cmd.linear.y = vy
        cmd.linear.z = vz
        # cmd.linear.z = -cmd.linear.z  # NED frame conversion

        err_x = target[0] - px
        err_y = target[1] - py
        dist = math.sqrt(err_x**2 + err_y**2)

        if dist < self.waypt_radius:
            self.ready_flag = True
            self.task_start_instant = current_time
            rospy.loginfo(format_logger(
                "[UAV{}] Reached initial waypoint {}".format(self.drone_id, key), 
                color='green', 
                styles='bold'
            ))
        else:
            if int(self.ctrl_cntr) % 25 == 0:
                rospy.loginfo(format_logger(
                    "[UAV{}] Moving to start point Tgt id:x/y/z: {}: {:.2f} / {:.2f} / {:.2f} | Fbk x/y/z: {:.2f} / {:.2f} / {:.2f} | Dist: {:.2f} | Vel x/y/z: {:.2f} / {:.2f} / {:.2f}".format(
                        self.drone_id,
                        key,
                        target[0],
                        target[1],
                        self.target_altitude,
                        px,
                        py,
                        pz,
                        dist,                        
                        vx,
                        vy,
                        vz
                    ),
                    color='green',
                ))

        return cmd

    def _mission_phase(self, cmd, current_time, start_time):
        # 飞行任务
        if not self.task_flag:
            self.task_flag = True
            self.task_start_time = current_time
            rospy.loginfo(format_logger("[UAV{}] Mission started...".format(self.drone_id), color='cyan'))

        key, target = self.sorted_waypoints[self.current_waypoint_index]
        limited_time = self.accumulated_time_list[self.current_waypoint_index]
        #
        if self.current_waypoint_index >= len(self.sorted_waypoints) - 1:
            rospy.loginfo("[UAV{}] All waypoints reached.".format(self.drone_id))
            self.landing_flag = True
            self.task_finished_instant = current_time

        px = self.uav_pose.pose.pose.position.x
        py = self.uav_pose.pose.pose.position.y
        pz = self.uav_pose.pose.pose.position.z

        vx, vy, vz = self.calculate_velocity(px, py, pz, target[0], target[1], -self.target_altitude)

        err_x = target[0] - px
        err_y = target[1] - py
        err_z = self.target_altitude - pz
        dist = math.sqrt(err_x**2 + err_y**2)
        #
        # Decision
        should_switch_waypoint = False

        if self.is_wait_until_time_exceeded:
            # 要等到时间到了再换点
            if dist < self.waypt_radius and current_time > limited_time + self.task_start_instant:
                should_switch_waypoint = True
        else:
            # 提前到达或时间到了都可以换点
            if dist < self.waypt_radius or current_time > limited_time + self.task_start_instant:
                should_switch_waypoint = True
        #
        #
        if should_switch_waypoint:
            if dist < self.waypt_radius:
                rospy.loginfo(format_logger(
                    "[UAV{}] Reached waypoint {} ({}/{}) | t: {:.2f} / {:.2f}".format(
                        self.drone_id,
                        key,
                        self.current_waypoint_index,
                        len(self.sorted_waypoints) - 1,
                        current_time,
                        limited_time + self.task_start_instant
                    ),
                    color='green',
                    styles='bold'
                ))
            else:
                rospy.loginfo(format_logger(
                    "[UAV{}] NOT Reach waypoint {} ({}/{}) | t: {:.2f} / {:.2f}, time exceeded".format(
                        self.drone_id,
                        key,
                        self.current_waypoint_index,
                        len(self.sorted_waypoints) - 1,
                        current_time,
                        limited_time + self.task_start_instant
                    ),
                    color='yellow',
                    styles='bold'
                ))
            
            if self.current_waypoint_index < len(self.sorted_waypoints) - 1:
                self.current_waypoint_index += 1

        if int(self.ctrl_cntr) % 25 == 0:
            rospy.loginfo(format_logger(
                "[UAV{}] Tgt id:x/y/z: {}: {:.2f} / {:.2f} / {:.2f} | Fbk x/y/z: {:.2f} / {:.2f} / {:.2f} | Dist: {:.2f} | Vel x/y/z: {:.2f} / {:.2f} / {:.2f}".format(
                    self.drone_id,
                    key,
                    target[0],
                    target[1],
                    self.target_altitude,
                    px,
                    py,
                    pz,
                    dist,                    
                    vx,
                    vy,
                    vz
                ),
                color='blue',
                styles='italic'
            ))
        cmd.linear.x = vx
        cmd.linear.y = vy
        cmd.linear.z = vz
        cmd.angular.z = 0.0  # No rotation
        return cmd

    def _landing_phase(self, cmd):
        """Handle landing phase control logic"""
        cmd.linear.z = -0.35
        # cmd.linear.z = -cmd.linear.z  # NED frame conversion
        
        print_c("[Controller] Landing...", color='blue', bold=True)
        
        if self.uav_pose.pose.pose.position.z < 0.1:
            cmd = Twist()
            print_c("[Controller] Landed!", color='green', bold=True)
        
        return cmd

    def run_mission(self):
        """Main mission execution loop"""
        
        start_time = rospy.Time.now().to_sec()
        print_c("[Controller] main process STARTED !", color='green', bold=True)
        
        rate = rospy.Rate(1 / self.ctrl_dt)
        
        try:
            while not rospy.is_shutdown():
                # Process state updates
                if self.is_uav_state_updated:
                    if self.ctrl_cntr % 5 == 0:
                        print_c("[Controller] UAV%d Mode %d, %d \t status: %d" % 
                            (self.drone_id,
                            self.uav_state.base_mode, 
                            self.uav_state.custom_mode, 
                            self.uav_state.system_status),
                            color='cyan', bold=False)
                    self.is_uav_state_updated = False
                
                # Process position updates
                if self.is_uav_pose_updated:
                    # Get current pose
                    x_current = self.uav_pose.pose.pose.position.x
                    y_current = self.uav_pose.pose.pose.position.y
                    z_current = self.uav_pose.pose.pose.position.z
                    
                    # Convert quaternion to Euler angles
                    orientation = self.uav_pose.pose.pose.orientation
                    [roll, pitch, yaw] = quat2euler([
                        orientation.w,
                        orientation.x,
                        orientation.y,
                        orientation.z
                    ])
                    
                    # Convert to degrees
                    roll_deg = roll * 180. / math.pi
                    pitch_deg = pitch * 180. / math.pi
                    yaw_deg = yaw * 180. / math.pi
                    
                    # Log pose information
                    if self.ctrl_cntr % 5 == 0:
                        print_c("[Controller] UAV%d | Pose: %.3f %.3f %.3f | Vel: %.3f %.3f %.3f | AVel: %.3f %.3f %.3f | Rpy: %.3f %.3f %.3f" % 
                            (self.drone_id,
                            x_current, y_current, z_current,
                            self.uav_pose.twist.twist.linear.x,
                            self.uav_pose.twist.twist.linear.y,
                            self.uav_pose.twist.twist.linear.z,
                            self.uav_pose.twist.twist.angular.x,
                            self.uav_pose.twist.twist.angular.y,
                            self.uav_pose.twist.twist.angular.z,
                            roll_deg, pitch_deg, yaw_deg),
                            color='blue', bold=True)
                    
                    self.is_uav_pose_updated = False
                    current_time = rospy.Time.now().to_sec() - start_time
                    
                    # Generate control command
                    cmd = Twist()
                    
                    # 起飞
                    if current_time < self.takeoff_duration - 0.25:
                        cmd = self._takeoff_phase(cmd, current_time, self.target_altitude)
                    elif current_time < self.takeoff_duration:
                        # 等待就位阶段
                        cmd.linear.x = 0.0
                        cmd.linear.y = 0.0
                        cmd.linear.z = 0.0
                        cmd.angular.z = 0.0
                        print_c("[Controller] UAV%d Waiting for takeoff to complete..." % (self.drone_id, ), color='yellow', bold=True)                        
                    # === 起飞后导航至初始路点（等待就位阶段） ===
                    elif not self.ready_flag:
                        cmd = self._goto_phase(cmd, current_time, self.target_altitude)
                    elif not self.landing_flag:
                        cmd = self._mission_phase(
                            cmd, 
                            current_time, 
                            self.takeoff_duration)
                    else:
                        cmd = self._landing_phase(cmd)
                    
                    # Publish command
                    self.cmd_vel_pub.publish(cmd)
                
                self.ctrl_cntr += 1
                if self.ctrl_cntr >= 1000000:
                    self.ctrl_cntr = 0
                rate.sleep()
                
        except KeyboardInterrupt:
            rospy.loginfo("Mission interrupted by user")
        except Exception as e:
            rospy.logerr("Mission failed: {}".format(str(e)))
        finally:
            # Send zero command on exit
            self.cmd_vel_pub.publish(Twist())
            rospy.loginfo("Mission terminated")



class TeamController(object):
    def __init__(self, joint_x_list, uav_ids, alt_list):
        """
        Args:
            joint_x_list: list of tuple，例如 [['0', '1', ...], ['5', '4', ...], ...]
            uav_ids: list of int，例如 [1,2,4]，表示无人机编号
        """
        self.uav_ids = uav_ids
        self.num_drones = len(uav_ids)
        self.joint_x_list = joint_x_list
        self.controllers = []

        # 初始化 UAV 控制器
        for idx in range(0, len(uav_ids)):
            ctrl = MultiDroneController(drone_id=uav_ids[idx], target_altitude=alt_list[idx])
            ctrl.x_list = self.joint_x_list[idx]
            self.controllers.append(ctrl)

    def start_team_mission(self):
        """并行执行多无人机任务"""
        import threading
        threads = []
        for ctrl in self.controllers:
            if ctrl.load_waypts(ctrl.x_list):
                ctrl.arm_drone()
                t = threading.Thread(target=ctrl.run_mission)
                t.start()
                threads.append(t)
        for t in threads:
            t.join()


if __name__ == "__main__":
    try:
        rospy.init_node('team_drone_control', anonymous=True)

        # TODO
        # 输入 UAV ID 序列，例如实验要控制 [1,2,4]
        uav_ids = [3, 4]                        # 这个是有顺序的
        alt_list = [0.75, 1.35]

        # 
        # TODO
        # modify here
        x_u_list_str = """'('0', '5')' '(('b',), ('b',))' '('2', '6')' '(('a',), ('a',))' '('3', '4')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('4', '3')' '(('a',), ('b',))' '('5', '4')' '(('b',), ('a',))' '('6', '3')' '(('b',), ('b',))' '('6', '0')' '(('a',), ('a',))' '('4', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')' '(('b',), ('b',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')'"""
        # x_u_list_str = """'('0', '5')' '(('b',), ('b',))' '('2', '6')' '(('a',), ('a',))' '('3', '4')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('4', '3')'"""
        #
        joint_x_u_list = extract_states_from_joint_x_u_lists(x_u_list_str, num_drones=len(uav_ids))
        
        team_ctrl = TeamController(joint_x_u_list, uav_ids, alt_list)
        team_ctrl.start_team_mission()

    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        rospy.logerr("Node initialization failed: {}".format(str(e)))

