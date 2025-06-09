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

UAV_SPEED_X_DEAD_ZONE = 0.0
UAV_MAX_SPEED_X = 1.0
UAV_MAX_SPEED_Y = 1.0
UAV_MAX_SPEED_Z = 2.0


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

        # PID 控制器
        self.pid_x = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_X, UAV_MAX_SPEED_X)
        self.pid_y = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_Y, UAV_MAX_SPEED_Y)
        self.pid_z = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_Z, UAV_MAX_SPEED_Z)

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
        map_file = self.get_parameter('map_file').value

        print(f"[UAV{drone_id}] Loading waypoints from {map_file}")
        with open(map_file, 'r') as f:
            self.waypoints = yaml.safe_load(f)['waypoint']

        self.sorted_waypoints = OrderedDict()
        for key in ['4', '1', '3', '5', '6', '2', '7', '8', '9', '10']:
            if key in self.waypoints:
                self.sorted_waypoints[key] = self.waypoints[key]

        # 控制流程变量
        self.create_timer(ctrl_dt, self.control_loop)
        self.start_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.ctrl_cntr = 0
        self.takeoff_duration = 10.0
        self.task_duration = 60.0
        self.target_altitude = 0.8
        self.current_waypoint_index = 0
        self.task_start_time = None
        self.task_flag = False
        self.finished_flag = False

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

        elif now < self.takeoff_duration + self.task_duration:
            # 飞行任务
            if not self.task_flag:
                self.task_flag = True
                self.task_start_time = now
                self.waypt_start_time = now
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Mission started...", color='cyan'))

            keys = list(self.sorted_waypoints.keys())
            if self.current_waypoint_index >= len(keys):
                self.get_logger().info(f"[UAV{self.drone_id}] All waypoints reached.")
                return

            elapsed_time = now - self.waypt_start_time

            key = keys[self.current_waypoint_index]
            target = self.sorted_waypoints[key]
            duration = 10                           # TODO

            px = self.uav_pose.pose.pose.position.x
            py = self.uav_pose.pose.pose.position.y
            pz = self.uav_pose.pose.pose.position.z

            vx, vy, vz = self.calculate_velocity(px, py, pz, target[0], target[1], -self.target_altitude)
            self.publish_velocity(vx, vy, vz)

            err_x = target[0] - px
            err_y = target[1] - py
            err_z = self.target_altitude - pz
            dist = math.sqrt(err_x**2 + err_y**2)
            if dist < 0.25 or elapsed_time > duration:
                #
                if dist < 0.25:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Reached waypoint {key}", color='green',  styles='bold'))
                else:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] NOT Reach waypoint {key}, time exceeded", color='yellow', styles='bold'))
                #
                if self.current_waypoint_index < len(keys) - 1:
                    self.current_waypoint_index += 1
                self.waypt_start_time = now  # 重置航点计时

            if int(self.ctrl_cntr) % 20 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Tgt id:x/y/z: {key}: {target[0]} / {target[1]} / {self.target_altitude} | Fbk x/y/z: {px} / {py} / {pz} | Vel x/y/z: {vx} / {vy} / {vz}", color='blue', styles='italic'))

        elif now < self.task_duration + 5.0:
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

def main(args=None):
    rclpy.init(args=args)
    node = MultiDroneController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
