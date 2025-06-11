#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
import time
import yaml
from collections import OrderedDict

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from drone_ros_centeralized_control.msg import UavCmd, UavState
from transforms3d.euler import quat2euler

from utils.vis import print_c
from utils.PID import PID_Position
from utils.functions import saturation, dead_zone

UAV_SPEED_X_DEAD_ZONE = 1
UAV_MAX_SPEED_X = 2
UAV_MAX_SPEED_Y = 2
UAV_MAX_SPEED_Z = 2


class UAVController(Node):
    def __init__(self):
        super().__init__('multi_drone_control')

        self.drone_id = 2
        self.uav_pose = Odometry()
        self.is_uav_pose_updated = False
        self.uav_state = UavState()
        self.is_uav_state_updated = False

        self.pid_x = PID_Position(0, 1.0, 0.1, 0.05, -0.3, 0.3)
        self.pid_y = PID_Position(0, 1.0, 0.1, 0.05, -0.3, 0.3)
        self.pid_z = PID_Position(0, 1.0, 0.1, 0.05, -0.3, 0.3)

        uav_cmd_topic = f"/cmd_arm_disarm_{self.drone_id}"
        cmd_vel_topic = f"/cmd_vel_{self.drone_id}"
        pose_topic = f"/mavrouter/drone_pose_{self.drone_id}"
        state_topic = f"/mavrouter/drone_state_{self.drone_id}"

        self.arm_disarm_pub = self.create_publisher(UavCmd, uav_cmd_topic, 1)
        self.cmd_vel_pub = self.create_publisher(Twist, cmd_vel_topic, 1)
        self.create_subscription(Odometry, pose_topic, self.uav_odom_callback, 1)
        self.create_subscription(UavState, state_topic, self.uav_state_callback, 1)

        self.load_waypoints()

        self.create_timer(0.1, self.control_loop)
        self.waypoint_iter = iter(self.sorted_waypoints.items())
        self.current_target = None
        self.takeoff_duration = 2.0
        self.task_duration = 60.0
        self.start_time = time.time()
        self.task_start_time = None

        self.arm_uav()

    def arm_uav(self):
        for _ in range(5):
            msg = self.set_arm_disarm_message(True)
            self.arm_disarm_pub.publish(msg)
            print_c("[Controller] Arming UAV...", color='yellow', bold=True)
            time.sleep(0.2)

    def set_arm_disarm_message(self, arm, disarm=False):
        msg = UavCmd()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.id = -1
        msg.is_arm = 1 if arm else -1 if disarm else 0
        return msg

    def load_waypoints(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, '../model', 'mapt.yaml')
        print_c(f"[Controller] Loading waypoints from {file_path}", color='yellow', bold=True)

        with open(file_path, 'r') as f:
            self.waypoints = yaml.safe_load(f)['waypoint']

        rho = ['4', '1', '3', '5', '6', '2', '7', '8', '9', '10']
        self.sorted_waypoints = OrderedDict((k, self.waypoints[k]) for k in rho if k in self.waypoints)

    def uav_odom_callback(self, msg):
        self.uav_pose = msg
        self.is_uav_pose_updated = True

    def uav_state_callback(self, msg):
        self.uav_state = msg
        self.is_uav_state_updated = True

    def calculate_velocity(self, err_x, err_y, err_z):
        vx = saturation(self.pid_x.get_new_ctrl(err_x), UAV_MAX_SPEED_X, -UAV_MAX_SPEED_X)
        vy = saturation(self.pid_y.get_new_ctrl(err_y), UAV_MAX_SPEED_Y, -UAV_MAX_SPEED_Y)
        vz = saturation(self.pid_z.get_new_ctrl(err_z), UAV_MAX_SPEED_Z, -UAV_MAX_SPEED_Z)
        vx = dead_zone(vx, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)
        vy = dead_zone(vy, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)
        return vx, vy, vz

    def control_loop(self):
        if not (self.is_uav_pose_updated and self.is_uav_state_updated):
            return

        self.is_uav_pose_updated = False
        self.is_uav_state_updated = False

        x = self.uav_pose.pose.pose.position.x
        y = self.uav_pose.pose.pose.position.y
        z = self.uav_pose.pose.pose.position.z

        now = time.time() - self.start_time
        cmd = Twist()

        if now < self.takeoff_duration:
            _, _, vz = self.calculate_velocity(0, 0, 0.8 - z)
            cmd.linear.z = vz
            self.cmd_vel_pub.publish(cmd)
            print_c("[Controller] Taking off...", color='blue', bold=True)
            return

        if self.current_target is None:
            try:
                self.current_key, self.current_target = next(self.waypoint_iter)
                self.task_start_time = time.time()
                print_c(f"[Controller] Going to point {self.current_key} : {self.current_target}", color='yellow', bold=True)
            except StopIteration:
                if z > 0.1:
                    _, _, vz = self.calculate_velocity(0, 0, -z)
                    cmd.linear.z = vz
                    self.cmd_vel_pub.publish(cmd)
                    print_c("[Controller] Landing...", color='blue', bold=True)
                else:
                    self.cmd_vel_pub.publish(Twist())
                    print_c("[Controller] Landed!", color='green', bold=True)
                return

        xt, yt, zt, duration = self.current_target
        vx, vy, vz = self.calculate_velocity(xt - x, yt - y, zt - z)
        cmd.linear.x = vx
        cmd.linear.y = vy
        cmd.linear.z = vz
        self.cmd_vel_pub.publish(cmd)

        elapsed = time.time() - self.task_start_time
        if elapsed > duration or (abs(x - xt) < 0.1 and abs(y - yt) < 0.1 and abs(z - zt) < 0.1):
            self.current_target = None


def main(args=None):
    rclpy.init(args=args)
    node = UAVController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

