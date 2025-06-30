#!/usr/bin/env python3
import rclpy
import time
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity     #, ResetWorld
from std_srvs.srv import Empty              # ResetSimulation 实际上是 Empty 类型
from geometry_msgs.msg import Pose
#
from utils2.vis import print_c, format_logger
from utils2.waypts import load_waypoints_from_yaml
import os

class GazeboController(Node):
    def __init__(self):
        super().__init__('gazebo_controller')
        
        # 声明参数（与launch文件中的结构匹配）
        # self.declare_parameters(
        #     namespace='',
        #     parameters=[
        #         ('pos_x', 0.0),
        #         ('pos_y', 0.0),
        #         ('goals', []),
        #         ('obstacles', []),
        #         ('is_avoiding_obstacle', 1),
        #         ('dist_goal', 0.2),
        #         ('dist_obs', 0.15)
        #     ]
        # )

        self.declare_parameter('map_file', '')
        map_file = self.get_parameter('map_file').value
        
        # 1. 重置世界
        #self.get_logger().info(format_logger(f"RESETING world ...", color="red", styles="bold"))
        #self.reset_world()                     # Added, commented
        
        # 2. 从参数生成目标点和障碍物
        self.get_logger().info(format_logger(f"SPAWNING target / obstacle locations ...", color="red", styles="bold"))

        #
        #self.spawn_objects()
        
        #
        self.spawn_waypoints_from_yaml(map_file)

    def reset_world(self):
        """重置Gazebo世界"""
        self.get_logger().info("Resetting Gazebo world...")
        reset_client = self.create_client(Empty, '/reset_simulation')
        while not reset_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('reset_simulation service not available, waiting...')
        
        future = reset_client.call_async(Empty.Request())
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info("World reset complete")

    def spawn_objects(self):
        """从参数生成目标点和障碍物"""
        # 获取参数值
        goals = self.get_parameter('goals').value
        obstacles = self.get_parameter('obstacles').value
        dist_goal = self.get_parameter('dist_goal').value
        dist_obs = self.get_parameter('dist_obs').value
        
        spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        while not spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('spawn_entity service not available, waiting...')
        self.get_logger().info(format_logger(f"SPAWNING target / obstacle locations complete...", color="green", styles="bold"))            

        # 生成目标点（绿色圆柱体）
        for i in range(0, len(goals), 5):
            x = goals[i]
            y = goals[i+1]
            self.get_logger().info(format_logger(f"Adding Goal: {x}, {y}", color="green", styles="italic"))
            self.spawn_cylinder(
                spawn_client,
                name=f"goal_{i//5}",
                x=x, y=y, z=0.05,
                radius=dist_goal,
                color='0 1 0 0.65'  # 绿色
            )

            time.sleep(0.025)

        # 生成障碍物（红色圆柱体）
        for i in range(0, len(obstacles), 5):
            x = obstacles[i]
            y = obstacles[i+1]
            radius = obstacles[i+2]
            self.get_logger().info(format_logger(f"Adding Obstacle: {x}, {y}, {radius}", color="green", styles="italic"))            
            self.spawn_cylinder(
                spawn_client,
                name=f"obstacle_{i//5}",
                x=x, y=y, z=0.05,
                radius=radius,
                color='1 0 0 0.65'  # 红色
            )

            time.sleep(0.025)

    def spawn_waypoints_from_yaml(self, yaml_path: str, radius=0.5):
        """从yaml加载路点并在Gazebo中可视化为圆柱体，并自动为不同ap分配颜色"""
        self.get_logger().info(format_logger(f"LOADING waypoints from: {yaml_path}", color="blue"))

        # 加载路点
        waypoint_list = load_waypoints_from_yaml(yaml_path, is_visualize=True)

        # 可用颜色池（RGBA），不透明度建议保持一致
        color_pool = [
            '0.0 0.6 1.0 0.9',    # 蓝
            '1.0 0.6 0.0 0.9',    # 橙
            '0.607 0.972 0.047 0.9',  # 绿
            '0.8 0.2 1.0 0.9',    # 紫
            '1.0 0.2 0.2 0.9',    # 红
            '0.0 1.0 1.0 0.9',    # 青
            '1.0 1.0 0.0 0.9',    # 黄
            '0.5 0.5 0.5 0.6'     # 灰（最后一组留作备用）
        ]

        ap_color_map = {}  # ap类型到颜色的动态映射表
        color_index = 0    # 当前使用的颜色索引

        # 调用服务
        spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        while not spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('spawn_entity service not available, waiting...')

        for wp in waypoint_list:
            pos = wp["pos"]  # [x, y, z, yaw]
            wp_id = wp["id"]

            x_t, y_t, z_t = pos[0], pos[1], 0.125
            x = y_t
            y = x_t
            z = z_t

            name = f"waypoint_{wp_id}"

            # 处理 ap 字段
            ap_list = wp.get("ap", [])
            if ap_list and isinstance(ap_list[0], str):
                ap_str = ap_list[0].strip("{} ").lower()
            else:
                ap_str = ''

            # 自动分配颜色
            if ap_str not in ap_color_map:
                if color_index < len(color_pool) - 1:
                    ap_color_map[ap_str] = color_pool[color_index]
                    color_index += 1
                else:
                    # 如果超出颜色池，重复最后一种颜色（灰色）
                    ap_color_map[ap_str] = color_pool[-1]

            color = ap_color_map[ap_str]

            self.get_logger().info(format_logger(
                f"Spawning {name} at ({x:.2f}, {y:.2f}, {z:.2f}) with ap: {ap_str} → color: {color}",
                color="cyan"
            ))

            self.spawn_cylinder(
                client=spawn_client,
                name=name,
                x=x, y=y, z=z,
                radius=radius,
                color=color,
                height=0.1
            )

            time.sleep(0.025)


    def spawn_cylinder(self, client, name, x, y, z, radius, color, height=0.5):
        """生成单个圆柱体"""
        cylinder_sdf = f"""
        <?xml version="1.0"?>
        <sdf version="1.6">
          <model name="{name}">
            <static>true</static>
            <pose>{x} {y} {z} 0 0 0</pose>
            <link name="link">
              <visual name="visual">
                <geometry>
                  <cylinder>
                    <radius>{radius}</radius>
                    <length>{height}</length>
                  </cylinder>
                </geometry>
                <material>
                  <ambient>{color}</ambient>
                  <diffuse>{color}</diffuse>
                </material>
              </visual>
              <collision name="collision">
              <geometry>
                  <box>
                  <size>0 0 0</size>  <!-- 将碰撞体积的尺寸设置为零 -->
                  </box>
              </geometry>
              <surface>
                  <contact>
                  <collide_without_contact>1</collide_without_contact> <!-- 禁止发生物理接触 -->
                  </contact>
              </surface>
              </collision>
            </link>
          </model>
        </sdf>
        """
        
        req = SpawnEntity.Request()
        req.name = name
        req.xml = cylinder_sdf
        req.initial_pose = Pose()
        req.initial_pose.position.x = 0.        # float(x)      alternative pos_x
        req.initial_pose.position.y = 0.        # float(y)                  pos_y
        req.initial_pose.position.z = 0.        # float(z)
        
        future = client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result() is not None and future.result().success:
            self.get_logger().info(f"Spawned {name} at ({x}, {y})")
        else:
            self.get_logger().error(f"Failed to spawn {name} at ({x}, {y})")

def main(args=None):
    rclpy.init(args=args)
    controller = GazeboController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()