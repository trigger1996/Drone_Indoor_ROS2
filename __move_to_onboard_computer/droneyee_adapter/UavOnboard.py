#!/usr/bin/python3
import threading
import time
from pymavlink import mavutil
import serial
import warnings
from config import *
import os
import math
import logging

    
class Pose:
    def __init__(self, x, y, z, r, p, yaw) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.p = p
        self.yaw = yaw
        pass
    
class UAVOnBoard:
    POS_SRC_NONE  = -1
    POS_SRC_VICON = 0
    POS_SRC_LOCAL = 1
    POS_SRC_GPS   = 2
    POS_SRC_CALCULATED = 3
    
    def __init__(self, gcs_protocol="udp", gcs_config={"local_ip":LOCAL_IP,"gcs_ip":GCS_IP, "msg_in_port_gcs":MSG_IN_PORT_GCS, "msg_in_port_local":MSG_IN_PORT_LOCAL}, fcu_config={"port":FCU_PORT, "baud":FCU_BAUD}) -> None:
        self.pose = Pose(0,0,0,0,0,0)
        self.vel = Pose(0,0,0,0,0,0)
        self.goto_pose = None
        self.pos_source = self.POS_SRC_NONE # Position source
        self.mission_state = UAV_CMD_TASK_WAITE
        self.pos_got_ever = False
        self.ctrl_block_flag = True  # 用于其他任务暂停起飞和降落的标志, True: 可以持续运行，False: 立刻截止当前任务
        self.gcs_protocol = gcs_protocol
        self.fcu_master = None
        self.gcs_master_udpout = None
        self.gcs_master_udpin = None
        self.takeoff_confirm_without_position = False
        self.gcs_config = gcs_config
        self.fcu_config = fcu_config
        self.open_flag = True
        self.onboard_mavlink_init()
        self.should_shutdown = False
        if self.open_flag:
            print("连接初始化完成")
            self.gcs_master_udpin.port.settimeout(1)
            self.fcu_master.port.timeout = 1
            self.data_trans_begin()
        pass
    
    def onboard_mavlink_init(self):
        try:
            self.fcu_master = mavutil.mavlink_connection(self.fcu_config["port"], baud=self.fcu_config["baud"])
            self.fcu_master.mav.version = 'v2.0'
            print("飞控连接成功@" + self.fcu_config["port"] + " " + str(self.fcu_config["baud"]))
        except Exception as e:
            print(e)
            self.open_flag = False
            warnings.warn("打开串口出现错误，无法连接飞控，请检查串口顺序，并使能串口")
        if self.gcs_protocol == "uart":
            # TODO uart not tested
            self.open_flag = False
            warnings.warn("串口模式未测试")
            try:
                self.gcs_ser = serial.Serial("/dev/ttyUSB1", baudrate=500000)
                self.gcs_master_udpout = mavutil.mavlink_connection(self.gcs_ser,source_system=255, source_component=1)
                self.gcs_master_udpout.mav.version = 'v2.0'
            except Exception:
                self.open_flag = False
                warnings.warn("打开串口出现错误，无法连接飞控或地面站，请检查串口顺序，并使能串口")
        elif self.gcs_protocol == "udp":
            try:
                self.gcs_master_udpout = mavutil.mavlink_connection(f"udpout:{self.gcs_config['gcs_ip']}:{self.gcs_config['msg_in_port_gcs']}",source_system=255, source_component=1)
                self.gcs_master_udpout.mav.version = 'v2.0'
                print("打开udpout网口成功@" + f"udpout:{self.gcs_config['gcs_ip']}:{self.gcs_config['msg_in_port_gcs']}")
            except Exception as e:
                print(e)
                self.open_flag = False
                warnings.warn("打开udpout网口出现错误，无法连接飞控或地面站，请检查串口顺序，并使能串口")
            try:
                self.gcs_master_udpin = mavutil.mavlink_connection(f"udpin:{self.gcs_config['local_ip']}:{self.gcs_config['msg_in_port_local']}",source_system=255, source_component=1)
                self.gcs_master_udpin.mav.version = 'v2.0'
                print("打开udpin网口成功@" + f"udpin:{self.gcs_config['local_ip']}:{self.gcs_config['msg_in_port_local']}")
            except Exception as e:
                print(e)
                self.open_flag = False
                warnings.warn("打开udpin网口出现错误，无法连接飞控或地面站，请检查串口顺序，并使能串口") 
    
    def data_trans_begin(self):
        t1 = threading.Thread(target = self.data_gcs2computer)
        t2 = threading.Thread(target = self.data_fcu2gcs_t)
        t1.start()
        t2.start()
        
    def set_pose(self, pos):
        self.pose = pos
        
    def set_vel(self, vel):
        self.vel = vel


    def uav_send_speed_ned(self, spd_x_m_per_sec, spd_y_m_per_sec, spd_z_m_per_sec, yaw_degree=0):
        type_mask = 0b0000111111000111  # 忽略位置信息，只设置速度
        self.fcu_master.mav.set_position_target_local_ned_send(
            0,  # 时间戳，0 表示立即执行
            self.fcu_master.target_system, self.fcu_master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,  # 使用局部NED坐标系
            type_mask,
            0, 0, 0,  # 目标位置（忽略，因为我们设置了速度）
            spd_x_m_per_sec, spd_y_m_per_sec, spd_z_m_per_sec,  # 目标速度
            0, 0, 0,  # 目标加速度（忽略）
            yaw_degree * 3.1415 / 180., 0  # 目标偏航角度和偏航速率（忽略）
        )
        
    def uav_send_speed_FLU(self, spd_x_m_per_sec, spd_y_m_per_sec, spd_z_m_per_sec, yaw_degree=0, yaw_spd_deg = 0):
        type_mask = 0b0000111111000111  # 忽略位置信息，只设置速度
        self.fcu_master.mav.set_position_target_local_ned_send(
            0,  # 时间戳，0 表示立即执行
            self.fcu_master.target_system, self.fcu_master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_FLU,  # 使用FLU坐标系
            type_mask,
            0, 0, 0,  # 目标位置（忽略，因为我们设置了速度）
            spd_x_m_per_sec, spd_y_m_per_sec, spd_z_m_per_sec,  # 目标速度
            0, 0, 0,  # 目标加速度（忽略）
            yaw_degree * 3.1415 / 180., yaw_spd_deg / 57.3  # 目标偏航角度和偏航速率（忽略）
        )

    def uav_turn_yaw_rad(self, rad):
        # 北零 左逆负，右顺正 -pi -- pi
        type_mask = 0b0000101111111111  # 忽略位置信息，只设置速度
        self.fcu_master.mav.set_position_target_local_ned_send(
            0,  # 时间戳，0 表示立即执行
            self.fcu_master.target_system, self.fcu_master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_FLU,  # 使用FLU坐标系
            type_mask,
            0, 0, 0,  # 目标位置（忽略，因为我们设置了速度）
            0, 0, 0,  # 目标速度
            0, 0, 0,  # 目标加速度（忽略）
            rad, 0  # 目标偏航角度和偏航速率（忽略）
        )
        
    def uav_turn_yaw_speed_rad(self, speed_rad):
        # 北零 左逆负，右顺正 -pi -- pi
        type_mask = 0b0000101111111111  # 忽略位置信息，只设置速度
        self.fcu_master.mav.set_position_target_local_ned_send(
            0,  # 时间戳，0 表示立即执行
            self.fcu_master.target_system, self.fcu_master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_FLU,  # 使用FLU坐标系
            type_mask,
            0, 0, 0,  # 目标位置（忽略，因为我们设置了速度）
            0, 0, 0,  # 目标速度
            0, 0, 0,  # 目标加速度（忽略）
            0, speed_rad  # 目标偏航角度和偏航速率（忽略）
        )
        
    def uav_turn_yaw_angle(self, angle):
        type_mask = 0b0000101111111111  # 忽略位置信息，只设置速度
        self.fcu_master.mav.set_position_target_local_ned_send(
            0,  # 时间戳，0 表示立即执行
            self.fcu_master.target_system, self.fcu_master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_FLU,  # 使用FLU坐标系
            type_mask,
            0, 0, 0,  # 目标位置（忽略，因为我们设置了速度）
            0, 0, 0,  # 目标速度
            0, 0, 0,  # 目标加速度（忽略）
            angle/57.3, 0  # 目标偏航角度和偏航速率（忽略）
        )

    def uav_hover(self):
        self.uav_send_speed_FLU(0,0,0)

    def uav_land(self):
        for i in range(100):
            if not self.ctrl_block_flag:
                print("[INFO] LAND process stopped")
                break
            self.uav_send_speed_FLU(0,0,-0.2)
            print("landing")
            time.sleep(0.1)

    def uav_take_off(self):
        for i in range(50):
            if not self.ctrl_block_flag:
                print("[INFO] takeoff process stopped")
                logging.basicConfig(level=logging.INFO,
                                    filename='LOGS/new.log',
                                    format='%(asctime)s - [INFO] takeoff process stopped')
                break
            self.uav_send_speed_FLU(0,0,0.2, 160)
            print("traking off")
            time.sleep(0.1)
        self.uav_hover()

    def uav_takeoff_closed(self, height = 1.4):
        if not self.pos_got_ever:
            print("[WARNING] Uav position never got, will takeoff open-loop if you confirm again")
            global takeoff_confirm_without_position
            if takeoff_confirm_without_position:
                self.uav_take_off()
            takeoff_confirm_without_position = True
        else:
            height_before_takeoff = self.pose.z
            target_height = height_before_takeoff + height
            for i in range(200):
                # 最多两百次
                if not self.ctrl_block_flag:
                    print("[INFO] takeoff process stopped")
                    logging.basicConfig(level=logging.INFO,
                                    filename='LOGS/new.log',
                                    format='%(asctime)s - [INFO] takeoff process closed')
                    break
                if self.pose.z < target_height:
                    self.uav_send_speed_FLU(0,0,0.25)
                else:
                    print(f"[INFO] UAV get the target height at {self.pose.z}")
                    logging.basicConfig(level=logging.INFO,
                                    filename='LOGS/new.log',
                                    format='%(asctime)s - [INFO] UAV get the target height at {self.pose.z}')
                    break
    
    def arm_uav(self):
        self.fcu_master.mav.command_long_send(
            self.fcu_master.target_system, self.fcu_master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,  # Confirmation
            1,  # 1 to arm, 0 to disarm
            0, 0, 0, 0, 0, 0  # Unused parameters
        )

    def arm_and_takeoff(self):
        self.arm_uav()
        time.sleep(0.1)
        self.arm_uav()
        time.sleep(0.1)
        self.uav_take_off()

    def takeoff_and_turn(self, angle_degree = 180):
        self.arm_uav()
        time.sleep(0.1)
        self.arm_uav()
        time.sleep(0.1)
        self.uav_take_off()
        t = angle_degree / 60.
        for i in range(int(10*t)):
            self.uav_turn_yaw_angle(i*6)
            if i % 3 == 0:
                print("turning: " + str(i*6) + " degree.")
            time.sleep(0.1)
        
    def dis_arm_uav(self):
        self.fcu_master.mav.command_long_send(
            self.fcu_master.target_system, self.fcu_master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,  # Confirmation
            0,  # 1 to arm, 0 to disarm
            0, 0, 0, 0, 0, 0  # Unused parameters
        )
        
    def data_gcs2fcu_t(self):
        while True:
            try:
                # 从地面站接收消息
                msg = self.gcs_master_udpin.recv_match(blocking=True)
                if not msg:
                    continue
                print(msg)
                # 检查消息类型
                if msg.get_type() in ['VISION_POSITION_ESTIMATE', 'SET_POSITION_TARGET_LOCAL_NED', 'HEARTBEAT']:
                    # 将消息原样转发到飞控
                    continue
                    self.fcu_master.mav.send(msg)
            except KeyboardInterrupt:
                print("程序被用户中断")
                break

    def start_data_fcu2computer(self):
        import threading
        t = threading.Thread(target=self.data_fcu2gcs_t)
        t.start

    def data_gcs2computer(self):
        while not self.should_shutdown:
            try:
                # 从地面站接收指令
                msg = self.gcs_master_udpin.recv_match(blocking=False)

                # print(msg)
                if not msg:
                    continue
                if msg.get_type() == 'COMMAND_LONG':
                    msg = msg.to_dict()
                    cmd = msg['command']
                    conf = msg['confirmation']
                    param1 = msg['param1']
                    param2 = msg['param2']
                    param3 = msg['param3']
                    param4 = msg['param4']
                    param5 = msg['param5']
                    param6 = msg['param6']
                    param7 = msg['param7']
                    if cmd != mavutil.mavlink.MAV_CMD_DO_SET_MISSION_CURRENT:
                        # TODO 
                        # 限制控制线程
                        self.mission_state = UAV_CMD_TASK_WAITE
                    if cmd == mavutil.mavlink.MAV_CMD_NAV_TAKEOFF:
                        takeoff_height = param1
                        print(f"[CMD] TAKOFF {takeoff_height}")
                        if takeoff_height == 0:
                            self.uav_take_off()
                        else:
                            self.uav_takeoff_closed(takeoff_height)
                        pass
                    elif cmd == mavutil.mavlink.MAV_CMD_NAV_LAND:
                        print(f"[CMD] LAND")
                        self.uav_land()
                        pass
                    elif cmd == mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM:
                        arm_flag = param1
                        print(f"[CMD] ARM" if arm_flag else "[CMD] DISARM")
                        if arm_flag:
                            self.arm_uav()
                        else:
                            self.dis_arm_uav()
                        pass
                    elif cmd == mavutil.mavlink.MAV_CMD_DO_SET_MISSION_CURRENT:
                        mission_current = param1
                        print(f"[CMD] MISSION CURRENT {mission_current}")
                        if param1 == UAV_CMD_TASK_BEGIN:
                            self.mission_state = UAV_CMD_TASK_BEGIN
                        if param1 == UAV_CMD_TASK_END:
                            self.mission_state = UAV_CMD_TASK_END
                        if param1 == UAV_CMD_TASK_GOTO_WAIT:
                            self.mission_state = UAV_CMD_TASK_GOTO_WAIT
                            self.goto_pose = [param2, param3]
                        if param1 == UAV_CMD_INFO_TARGET_POS:
                            # self.mission_state = UAV_CMD_INFO_TARGET_POS
                            #目标是移动到target附近
                            goto_x = param2 - 1
                            goto_y = param3 - 1
                            self.goto_pose = [goto_x, goto_y]
                        if param1 == DRV_CMD_TASK_FOLLOW_PERSON:
                            self.mission_state = DRV_CMD_TASK_FOLLOW_PERSON
                    elif cmd == mavutil.mavlink.MAV_CMD_DO_PAUSE_CONTINUE:
                        continue_flag = param1  # 1: continue, 0: stop
                        print(f"[CMD] CONTINUE" if continue_flag else f"[CMD] STOP")
                    
                    pass
                elif msg.get_type() == 'VICON_POSITION_ESTIMATE':
                    msg = msg.to_dict()
                    self.pos_source = UAVOnBoard.POS_SRC_VICON
                    x = msg['x']
                    y = msg['y']
                    # print(x,y)
                    z = msg['z']
                    roll = msg['roll']
                    pitch = msg['pitch']
                    yaw = msg['yaw']
                    self.pose.x = x
                    self.pose.y = y
                    self.pose.z = z
                    self.pose.r = roll
                    self.pose.p = pitch
                    self.pose.yaw = yaw
                    self.pos_got_ever = True
                    pass
            except KeyboardInterrupt:
                break
            except TimeoutError:
                pass
            except socket.timeout:
                pass
    def data_fcu2gcs_t(self):
        last_print_time = time.time()
        while not self.should_shutdown:
            try:
                # 从飞控接收消息
                should_print = False
                msg = self.fcu_master.recv_match(blocking=False)
                if not msg:
                    continue
                # print(msg.get_type())
                if time.time() - last_print_time > 0.1:
                    #TODO
                    should_print = False
                    last_print_time = time.time()
                    # print(msg.get_type())
                if msg.get_type() == 'HEARTBEAT':
                    if should_print:
                        print('heart beat')
                if msg.get_type() == 'LOCAL_POSITION_NED':
                    m = msg.to_dict()
                    if should_print:
                        print(f"飞机位置NED："+
                            f"x : {m['x'] :.2f} "+
                            f"y : {m['y'] :.2f} "+
                            f"z : {m['z'] :.2f} "+
                            f"vx: {m['vx']:.2f} "+
                            f"vy: {m['vy']:.2f} "+
                            f"vz: {m['vz']:.2f} "
                            )
                    if self.pos_source == UAVOnBoard.POS_SRC_NONE or self.pos_source == UAVOnBoard.POS_SRC_LOCAL:
                        # 尚未置位何种来源
                        self.pos_source = UAVOnBoard.POS_SRC_LOCAL
                        self.pose.x = m['x']
                        self.pose.y = m['y']
                        self.pose.z = m['z']
                        self.vel.x = m['vx']
                        self.vel.y = m['vy']
                        self.vel.z = m['vz']
                        self.pos_got_ever = True
                        self.gcs_master_udpout.mav.local_position_ned_send(0, self.pose.x, self.pose.y, self.pose.z, self.vel.x, self.vel.y, self.vel.z)
                if msg.get_type() == 'ATTITUDE':
                    m = msg.to_dict()
                    if should_print:
                        print(f"飞机姿态："+
                            f"roll : {m['roll']:.2f} "+
                            f"pitch: {m['pitch']:.2f} "+
                            f"yaw  : {m['yaw']:.2f} "
                            )
                    if self.pos_source == UAVOnBoard.POS_SRC_NONE or self.pos_source == UAVOnBoard.POS_SRC_LOCAL:
                        self.pose.r = m['roll']
                        self.pose.p = m['pitch']
                        self.pose.yaw = m['yaw']
                        self.gcs_master_udpout.mav.attitude_send(0, self.pose.r, self.pose.p, self.pose.yaw, 0,0,0)
                    
                if msg.get_type() == 'GLOBAL_POSITION_INT':
                    if should_print:
                        print(msg.to_dict())
                # print(msg.get_type())
                # 检查消息类型
                if msg.get_type() in ['VISION_POSITION_ESTIMATE', 'SET_POSITION_TARGET_LOCAL_NED', 'HEARTBEAT']:
                    # 将消息原样转发到地面站
                    continue
                    self.gcs_master_udpout.mav.send(msg)
            except KeyboardInterrupt:
                print("程序被用户中断")
                break
            except Exception:
                print("eee2")
                # break

