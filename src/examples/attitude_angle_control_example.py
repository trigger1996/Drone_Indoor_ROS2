#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
import math
from nav_msgs.msg import Odometry
from drone_ros_centeralized_control.msg import UavCmd, UavState, AttitudeSetpoint2
from transforms3d.euler import quat2euler
from utils.vis import print_c

MAX_TILT = 15.0 * math.pi / 180.0   # 最大倾角 (15度, rad)

uav_pose = Odometry()
is_uav_pose_updated = False
def uav_odom_callback(msg):
    global uav_pose, is_uav_pose_updated
    uav_pose = msg
    is_uav_pose_updated = True

def set_arm_disarm_message(arm=True, disarm=False):
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
    rospy.init_node("attitude_angle_control_example", anonymous=True)

    drone_id = 3
    uav_cmd_topic_name = "/cmd_arm_disarm_{0}".format(drone_id)
    uav_att_topic_name = "/cmd_attitude_{0}".format(drone_id)

    arm_disarm_pub = rospy.Publisher(uav_cmd_topic_name, UavCmd, queue_size=1)
    cmd_att_pub    = rospy.Publisher(uav_att_topic_name, AttitudeSetpoint2, queue_size=1)

    # 订阅姿态
    drone_pose_topic_name = "/mavrouter/drone_pose_" + str(drone_id)
    rospy.Subscriber(drone_pose_topic_name, Odometry, uav_odom_callback)

    # ARM
    rate = rospy.Rate(5)
    for _ in range(5):
        arm_disarm_pub.publish(set_arm_disarm_message(True))
        print_c("[Angle Control Example] ARM UAV!", color="yellow", bold=True)
        rate.sleep()

    rospy.sleep(2.0)

    print_c("[Angle Control Example] Start!", color="green", bold=True)
    start_time = rospy.Time.now().to_sec()
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        if not is_uav_pose_updated:
            rate.sleep()
            continue
        is_uav_pose_updated = False

        t = rospy.Time.now().to_sec() - start_time
        cmd = AttitudeSetpoint2()
        cmd.id = drone_id

        if t < 5.0:   # 起飞阶段
            cmd.roll_body = 0.0
            cmd.pitch_body = 0.0
            cmd.yaw_body = 0.0
            cmd.thrust_body = 0.6

            print_c("[Controller Example] Taking Off... Time: %.2f s | cmd_rpy_trust: %f %f %f %f " % (t_now, cmd.roll_body, cmd.pitch_body, cmd.yaw_body, cmd.thrust_body), color='blue', bold=True)
        elif t < 10.0:  # 倾斜控制阶段
            # 目标角度：向前 pitch，但限制15度
            pitch_cmd = 10.0 * math.pi / 180.0
            pitch_cmd = max(min(pitch_cmd, MAX_TILT), -MAX_TILT)

            cmd.roll_body = 0.0
            cmd.pitch_body = pitch_cmd
            cmd.yaw_body = 0.0
            cmd.thrust_body = 0.55

            print_c("[Controller Example] Leaning Front... Time: %.2f s | cmd_rpy_trust: %f %f %f %f " % (t_now, cmd.roll_body, cmd.pitch_body, cmd.yaw_body, cmd.thrust_body), color='blue', bold=True)
        elif t < 16.0:  # 回正
            cmd.roll_body = 0.0
            cmd.pitch_body = 0.0
            cmd.yaw_body = 0.0
            cmd.thrust_body = 0.5

            print_c("[Controller Example] Leaning Back... Time: %.2f s | cmd_rpy_trust: %f %f %f %f " % (t_now, cmd.roll_body, cmd.pitch_body, cmd.yaw_body, cmd.thrust_body), color='blue', bold=True)            
        else:  # 刹停并落地
            cmd.roll_body = 0.0
            cmd.pitch_body = 0.0
            cmd.yaw_body = 0.0
            cmd.thrust_body = 0.2

            print_c("[Controller Example] Landing... Time: %.2f s | cmd_rpy_trust: %f %f %f %f " % (t_now, cmd.roll_body, cmd.pitch_body, cmd.yaw_body, cmd.thrust_body), color='blue', bold=True)  

        cmd_att_pub.publish(cmd)
        rate.sleep()

