#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pymavlink import mavutil
import time
import threading
import struct
import socket
import decimal
import rospy
import math
import configparser
import os
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist, PoseStamped
from drone_ros_centeralized_control.msg import UavCmd, UavState
from nav_msgs.msg import Odometry
import tf
from transforms3d.euler import quat2euler, euler2quat
from utils.vis import print_c
class MocapRouter(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app
        self.mocapNum = app.droneNum
        self.daemon = True
        rospy.init_node('MocapRouter', anonymous=True)
        for i in range(self.mocapNum):
            drone = app.drones[i]
            rospy.Subscriber("/vrpn_client_node/droneyee" +
                             str(i+1)+"/pos_sync", PoseStamped, drone.rosPosCb)
            rospy.Subscriber("/vrpn_client_node/droneyee" +
                             str(i+1)+"/vel_sync", PoseStamped, drone.rosVelCb)

    def run(self):
        rospy.spin()

class ROSReceiver:
    def __init__(self, app):
        self.app = app
        self.uavNum = app.droneNum  # 无人机数量
        self.drones = app.drones  # 所有无人机对象
        self.cmd_vel_subscribers = []  # 存储所有无人机的ROS订阅
        self.cmd_state_subscribers = []

        self.arm_disarm_vector = [0] * self.uavNum  # 存储解锁/上锁指令

        # 为每架无人机创建ROS订阅
        for i in range(1, self.uavNum + 1):
            cmd_vel_topic_name = "/cmd_vel_%d" % (i+1, )  # 订阅不同的 cmd_vel 话题
            cmd_vel_sub = rospy.Subscriber(cmd_vel_topic_name, Twist, self.cmd_vel_callback, callback_args=i)
            self.cmd_vel_subscribers.append(cmd_vel_sub)
            print("ROS Receiver initialized, listening to %s" % (cmd_vel_topic_name,))

            #
            arm_disarm_topic_name = "/cmd_arm_disarm_%d" % (i, )  # 订阅不同的 cmd_vel 话题
            arm_disarm_sub = rospy.Subscriber(arm_disarm_topic_name, UavCmd, self.arm_disarm_callback, callback_args=i)
            self.cmd_state_subscribers.append(arm_disarm_sub)

    def cmd_vel_callback(self, msg, drone_index):
        drone = self.drones[drone_index]
        drone.cmdVel[0] = msg.linear.x
        drone.cmdVel[1] = msg.linear.y
        drone.cmdVel[2] = msg.linear.z
        drone.cmdVel[3] = msg.angular.x
        drone.cmdVel[4] = msg.angular.y
        drone.cmdVel[5] = msg.angular.z
        #drone.cmdVel[6] = 0  

        drone.cmd_vel_update = True
        drone.matlabControlInited = True

        print("Received /cmd_vel_%d: %f, %f, %f" % (drone_index+1, msg.linear.x, msg.linear.y, msg.linear.z, ))

    def arm_disarm_callback(self, msg, drone_index):
        """
        处理解锁/上锁指令
        :param msg: Twist消息，msg.angular.z 用于传递指令（2=解锁，5=上锁）
        """
        drone_id = msg.id
        if drone_id == -1:
            print_c("[MavStandard Warning] All drones will be armed/disarmed.", color='yellow', bold=True)
        elif drone_id >= 1 and drone_id == drone_index:
            print_c("[MavStandard] Drone %d will be armed/disarmed." % (drone_id, ), color='green', bold=True)
        else:
            print_c("Invalid drone ID: %d / current_drone: %d" % (drone_id, drone_index, ), color='red', bold=True)
            return

        command = msg.is_arm
        if command == 1:        # 解锁
            for drone in self.drones:
                if drone_id == drone.nId or drone_id == -1:
                    drone.gotoGuided()
                    drone.arm()                    
                    print_c("Drone {0}: Armed.".format(drone.nId), color='green')               # CRITICAL切记: 此时遥控器切换至定点模式, 程控开
        elif command == -1:     # 上锁
            for drone in self.drones:
                if drone_id == drone.nId or drone_id == -1:
                    drone.disarm()
                    print_c("Drone {0}: Disarmed.".format(drone.nId), color='green')
        else:
            print_c("Invalid arm/disarm command: {0}".format(command), color='yellow')
        

class ROSSender:
    def __init__(self, app):
        self.app = app
        self.uavNum = app.droneNum  
        self.drones = app.drones
        self.drone_state_publishers = []
        self.drone_pose_publishers  = []
        #
        self.tf_broadcasters_base_link_2_base_link_ned = []
        self.tf_broadcasters_map_2_base_link_ned       = []   # 创建 TF 广播器

        for i in range(self.uavNum):
            drone_state_topic_name = "/mavrouter/drone_state_" + str(i+1)
            drone_pose_topic_name = "/mavrouter/drone_pose_"  + str(i+1)            # begin from 1
            #
            # state publishers
            drone_state_pub = rospy.Publisher(drone_state_topic_name, UavState, queue_size=1)
            self.drone_state_publishers.append(drone_state_pub)
            #
            # pose publishers
            drone_pose_pub = rospy.Publisher(drone_pose_topic_name, Odometry, queue_size=1)
            self.drone_pose_publishers.append(drone_pose_pub)

            # TODO
            # to publish TF
            # base_link_ned -> base_link
            self.tf_broadcasters_base_link_2_base_link_ned.append(tf.TransformBroadcaster())  # 创建 TF 广播器
            self.tf_broadcasters_map_2_base_link_ned.append(tf.TransformBroadcaster())

        #每 0.1s 发布一次（10Hz）
        rospy.Timer(rospy.Duration(0.1), self.publish_drone_state)

    def publish_drone_state(self, event):
        for i in range(self.uavNum):
            # msg = Float32MultiArray()
            # drone = self.drones[i]
            # msg.data = [
            #     i + 1, drone.batInfo[0], drone.batInfo[1] / 1000.0,
            #     drone.localPosNED[0], drone.localPosNED[1], drone.localPosNED[2],
            #     drone.attitude[0], drone.attitude[1], drone.attitude[2],
            #     drone.visionPose[0], drone.visionPose[1], drone.visionPose[2],
            #     drone.localPosNED[3], drone.localPosNED[4], drone.localPosNED[5],
            #     drone.visionPose[0], drone.visionPose[1], drone.visionPose[2],
            #     0, drone.connected, drone.system_status
            # ]
            # self.publishers[i].publish(msg)
            drone = self.drones[i]
            #
            pose_msg = Odometry()
            pose_msg.header.stamp = rospy.Time.now()
            pose_msg.header.frame_id = "base_link_ned"
            #
            # Define as NED frame !
            pose_msg.pose.pose.position.x = drone.visionPose[0]             # drone.localPosNED[0]      localPosNED is obtained from EKF， not Vicon
            pose_msg.pose.pose.position.y = drone.visionPose[1]             # drone.localPosNED[1]
            pose_msg.pose.pose.position.z = drone.visionPose[2]             # drone.localPosNED[2]
            pose_msg.twist.twist.linear.x = drone.localPosNED[3]
            pose_msg.twist.twist.linear.y = drone.localPosNED[4]
            pose_msg.twist.twist.linear.z = drone.localPosNED[5]
            #
            # Define follows NED frame !
            # [roll,pitch,yaw] = quat2euler([self.visionPose[3],self.visionPose[4],self.visionPose[5],self.visionPose[6]])
            # yaw = -yaw + math.pi/2
            roll_t  = drone.attitude[0]
            pitch_t = drone.attitude[1]
            yaw_t   = drone.attitude[2]
            wx_t    = drone.attitude[3]     # roll_speed
            wy_t    = drone.attitude[4]     # pitch_speed
            wz_t    = drone.attitude[5]     # yaw_speed
            quat_rxyz = euler2quat(roll_t, pitch_t, yaw_t, axes='sxyz')      # alternative axes='sxyz', axes='szyx', axes='rxyz', s代表静态坐标系, r代表旋转坐标系
            pose_msg.pose.pose.orientation.w = quat_rxyz[0]
            pose_msg.pose.pose.orientation.x = quat_rxyz[1]
            pose_msg.pose.pose.orientation.y = quat_rxyz[2]
            pose_msg.pose.pose.orientation.z = quat_rxyz[3]
            #
            # TODO
            # To check frames
            pose_msg.twist.twist.angular.x = wx_t
            pose_msg.twist.twist.angular.y = wy_t
            pose_msg.twist.twist.angular.z = wz_t
            #
            self.drone_pose_publishers[i].publish(pose_msg)

            state_msg = UavState()
            state_msg.header.stamp = rospy.Time.now()
            state_msg.id = drone.nId
            state_msg.mavtype = drone.mavtype
            state_msg.autopilot = drone.autopilot
            state_msg.base_mode = drone.base_mode
            state_msg.custom_mode = drone.custom_mode
            state_msg.system_status = drone.system_status
            state_msg.connected = drone.connected
            state_msg.bat_voltage = float(drone.batInfo[0])
            state_msg.bat_remaining = float(drone.batInfo[1])
            self.drone_state_publishers[i].publish(state_msg)

            #
            self.tf_broadcasters_base_link_2_base_link_ned[i].sendTransform(
                (0., 0., 0.),                                                                  # 平移（ENU）
                [ 0.7071068, 0.7071068, 0., 0. ],                                              #  x, y, z, w https://www.andre-gaschler.com/rotationconverter/
                rospy.Time.now(),                    # 时间戳
                "base_link_%d" % (i + 1),            # 子坐标系
                "base_link_ned_%d" % (i + 1)         # 父坐标系
            )

            self.tf_broadcasters_map_2_base_link_ned[i].sendTransform(
                (drone.visionPose[0], drone.visionPose[1], drone.visionPose[2]),
                [ quat_rxyz[0], quat_rxyz[1], quat_rxyz[2], quat_rxyz[3] ],
                rospy.Time.now(),                    # 时间戳
                "base_link_ned_%d" % (i + 1),        # 子坐标系
                "map"                                # 父坐标系
            )

class Drone():
    def __init__(self, addr,nId):
        self.addr = addr
        self._active = False
        self.last_packet_received = 0
        self.last_pos_updated = 0
        self.last_connection_attempt = 0
        self.cmdVel=[0]*7
        self.visionPose=[0]*9
        self.localPosNED=[0]*6
        self.attitude=[0]*6
        self.batInfo=[0]*2
        self.mode=0             # drones初始化过程中的参数传递
        self.conn = None
        self.nId = nId
        self.mavtype = 0
        self.autopilot = 0
        self.base_mode = 0
        self.custom_mode = 0
        self.system_status = 0
        self.connected = False
        self.cmd_vel_update = False
        self.matlabControlInited = False
        self.cmdlast = 0
        rospy.Subscriber("/droneyee"+str(self.nId)+"/mavros/vision_pose/pose", PoseStamped, self.rosPosCb)
        print("====drone %d launched with connect %s ==="%(self.nId,addr))
    # 回调函数，ros消息回调#/vrpn_client_node/droneyee%i/pos_sync
    def rosPosCb(self,msg):
        #
        # Critical
        # ENU frame to NED
        self.visionPose[0] =  msg.pose.position.y
        self.visionPose[1] =  msg.pose.position.x
        self.visionPose[2] = -msg.pose.position.z
        self.visionPose[3] =  msg.pose.orientation.w
        self.visionPose[4] =  msg.pose.orientation.x
        self.visionPose[5] =  msg.pose.orientation.y
        self.visionPose[6] =  msg.pose.orientation.z
        #print("recv pos_sync %d,%f,%f,%f"%(self.nId,self.visionPose[0],self.visionPose[1],self.visionPose[2]))
    # 回调函数，ros消息回调#/vrpn_client_node/droneyee%i/vel_sync
    def rosVelCb(self,msg):
        self.visionPose[7] = msg.pose.position.x
        self.visionPose[8] = msg.pose.position.y
        self.visionPose[9] = msg.pose.position.z
    # 打开连接
    def open(self):
        try:
            print("Opening connection to %s" % (self.addr,))
            self.conn = mavutil.mavlink_connection(self.addr)
            self._active = True
            self.last_packet_received = time.time()  # lie
            self.last_pos_updated = time.time()
        except Exception as e:
            print("Connection to (%s) failed: %s" % (self.addr, str(e)))
            self._active = False
    # 发送ARM指令
    def arm(self):
        if self.connected:
            self.conn.mav.command_long_send(self.conn.target_system,self.conn.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,0,
               1,0,0,0,0,0,0)
            print("Mav %d: arm" % (self.conn.target_system))
    # 发送DISARM指令
    def disarm(self):
        if self.connected:
            self.conn.mav.command_long_send(self.conn.target_system,self.conn.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,0,
               0,0,0,0,0,0,0)
            print("Mav %d: disarm" % (self.conn.target_system))
    def gotoGuided(self):
        if self.connected:
            #self.conn.wait_heartbeat(timeout=2)
            self.conn.mav.set_position_target_local_ned_send(0,       # time_boot_ms (not used)
                                                    0, 0,    # target system, target component
                                                    mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
                                                    0b0000111111000111, # type_mask (only speeds enabled)
                                                    0, 0, 0, # x, y, z positions (not used)
                                                    0, 0, 0, # x, y, z velocity in m/s
                                                    0, 0, 0, # x, y, z acceleration (not used)
                                                    0, 0)    # yaw,)OFFBOARD
            #mode_id = self.conn.mode_mapping()["STABILIZE"]
            self.conn.set_mode('OFFBOARD')
            #self.conn.mav.command_long_send(self.conn.target_system,self.conn.target_component,
               # mavutil.mavlink.MAV_CMD_NAV_GUIDED_ENABLE,0,
                #1,0,0,0,0,0,0)
              
            print("Mav %d: go guided " % (self.conn.target_system))
    # att_pos_mocap_send函数的用法需要查一下
    def update(self):
        if self.cmd_vel_update:
            self.cmd_vel_update = False
            self.conn.mav.set_position_target_local_ned_send(0,       # time_boot_ms (not used)
                                                    0, 0,    # target system, target component
                                                    mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
                                                    0b0000111111000111, # type_mask (only speeds enabled)
                                                    0, 0, 0, # x, y, z positions (not used)
                                                    self.cmdVel[0], self.cmdVel[1], self.cmdVel[2], # x, y, z velocity in m/s
                                                    0, 0, 0, # x, y, z acceleration (not used)
                                                    0, 0)    # yaw,)
            print("send cmd vel to uav %d==(%f,%f,%f)"%(self.nId,self.cmdVel[0],self.cmdVel[1],self.cmdVel[2]))     # for debugging

        else:
            if not self.matlabControlInited:
                self.conn.mav.set_position_target_local_ned_send(0,       # time_boot_ms (not used)
                                                        0, 0,    # target system, target component
                                                        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
                                                        0b0000111111000111, # type_mask (only speeds enabled)
                                                        0, 0, 0, # x, y, z positions (not used)
                                                        0, 0, 0, # x, y, z velocity in m/s
                                                        0, 0, 0, # x, y, z acceleration (not used)
                                                        0, 0)    # yaw,) 
                #print("send cmd vel to uav %d==(%f,%f,%f)"%(self.nId,self.cmdVel[0],self.cmdVel[1],self.cmdVel[2]))

                                           
        [roll,pitch,yaw] = quat2euler([self.visionPose[3],self.visionPose[4],self.visionPose[5],self.visionPose[6]])
        #print("send vision pose to uav %d==(%f,%f,%f,%f,%f,%f)"%(self.nId,self.visionPose[0],self.visionPose[1],self.visionPose[2],roll,pitch,yaw))
        self.conn.mav.vision_position_estimate_send(0,self.visionPose[0],self.visionPose[1],self.visionPose[2],roll,pitch,-yaw+math.pi/2)
    def recv_message(self):
        if self._active:
            while True:
                m = None
                try:
                    m = self.conn.recv_msg()
                except Exception as e:
                    print("Exception receiving message on addr(%s): %s" % (str(self.addr), str(e)))
                    self.conn.close()
                    m = None
                    break
                if m is None:
                    break
                self.last_packet_received = time.time()
                if  m.get_type() == "LOCAL_POSITION_NED":
                    now = time.time()
                    tt = now-self.last_pos_updated
                    self.last_pos_updated = now
                    if(tt>0.05):
                        print("Mav %d: RTT too long time %8.3f ms" % (self.conn.target_system,tt*1000))
                    self.localPosNED[0] = m.x
                    self.localPosNED[1] = m.y
                    self.localPosNED[2] = m.z
                    self.localPosNED[3] = m.vx
                    self.localPosNED[4] = m.vy
                    self.localPosNED[5] = m.vz
                    print("Mav %d: local pos (%f,%f,%f)" % (self.conn.target_system,m.x,m.y,m.z))
                elif m.get_type() == 'HEARTBEAT':
                    self.mavtype = m.type
                    self.autopilot = m.autopilot
                    self.base_mode = m.base_mode
                    self.custom_mode = m.custom_mode
                    self.system_status = m.system_status
                    print("MAV ID === %d,system_status === %f"%(self.nId,m.system_status))
                    self.connected = True
                    #print("Mav %d: type=%d,autopilot=%d,base_mode=%d,custom_mode=%d" % (self.conn.target_system,m.type,m.autopilot,m.base_mode,m.custom_mode))
                elif m.get_type() == 'BATTERY_STATUS':
                    self.batInfo[1] = m.voltages[0]
                    self.batInfo[0] = m.battery_remaining
                    #print("Mav %d: battery (%f,%f)" % (self.conn.target_system,m.voltages[0],m.battery_remaining))
                elif m.get_type() == 'ATTITUDE':
                    self.attitude[0] = m.roll
                    self.attitude[1] = m.pitch
                    self.attitude[2] = m.yaw
                    self.attitude[3] = m.rollspeed
                    self.attitude[4] = m.pitchspeed
                    self.attitude[5] = m.yawspeed
                    #print("Mav %d: attitude (%f,%f,%f)" % (self.conn.target_system,m.roll,m.pitch,m.yaw))
                elif m.get_type() == 'STATUSTEXT':
                    print("mav %d ,info message %d (%s)"%(self.conn.target_system,m.severity,m.text))
    # 关闭连接        
    def close(self):
        self.conn.close()
        self._active = False
    # 返回激活状态
    def active(self):
        return self._active
# MAVLinkRouter类用于接收和发送飞机的数据，保持所有飞机的连接状态
# MAVLinkRouter类有三个线程：
# connection_maintenance_thread线程用于维护所有飞机的连接状态
# receving_thread线程用于循环接收飞机发送来的数据
# 自己的主线程用于向飞机发送消息（这些数据通过由matlab线程和mocap线程接收过来），通过drone的update函数实现

# Drone类维护了一个和飞机的连接
# Drone提供了发送和接受飞机数据的接口
# Drone的连接字符串通过参数传入
# 连接参数addr的格式需要查一下？
class MAVLinkRouter(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)  
        self.connection_maintenance_target_should_live = False
        self.receving_thread_should_live = False
        self.inactivity_timeout = 5
        self.reconnect_interval = 2
        self.drones = app.drones
        self.uavNum = app.droneNum
        self.daemon = True
    # 这里面打开所有飞机的连接
    def create_connections(self):
        for dr in self.drones:
            dr.open()
        self.connection_maintenance_target_should_live = True
        self.receving_thread_should_live = True
    # 这个函数是connection_maintenance_thread线程的主函数，更新所有飞机的连接状态，每周期运行一次
    def maintain_connections(self):
        now = time.time()
        for dr in self.drones:
            if not dr.active():
                continue
            if now - dr.last_packet_received > self.inactivity_timeout:
                print("Connection (%s) timed out" % (dr.addr,))
                dr.close()
        for dr in self.drones:
            if not dr.active():
                if now - dr.last_connection_attempt > self.reconnect_interval:
                    dr.last_connection_attempt = now
                    dr.open()
    # 创建connection_maintenance_thread线程
    def create_connection_maintenance_thread(self):
        '''create and start helper threads and the like'''
        # 10Hz周期运行，调用maintain_connections
        def connection_maintenance_target():
            while self.connection_maintenance_target_should_live:
                self.maintain_connections()
                time.sleep(0.1)
        connection_maintenance_thread = threading.Thread(target=connection_maintenance_target)
        connection_maintenance_thread.setDaemon(True)
        connection_maintenance_thread.start()
    
    # 这个函数是receving_thread线程的主函数，接收飞机的数据，每周期运行一次
    def receiving_messages(self):
        for dr in self.drones:
            dr.recv_message()
    # 创建receving_thread线程
    def create_receving_thread(self):
        '''create and start receiving threads and the like'''
        # 100Hz周期运行，调用receiving_messages
        def receving_message_target():
            while self.receving_thread_should_live:
                self.receiving_messages()
                time.sleep(0.01)
        receving_thread = threading.Thread(target=receving_message_target)
        receving_thread.setDaemon(True)
        receving_thread.start()
    # 主线程，用于向飞机发送数据
    def run(self):
        self.create_connections()
        self.create_receving_thread()
        self.create_connection_maintenance_thread()
        # 先把所有飞机切换至offboard状态
        time.sleep(10)
        #for dr in self.drones:
        #    dr.gotoGuided()
        #    dr.arm()
        # 循环执行，向飞机发送数据，20Hz运行
        while True:
            # send messages
            for dr in self.drones:
            #for i in range(self.uavNum):
                if (dr.cmdVel[6]-3)==0 and dr.cmdVel[6]!=dr.cmdlast:
                    dr.gotoGuided()
                    print('offboard %f'%(dr.cmdVel[6]))
                    dr.cmdlast = 3
                    
                if (dr.cmdVel[6]-2)==0 and dr.cmdVel[6]!=dr.cmdlast:
                    dr.arm()
                    dr.cmdlast = 2
                    
                if (dr.cmdVel[6]-5)==0 and dr.cmdVel[6]!=dr.cmdlast:
                    dr.disarm()
                    dr.cmdlast = 5
                         
                dr.update()
                #print('updating')
            time.sleep(0.01)


class RouterApp():
    def __init__(self, args):
        BASEDIR = os.path.dirname(os.path.abspath(__file__))
        cf = configparser.ConfigParser()
        cf.read(os.path.join(BASEDIR, '../config/mav.conf'))
        self.droneNum = cf.getint("mav", "mav_num")
        self.drones = []

        print("MAV NUM === %d" % self.droneNum)
        for i in range(self.droneNum):
            port = cf.get("mav", "mav_port" + str(i+1))
            drone = Drone("udpin:0.0.0.0:"+port, i+1)
            self.drones.append(drone)

        # 初始化 MAVLinkRouter
        self.mavlinkRouter = MAVLinkRouter(self)

    def start_run(self):
        self.mavlinkRouter.start()                  # 启动MAVLink连接
        time.sleep(2)                               # 等待2秒，确保MAVLink正常运行
        
        # 初始化ROS组件
        # 通过self传递drones数据
        self.rosReceiver = ROSReceiver(self)        # 订阅 /cmd_vel_N,
        self.rosSender   = ROSSender(self)          # 发布 /drone_state_N
        rospy.spin()


if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser("MavRouter.py [options]")
    (opts, args) = parser.parse_args()
    
    rospy.init_node('MavRouter', anonymous=True)
    print("======init ros node MavRouter done!====")
    
    router = RouterApp(args)
    router.start_run()
    
    rospy.spin()
    
    

    # if len(args) == 0:
    #    print("Insufficient arguments")
    #    sys.exit(1)
