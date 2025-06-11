#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

from geometry_msgs.msg import Twist, PoseStamped, Quaternion
from std_msgs.msg import Float32MultiArray
from drone_ros2_centralized_control.msg import UavCmd, UavState, AttitudeSetpoint2

import math
import time

class UavTestController(Node):
    def __init__(self):
        super().__init__('uav_test_controller')

        # 控制的 UAV ID（1 或 2）
        self.declare_parameter('target_id', 1)
        self.target_id = self.get_parameter('target_id').get_parameter_value().integer_value

        ns = f"/px4_{self.target_id}"
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # 发布器
        self.cmd_vel_pub = self.create_publisher(Twist, f"{ns}/cmd_vel", qos)
        self.cmd_pos_pub = self.create_publisher(PoseStamped, f"{ns}/cmd_pos", qos)
        self.cmd_acc_pub = self.create_publisher(Float32MultiArray, f"{ns}/cmd_acc", qos)
        self.cmd_att_pub = self.create_publisher(AttitudeSetpoint2, f"{ns}/cmd_att", qos)
        self.uav_cmd_pub = self.create_publisher(UavCmd, '/uav_cmd', qos)

        # 状态订阅
        self.state_sub = self.create_subscription(UavState, f"{ns}/uav_state", self.state_callback, qos)

        self.timer = self.create_timer(0.05, self.control_sequence)

        self.state = None
        self.step = 0
        self.start_time = None

        self.get_logger().info(f"Testing UAV px4_{self.target_id}")

    def state_callback(self, msg: UavState):
        self.state = msg

    def control_sequence(self):
        if self.state is None:
            self.get_logger().info("Waiting for UAV state...")
            return
        elif self.start_time == None:
            self.start_time = self.get_clock().now().nanoseconds

            for _ in range(10):
                cmd = UavCmd()
                cmd.header.stamp = self.get_clock().now().to_msg()
                cmd.id = self.target_id
                cmd.is_arm = 1
                self.uav_cmd_pub.publish(cmd)
                time.sleep(0.05)
            self.get_logger().info("Sent arm command.")

        t = (self.get_clock().now().nanoseconds - self.start_time) / 1.e9

        if t < 5.0:
            # Takeoff (位置上升)
            twist = Twist()
            twist.linear.x =  0.0
            twist.linear.y =  0.0
            twist.linear.z = -1.0
            twist.angular.z = 0.0
            self.cmd_vel_pub.publish(twist)
            self.get_logger().info("Sent takeoff position command.")

        elif t < 15.0:
            # 位置控制
            pose = PoseStamped()
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.pose.position.x = 2.0
            pose.pose.position.y = 0.0
            pose.pose.position.z = -15.0
            self.cmd_pos_pub.publish(pose)
            self.get_logger().info("Sent position command.")

        elif t < 25.0:
            # 速度控制
            twist = Twist()
            twist.linear.x  = 0.2
            twist.linear.y  = 0.2
            twist.linear.z  = 0.0
            twist.angular.z = 0.5
            self.cmd_vel_pub.publish(twist)
            self.get_logger().info("Sent velocity command.")

        elif t < 35.0:
            # 加速度控制
            acc = Float32MultiArray()
            acc.data = [-1.5, 0.0, -0.2]  # 给出完整的加速度三轴值
            self.cmd_acc_pub.publish(acc)
            self.get_logger().info("Sent acceleration command.")

        elif t < 45.0:
            # 姿态控制 - 四元数（mode = 1）
            q = self.euler_to_quaternion(5.0 * math.pi / 180., 0.0, math.pi / 4)
            att = AttitudeSetpoint2()
            att.timestamp = int(self.get_clock().now().nanoseconds / 1000)
            att.mode = 1
            att.q_d = [float(q.w), float(q.x), float(q.y), float(q.z)]            # TODO wxyz or xyzw
            att.thrust_body = [0.0, 0.0, -0.75]  # thrust[2] 必须为负            
            self.cmd_att_pub.publish(att)
            self.get_logger().info("Sent quaternion attitude command.")

        elif t < 55.0:
            # 姿态控制 - roll/pitch/yaw（mode = 2）
            att = AttitudeSetpoint2()
            att.timestamp = int(self.get_clock().now().nanoseconds / 1000)
            att.mode = 2
            att.roll_body = 0.0
            att.pitch_body = 5.0 * math.pi / 180.
            att.yaw_body = math.pi / 4  # 45°
            att.thrust_body = [0.0, 0.0, -0.6]  # thrust[2] 必须为负, [0] and [1] must be zero for quadrotor, NEGATIVE [2] for up
            self.cmd_att_pub.publish(att)
            self.get_logger().info("Sent r/p/y attitude command.")

        elif t < 60.0:
            # 姿态控制 - body rate（mode = 0）
            att = AttitudeSetpoint2()
            att.timestamp = int(self.get_clock().now().nanoseconds / 1000)
            att.mode = 0
            att.roll_rate = 25.0 * math.pi / 180.
            att.pitch_rate = -5.0 * math.pi / 180.
            att.yaw_rate = 5.0 * math.pi / 180.  # 持续 yaw 旋转
            att.thrust_body = [0.0, 0.0, -1.0]  # thrust[2] 仍需为负
            self.cmd_att_pub.publish(att)
            self.get_logger().info("Sent body rate command.")


        elif t < 65.0:
            # 降落
            pose = PoseStamped()
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.pose.position.z = 0.0  # 降到地面
            self.cmd_pos_pub.publish(pose)
            self.get_logger().info("Sent landing command.")

        else:
            # Disarm
            cmd = UavCmd()
            cmd.header.stamp = self.get_clock().now().to_msg()
            cmd.id = self.target_id
            cmd.is_arm = -1
            self.uav_cmd_pub.publish(cmd)
            self.get_logger().info("Sent disarm command. Test complete.")

    def euler_to_quaternion(self, roll, pitch, yaw):
        q = Quaternion()
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        q.w = cr * cp * cy + sr * sp * sy
        q.x = sr * cp * cy - cr * sp * sy
        q.y = cr * sp * cy + sr * cp * sy
        q.z = cr * cp * sy - sr * sp * cy
        return q

def main(args=None):
    rclpy.init(args=args)
    node = UavTestController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
