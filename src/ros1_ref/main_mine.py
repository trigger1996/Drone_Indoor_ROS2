#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import yaml
import time
#
import rospy
import math
from collections import OrderedDict
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from drone_ros_centeralized_control.msg import UavCmd, UavState
from transforms3d.euler import quat2euler, euler2quat
#
from utils.vis import print_c
from utils.PID import PID_Position
from utils.functions import saturation, dead_zone
# from MavRouter_standard_ROS_2_0 import *


UAV_SPEED_X_DEAD_ZONE   = 1
UAV_MAX_SPEED_X = 2
UAV_MAX_SPEED_Y = 2
UAV_MAX_SPEED_Z = 2

# Initialize PID controller
pid_x = PID_Position(0, 1.0, 0.1, 0.05, -0.3, 0.3)
pid_y = PID_Position(0, 1.0, 0.1, 0.05, -0.3, 0.3)
pid_z = PID_Position(0, 1.0, 0.1, 0.05, -0.3, 0.3)

def calculate_velocity(err_x, err_y, err_z):
    velocity_x = pid_x.get_new_ctrl(err_x)
    velocity_y = pid_y.get_new_ctrl(err_y)
    velocity_z = pid_z.get_new_ctrl(err_z)

    # 限幅控制率
    velocity_x = saturation(velocity_x, UAV_MAX_SPEED_X, -UAV_MAX_SPEED_X)
    velocity_y = saturation(velocity_y, UAV_MAX_SPEED_Y, -UAV_MAX_SPEED_Y)
    velocity_z = saturation(velocity_z, UAV_MAX_SPEED_Z, -UAV_MAX_SPEED_Z)
    
    # 加一个死区，防止摇摆
    velocity_x = dead_zone(velocity_x, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE) 
    velocity_y = dead_zone(velocity_y, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE) 
    # velocity_z = dead_zone(velocity_z, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)

    return velocity_x,velocity_y,velocity_z

def is_arrived(x_current, y_current, z_current, x_tgt, y_tgt, z_tgt):
    # 判断是否到达目标点
    if abs(x_current - x_tgt) < 0.1 and abs(y_current - y_tgt) < 0.1 and abs(z_current - z_tgt) < 0.1:
        return True
    else:
        return False

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


def main():
    global is_uav_pose_updated, is_uav_state_updated, uav_pose, uav_state
    interval = 0.1  # 每隔interval秒调用一次

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
  
    # Load waypoints from map.yaml
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 脚本所在目录
    file_path = os.path.join(script_dir, '../model', 'mapt.yaml')  # 拼接路径
    #
    print_c("[Controller Example] Loading waypoints from %s" % file_path, color='yellow', bold=True)
    #
    with open(file_path, 'r') as f:
        waypoints = yaml.safe_load(f)['waypoint']

    for key, value in waypoints.items():
        print_c("point %s : %s" % (str(key), str(value)), color='yellow', bold=True)

    rate = rospy.Rate(5)
    for i in range(0, 5):
        arm_msg = set_arm_disarm_message(True)
        arm_disarm_pub.publish(arm_msg)
        #
        print_c("[Controller Example] try ARMING UAV !", color='yellow', bold=True)
        #
        rate.sleep()

    # 起飞：10秒内上升到0.8米高度 # 任务：1分钟
    takeoff_duration = 2.0  # 起飞时间print_c
    target_altitude = 0.8  # 目标高度
    task_duration = 60.0    # 任务时间

    rho = [ '4', '1', '3', '5', '6' , '2' , '7' , '8' , '9' , '10' ]
    # 按自定义顺序生成新字典
    sorted_waypoints = OrderedDict()
    for key in rho:
        if key in waypoints:  # 检查键是否存在
            sorted_waypoints[key] = waypoints[key]

    # sorted_waypoints = {k: waypoints[k] for k in rho}
    for key, value in sorted_waypoints.items():
        print_c("new point %s : %s" % (str(key), str(value)), color='blue', bold=True)

    start_time = rospy.Time.now().to_sec()
    for key, waypoint in sorted_waypoints.items():
        x_tgt, y_tgt, z_tgt, duration = waypoint
        print_c("now going to %s : %s" % (str(key), str(value)), color='yellow', bold=True)
        task_flag = False
        try:    
            while True:
                if is_uav_state_updated:
                    print_c("[Controller Example] UAV Mode %d, %d \t status: %d" % (uav_state.base_mode, uav_state.custom_mode, uav_state.system_status,), color='cyan', bold=True)
                    is_uav_state_updated = False
            
                if is_uav_pose_updated:
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
                        # #cmd.linear.z = (target_altitude - -z_current) * 0.35   # 计算上升速度
                        # cmd.linear.z = 0.85                                     # 有一个最小起飞速度, TODO, 这个地方要调清楚控制律
                        # cmd.linear.z = -cmd.linear.z                            # for NED
                        cmd.linear.x, cmd.linear.y , cmd.linear.z = calculate_velocity(0, 0, target_altitude - z_current)
                        cmd_vel_pub.publish(cmd)
                        print_c("[Controller Example] Taking off... Height: %.2f m" % (cmd.linear.z * current_time), color='blue', bold=True)

                    elif current_time < takeoff_duration + task_duration:
                        if not task_flag:
                            task_start = rospy.Time.now().to_sec()
                            task_flag = True

                        # Calculate velocity using PID
                        current_time = rospy.Time.now().to_sec()
                        elapsed_time = current_time - task_start

                        cmd = Twist()
                        cmd.linear.x, cmd.linear.y , cmd.linear.z = calculate_velocity(x_tgt-x_current, y_tgt-y_current, z_tgt-z_current)
                        cmd_vel_pub.publish(cmd)
        
                        # Check if the drone has reached the waypoint or if the time has expired
                        if elapsed_time > duration:
                            break
                        if is_arrived(x_current, y_current, z_current, x_tgt, y_tgt, z_tgt):
                            break

                        print_c("[Controller Example] go to %s point in time %.2f" % (key, elapsed_time), color='blue', bold=True)

                time.sleep(interval)

        except KeyboardInterrupt:
            print_c("程序已停止" , color='red', bold=True)
            break

    # 降落阶段
    while True:
        if is_uav_state_updated:
            print_c("[Controller Example] UAV Mode %d, %d \t status: %d" % (uav_state.base_mode, uav_state.custom_mode, uav_state.system_status,), color='cyan', bold=True)
            is_uav_state_updated = False
    
        if is_uav_pose_updated:
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

            cmd = Twist()
            # cmd.linear.z = -0.1  # 缓慢下降速度
            # cmd.linear.z = -cmd.linear.z            # for NED
            cmd.linear.x, cmd.linear.y , cmd.linear.z = calculate_velocity(0, 0,- z_current)
            cmd_vel_pub.publish(cmd)
            print_c("[Controller Example] Landing...", color='blue', bold=True)

            if uav_pose.pose.pose.position.z < 0.1:  # 接近地面时停止
                cmd = Twist()
                cmd_vel_pub.publish(cmd)
                print_c("[Controller Example] Landed!", color='green', bold=True)
                break
        

if __name__ == "__main__":
    main()