def test_ctrl_t():
    """测试线程
    """
    Uav.arm_uav()
    time.sleep(0.05)
    Uav.arm_uav()
    time.sleep(0.05)
    Uav.arm_uav()
    time.sleep(0.05)
    Uav.uav_take_off()
    for i in range(50):
        Uav.uav_hover()
        print("悬停")
        time.sleep(0.1)
    for i in range(50):
        Uav.uav_send_speed_FLU(0.3, 0.0, 0.0)
        print("向前飞行")
        time.sleep(0.1)
        
    for i in range(50):
        Uav.uav_send_speed_FLU(0.0, -0.3, 0.0)
        print("向右飞行")
        time.sleep(0.1)
    for i in range(50):
        Uav.uav_send_speed_FLU(0.0, 0.3, 0.0)
        print("向左飞行")
        time.sleep(0.1)
    Uav.uav_land()
    Uav.dis_arm_uav()

def test_ctrl_t2():
    """测试线程2
    """
    Uav.arm_and_takeoff()
    while True:
        # uav_send_speed_FLU(0.3, 0., 0.)
        # print("向前飞行")
        # time.sleep(0.1)
        # continue
        # arm_uav()
        # for i in range(15):
        #     uav_hover()
        #     print("悬停")
        #     time.sleep(0.1)
        for i in range(30):
            Uav.uav_send_speed_FLU(0.3, 0, 0)
            print("向前飞行")
            time.sleep(0.1)
            
        for i in range(30):
            Uav.uav_send_speed_FLU(0.0, -0.3, 0.0)
            print("向右飞行")
            time.sleep(0.1)
        for i in range(30):
            Uav.uav_send_speed_FLU(0.0, 0.3, 0.0)
            print("向左飞行")
            time.sleep(0.1)
            
        # uav_land()
        # time.sleep(5)
        # dis_arm_uav()

