#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from drone_ros_centeralized_control.msg import UavCmd, UavState
from transforms3d.euler import quat2euler, euler2quat
#
# 打开VSCode的设置：
#     通过菜单：File > Preferences > Settings
#     或者快捷键：Ctrl + ,
# 在搜索框中输入python.autoComplete.extraPaths。
# 点击Add Item，然后添加以下路径（根据你的ROS工作空间路径调整）: "/path/to/your_workspace/devel/lib/python2.7/dist-packages"
#
from utils.vis import print_c

# def send_arm_disarm(drone_id, arm):
#     if arm:

#     else:

# def send_velocity(drone_id, vx, vy, vz, wx, wy, wz):
#     """
#     发送速度指令到指定无人机
#     :param drone_id: 无人机编号 (1, 2, 3, ...)
#     :param vx: 线速度 X 方向
#     :param vy: 线速度 Y 方向
#     :param vz: 线速度 Z 方向
#     :param wx: 角速度 X 方向
#     :param wy: 角速度 Y 方向
#     :param wz: 角速度 Z 方向
#     """
#     topic_name = "/cmd_vel_{0}".format(drone_id)  # 替换 f-string
#     pub = rospy.Publisher(topic_name, Twist, queue_size=10)

#     cmd = Twist()
#     cmd.linear.x = vx
#     cmd.linear.y = vy
#     cmd.linear.z = vz
#     cmd.angular.x = wx
#     cmd.angular.y = wy
#     cmd.angular.z = wz

#     rate = rospy.Rate(10)  # 10Hz 发送数据
#     for _ in range(10):  # 发送 10 次，确保接收
#         pub.publish(cmd)
#         rate.sleep()

#     print("Sent velocity command to drone {0}: {1}, {2}, {3}".format(drone_id, vx, vy, vz))  # 替换 f-string

# def control_multiple_drones(drone_count, vx, vy, vz, wx, wy, wz):
#     """
#     向多个无人机发布相同的速度控制指令
#     :param drone_count: 无人机数量
#     :param vx, vy, vz: 线速度
#     :param wx, wy, wz: 角速度
#     """
#     for drone_id in range(1, drone_count + 1):
#         send_velocity(drone_id, vx, vy, vz, wx, wy, wz)

uav_pose = Odometry()
is_uav_pose_updated = False
def uav_odom_callback(msg):
    global uav_pose, is_uav_pose_updated
    uav_pose = msg
    is_uav_pose_updated = True

uav_state = UavState()
is_uav_state_updated = False
def uav_state_callback(msg):
    global uav_state, is_uav_state_updated
    uav_state = msg
    is_uav_state_updated = True

def set_arm_disarm_message(arm, disarm=False):
    """
    设置解锁/上锁消息
    :param arm: True: 解锁, False: 上锁
    :return: Twist 消息
    """
    msg = UavCmd()
    if arm:
        command = 1
    elif disarm:
        command = -1
    else:
        command = 0
    msg.header.stamp = rospy.Time.now()
    msg.id = -1                             # -1 for all drones
    msg.is_arm = command
    return msg

