#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 多 UAV 桥接节点（支持 px4_1, px4_2）
        Node(
            package='drone_ros2_centralized_control',  # 替换为你的包名
            executable='gazebo_px4_relay.py',
            name='gazebo_px4_relay',
            output='screen',
            parameters=[{'uav_ids': [1, 2]}]
        ),

        # UAV 1 测试控制节点
        Node(
            package='drone_ros2_centralized_control',
            executable='muptiple_uav_ctrl.py',
            name='test_uav1',
            output='screen',
            parameters=[{'target_id': 1}]
        ),

        # UAV 2 测试控制节点
        Node(
            package='drone_ros2_centralized_control',
            executable='muptiple_uav_ctrl.py',
            name='test_uav2',
            output='screen',
            parameters=[{'target_id': 2}]
        )
    ])