def test_turn():
    angle = 50
    print(f"turn to {angle}")
    Uav.uav_turn_yaw_angle(angle)
    time.sleep(10)
    angle += 50
    print(f"turn to {angle}")
    Uav.uav_turn_yaw_angle(angle)
    time.sleep(10)
    angle += 50
    print(f"turn to {angle}")
    Uav.uav_turn_yaw_angle(angle)
    time.sleep(10)
    angle += 50
    print(f"turn to {angle}")
    Uav.uav_turn_yaw_angle(angle)
    time.sleep(10)
    angle += 50
    print(f"turn to {angle}")
    Uav.uav_turn_yaw_angle(angle)
    time.sleep(10)
    angle += 50
    Uav.uav_land()

def test_turn_rad():
    rad = 0
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    rad = 3.14/4
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    rad = 3.14/2
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    rad = 3.14*3/4
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    rad = 3.14/2
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    rad = 0
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    rad = -3.14/4
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    rad = -3.14/2
    print(f"turn to {rad}")
    Uav.uav_turn_yaw_rad(rad)
    time.sleep(10)
    
    Uav.uav_land()


    

    


if __name__ == "__main__":
    # test_ctrl_t()
    # test_turn()
    
    Uav = UAVOnBoard()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("程序被用户中断")
            Uav.should_shutdown = True
            break
    # t1 = threading.Thread(target = Uav.data_gcs2computer)
    # t2 = threading.Thread(target = Uav.data_fcu2gcs_t)
    # t1.start()
    # t2.start()