if __name__ == "__main__":
    rospy.init_node('multi_drone_control', anonymous=True)  # 只初始化一次 ROS 节点
    
    drone_id = 2
    uav_cmd_topic_name = "/cmd_arm_disarm_{0}".format(drone_id)
    cmd_vel_topic_name = "/cmd_vel_{0}".format(drone_id)  # 替换 f-string

    arm_disarm_pub = rospy.Publisher(uav_cmd_topic_name,    UavCmd, queue_size=1)
    cmd_vel_pub    = rospy.Publisher(cmd_vel_topic_name,    Twist,  queue_size=1)

    drone_pose_topic_name  = "/mavrouter/drone_pose_"  + str(drone_id)            # begin from 1
    drone_state_topic_name = "/mavrouter/drone_state_" + str(drone_id)
    #
    cmd_vel_sub   = rospy.Subscriber(drone_pose_topic_name,  Odometry, uav_odom_callback)
    cmd_state_sub = rospy.Subscriber(drone_state_topic_name, UavState, uav_state_callback)
  
    rate = rospy.Rate(5)
    for i in range(0, 5):                                   # for debugging
        arm_msg = set_arm_disarm_message(True)
        arm_disarm_pub.publish(arm_msg)
        #
        print_c("[Controller Example] try ARMING UAV !", color='yellow', bold=True)
        #
        rate.sleep()

    # 起飞阶段：10秒内上升到0.8米高度
    takeoff_duration = 2.0  # 起飞时间
    target_altitude = 0.8  # 目标高度
    #
    t_period = 20.0  # 圆周运动周期
    r = 1.2  # 圆周半径
    w = 2 * math.pi / t_period  # 角速度
    #
    start_time = rospy.Time.now().to_sec()  # 获取当前时间

    print_c("[Controller Example] main process STARTED !", color='green', bold=True)
    rate = rospy.Rate(20)  
    # control_multiple_drones(drone_count, vx, vy, vz, wx, wy, wz)  # 控制所有无人机同时前进
    while True:
        # cmd = Twist()
        # cmd.linear.x = 0.5
        # cmd.linear.y = 0
        # cmd.linear.z = 0
        # cmd.angular.x = 0
        # cmd.angular.y = 0
        # cmd.angular.z = 0.01

        # cmd_vel_pub.publish(cmd)



        if is_uav_state_updated:
            print_c("[Controller Example] UAV Mode %d, %d \t status: %d" % (uav_state.base_mode, uav_state.custom_mode, uav_state.system_status,), color='cyan', bold=True)
            is_uav_state_updated = False
        
        if is_uav_pose_updated:

            #
            # 更新飞机姿态 
            # Define follows NED frame !
            x_current = uav_pose.pose.pose.position.x
            y_current = uav_pose.pose.pose.position.y
            z_current = uav_pose.pose.pose.position.z
            #
            [roll_t,pitch_t,yaw_t] = quat2euler([uav_pose.pose.pose.orientation.w, uav_pose.pose.pose.orientation.x, uav_pose.pose.pose.orientation.y, uav_pose.pose.pose.orientation.z])
            roll_t  = roll_t * 180.  / math.pi
            pitch_t = pitch_t * 180. / math.pi
            yaw_t   = yaw_t * 180.   / math.pi
            print_c("[Controller Example] UAV Pose: %.3f %.3f %.3f | %.3f %.3f %.3f | %.3f %.3f %.3f | %.3f %.3f %.3f" % 
                    (uav_pose.pose.pose.position.x, uav_pose.pose.pose.position.y, uav_pose.pose.pose.position.z,           # from ekf， NED frame
                     uav_pose.twist.twist.linear.x,  uav_pose.twist.twist.linear.y,  uav_pose.twist.twist.linear.z,         # 这个数据似乎不是很准
                     uav_pose.twist.twist.angular.x,  uav_pose.twist.twist.angular.y,  uav_pose.twist.twist.angular.z,      # 需要准确数据, please refer to /vrpn_client_node/droneyee%i/pose
                     roll_t, pitch_t, yaw_t), color='blue', bold=True)
            is_uav_pose_updated = False

            # 获取当前时间
            current_time = rospy.Time.now().to_sec() - start_time

            if current_time < takeoff_duration:

                
                # 起飞阶段
                cmd = Twist()
                #cmd.linear.z = (target_altitude - -z_current) * 0.35   # 计算上升速度
                cmd.linear.z = 0.85                                     # 有一个最小起飞速度, TODO, 这个地方要调清楚控制律
                cmd.linear.z = -cmd.linear.z                            # for NED
                cmd_vel_pub.publish(cmd)
                print_c("[Controller Example] Taking off... Height: %.2f m" % (cmd.linear.z * current_time), color='blue', bold=True)

            elif current_time < takeoff_duration + 60.0:  # 画圆阶段：1分钟
                # 画圆阶段
                t_now = current_time - takeoff_duration  # 画圆阶段的时间

                x_d = r * math.cos(w * t_now)
                y_d = r * math.sin(w * t_now)

                # 计算速度命令
                cmd = Twist()
                cmd.linear.x = (x_d - x_current) * 0.5  # 比例控制，0.5 是增益
                cmd.linear.y = (y_d - y_current) * 0.5
                cmd.linear.z = 0.                       # 保持高度不变
                cmd.angular.z = 0.                      # 设置角速度以保持圆周运动
                cmd_vel_pub.publish(cmd)
                print_c("[Controller Example] Circling... Time: %.2f s" % t_now, color='blue', bold=True)
            else:
                # 降落阶段
                cmd = Twist()
                cmd.linear.z = -0.1  # 缓慢下降速度
                cmd.linear.z = -cmd.linear.z            # for NED
                cmd_vel_pub.publish(cmd)
                print_c("[Controller Example] Landing...", color='blue', bold=True)
                if uav_pose.pose.pose.position.z < 0.1:  # 接近地面时停止
                    cmd = Twist()
                    cmd_vel_pub.publish(cmd)
                    print_c("[Controller Example] Landed!", color='green', bold=True)

        rate.sleep()