#!/usr/bin/pyhton2
# -*- coding: UTF-8 -*-
import copy
import math
from infe_rknn_with_gimbal import *
from a8_mini_protocol import *
import warnings
from config import *
from functions import MovingAverageFilter, saturation, dead_zone
# from handle_mavlink import Uav
from UavOnboard import UAVOnBoard
from UavOnboard import Pose
from DataTransferUDP import DataTransferUDP
import logging

class RknnError(Exception):
    pass
# 飞机
Uav = UAVOnBoard()
# 输入滤波器
target_img_x_err_filter     = MovingAverageFilter(window_size=6)
target_img_y_err_filter     = MovingAverageFilter(window_size=6)
target_size_filter          = MovingAverageFilter(window_size=6)
fps_filter = MovingAverageFilter(window_size=5)
# 输出滤波器
output_uav_vz_filter        = MovingAverageFilter(window_size=3)
output_uav_vy_filter        = MovingAverageFilter(window_size=3)
output_uav_vx_filter        = MovingAverageFilter(window_size=3)
output_uav_vyaw_filter      = MovingAverageFilter(window_size=3)
# yaw 角控制量不能设置滤波器
output_gim_vp_filter        = MovingAverageFilter(window_size=3)
output_gim_vy_filter        = MovingAverageFilter(window_size=3)
output_gim_p_filter         = MovingAverageFilter(window_size=3)
output_gim_y_filter         = MovingAverageFilter(window_size=3)
time_begin = None
"""=====================================================================================

    目标检测部分

====================================================================================="""
boxes, classes, scores = None, None, None
is_rknn_set = False
target_detected = False
img_to_save = None

def letter_box(im, new_shape, pad_color=(0,0,0), info_need=False):
    # Resize and pad image while meeting stride-multiple constraints
    shape = im.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])

    # Compute padding
    ratio = r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=pad_color)  # add border
    
    # if self.enable_ltter_box is True:
    #     self.letter_box_info_list.append(Letter_Box_Info(shape, new_shape, ratio, ratio, dw, dh, pad_color))
    if info_need is True:
        return im, ratio, (dw, dh)
    else:
        return im

def rknn_t():
    # Create RKNN object
    rknn = RKNNLite(verbose=False)
    rknn.load_rknn(path=RKNN_MODEL)
    _force_builtin_perm = False
    # pre-process config
    print('--> Config model')
    # rknn.config(
    #             reorder_channel='2 1 0',
    #             mean_values=[[0, 0, 0]],
    #             std_values=[[255, 255, 255]],
    #             optimization_level=3,
    #             target_platform = 'rk3588',
    #             # target_platform='rv1109',
    #             quantize_input_node= QUANTIZE_ON,
    #             output_optimize=1,
    #             force_builtin_perm=_force_builtin_perm
    #             )
    # print('done')
    
    # # Load rknn model
    # print('--> Loading model')
    # ret = rknn.load_rknn(path=RKNN_MODEL)
    # if ret != 0:
    #     print('Load yolov5-rknn model failed!')
    #     exit(ret)
    # print('done')

    # init runtime environment
    print('--> Init runtime environment')
    ret = rknn.init_runtime(core_mask=RKNNLite.NPU_CORE_0)
    # ret = rknn.init_runtime('rk3399pro', device_id='')
    if ret != 0:
        print('Init runtime environment failed')
        exit(ret)
    print('done')

    # Set inputs
    try:
        cap = cv2.VideoCapture(VIDEO_PATH)  # replace VIDEO_PATH with your video file path
    except Exception:
        raise RknnError("Invalid video addr:"+VIDEO_PATH)
    
    # time_name = str(int(time.time()))
    # out = cv2.VideoWriter('../videos/video_'+time_name+'.avi',fourcc, 20.0, (SHOW_IMG_SIZE_X,SHOW_IMG_SIZE_Y),isColor = True)
    global is_rknn_set, time_begin
    is_rknn_set = True
    time_begin = time.time()
    log_save_init()
    while True:
        try:
            # st = time.time()
            ret, img = cap.read()
            img = cv2.rotate(img, cv2.ROTATE_180)
            img = cv2.resize(img, (640, 640))
            # img =(img, 180)
            if not ret:
                break
            # 获取图像尺寸
            height, width, channels = img.shape
            cv2.imshow("init img", img)
            
            # 计算中心区域的起始点
            start_x = int((width-IMG_SIZE) / 2)
            start_y = int((height-IMG_SIZE) / 2)

            # 截取中间的 100x100 区域
            # 使用数组切片：image[y:y+h, x:x+w]
            # img = img[start_y:start_y + IMG_SIZE, start_x:start_x + IMG_SIZE]
            # img = cv2.resize(img, (SHOW_IMG_SIZE_X, SHOW_IMG_SIZE_Y))
            img_1 = letter_box(im= img.copy(), new_shape=(IMG_SIZE, IMG_SIZE), pad_color=(0,0,0))
            # img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
            cv2.imshow("after pre", img_1)
            cv2.waitKey(1)
            input_data = np.expand_dims(img_1, 0)
            # pre_t = time.time()
            outputs = rknn.inference(inputs=[input_data], inputs_pass_through=[0 if not _force_builtin_perm else 1])
            # inf_t = time.time()
            # post process
            # input0_data = outputs[0]
            # input1_data = outputs[1]
            # input2_data = outputs[2]

            # input0_data = input0_data.reshape([3,-1]+list(input0_data.shape[-2:]))
            # input1_data = input1_data.reshape([3,-1]+list(input1_data.shape[-2:]))
            # input2_data = input2_data.reshape([3,-1]+list(input2_data.shape[-2:]))

            # input_data = list()
            # input_data.append(np.transpose(input0_data, (2, 3, 0, 1)))
            # input_data.append(np.transpose(input1_data, (2, 3, 0, 1)))
            # input_data.append(np.transpose(input2_data, (2, 3, 0, 1)))

            global boxes, classes, scores  # added zbw: 为了和通讯程序同步
            boxes, classes, scores = post_process_3588(outputs)
            # post_t = time.time()
            # print(len(classes))
            # yolov5_post_process(input_data)
            if boxes is not None:
                boxes_t = []
                classes_t = []
                scores_t = []
                for i in range(len(boxes)):
                    if classes[i] in target_id_list and scores[i]>0.6:
                        boxes_t.append(boxes[i])
                        classes_t.append(classes[i])
                        scores_t.append(scores[i])
                if len(boxes_t) != 0:
                    draw(img, boxes_t, scores_t, classes_t)
                    # log_save_once(boxes_t, scores_t, classes_t)
            # filter_t = time.time()    
            point_color2 = (5, 240, 5)  # 点的颜色，这里是绿色，格式为 (B, G, R)
            cv2.circle(img, (int(SHOW_IMG_SIZE_X/2), int(SHOW_IMG_SIZE_Y/2)), 5, point_color2, -1)
            fps = target_process(img)
            # cv2.putText(img, f'FPS:{fps:.1f}',
            #         (SHOW_IMG_SIZE_X-100, SHOW_IMG_SIZE_Y - 15),
            #         cv2.FONT_HERSHEY_SIMPLEX,
            #         0.6, (0, 0, 255), 2)
            # gimbal_control()
            
            # img_2 = cv2.resize(img_1, (640, 640))
            
            cv2.imshow("post process result", img)
            global img_to_save
            img_to_save = copy.copy(img)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to quit
                break
            # et = time.time()
            # print(f"process time:{et-st:.4f}; pre:{pre_t - st:.4f}; inf:{inf_t - st:.4f}, post:{post_t-st:.4f}, filter{filter_t-st:.4f}")
        except KeyboardInterrupt as e:
            print("KeyboardInterrupt1")
            cap.release()
            cv2.destroyAllWindows()
            rknn.release()

    print("KeyboardInterrupt2")
    cap.release()
    # out.release()
    cv2.destroyAllWindows()
    rknn.release()
    # print("SAVED：name:"+str(time_name)+".avi")


"""=====================================================================================

    数据保存部分

====================================================================================="""
VIDEO_FRAME_PRE_SEC  = 20.0
VIDEO_FRAME_TIME     = 1.0 / VIDEO_FRAME_PRE_SEC
def video_save_t():
    time_name = 0
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    for file_name_n in range(1000):
        file_path = '../videos/video_'+str(time_name)+'.avi'
        if os.path.exists(file_path):
            time_name += 1
    out = cv2.VideoWriter('../videos/video_'+str(time_name)+'.avi',fourcc, VIDEO_FRAME_PRE_SEC, (SHOW_IMG_SIZE_X,SHOW_IMG_SIZE_Y),isColor = True)
    while(True):
        if should_save:
            out.release()
            print("SAVED：name:"+str(time_name)+".avi")
        if img_to_save is None:
            time.sleep(VIDEO_FRAME_TIME)
            continue
        try:
            out.write(img_to_save)
            time.sleep(VIDEO_FRAME_TIME)
        except KeyboardInterrupt as e:
            print("KeyboardInterrupt3")
            out.release()
            print("SAVED：name:"+str(time_name)+".avi")

LOG_FILE = None
def log_save_init():
    time_name = 0
    for file_name_n in range(1000):
        file_path = '../LOGS/log_'+str(time_name)+'.csv'
        if os.path.exists(file_path):
            time_name += 1
    global LOG_FILE
    LOG_FILE = file_path
    with open(LOG_FILE,"w") as log_f:
        log_f.write("time,target_id,left,top,right,bottom,score\n")
        log_f.close()
    # Waiting for rknnset

def log_save_once(boxes, scores, classes):
    with open(LOG_FILE,"a+") as log_f:
        t = time.time() - time_begin
        for i in range(len(boxes)):
            left, top, right, bottom = boxes[i]
            log_f.write(f"{t:.3f},{classes[i]:d},{left:.1f},{top:.1f},{right:.1f},{bottom:.1f},{scores[i]:.4f}\n")
        log_f.close()
"""=====================================================================================

    飞机控制部分

====================================================================================="""

desired_target_size = 36000
def uav_gimbal_ctrl_front_pull(x_err, y_err, target_size_err):
    """相机前视，飞机左右飞以及左右转控制目标在图像中的x，前后飞控制大小，云台控制pitch控制目标在图像中的Y
        拉模式表示跟着走，保持一定距离
    """
    """
        可以是这样的策略：
        转向：
            云台先转，在一个区间内，称为舒适区间[gim_soft_min, gim_soft_max] yaw pitch均是
            当转到该区间边界时，飞机开始旋转，让云台回到舒适区间（级联or直接将飞机角速度纳入云台的控制率）
        前后：
            
        左右：
            
        云台俯仰：
            
        飞机高度：
            
        目前是加了一个角度
    """
    uav_target_spd_x = - PID_uav_x_para.get_new_ctrl(target_size_err)  # 小的话向前走
    uav_target_yaw_speed = PID_uav_vyaw_para.get_new_ctrl(x_err)  # 为正向左转
    uav_target_spd_y = PID_uav_y_para.get_new_ctrl(x_err)  # err为正,目标在图像中心左侧，向左转了，所以向右走，为负
    gimbal_target_pitch_speed = - PID_gim_vp_para.get_new_ctrl(y_err)  # err为正，目标位于图像中心上侧，要向上转，正着转
    
    uav_target_spd = [uav_target_spd_x, uav_target_spd_y, 0]
    uav_target_angl = None
    uav_target_angle_spd = [0,0,uav_target_yaw_speed]  # RPY
    gimbal_target_angle = None
    gimbal_target_spd = [0, gimbal_target_pitch_speed, 0] # RPY
    
    return uav_target_spd, uav_target_angl, uav_target_angle_spd, gimbal_target_angle, gimbal_target_spd

from PID import PID_Incremental, PID_Position
# PID_uav_x_para = PID_Incremental(0, 0.3, 0, 0, -0.2, 0.2)
# PID_uav_y_para = PID_Incremental(0, 0.3, 0, 0, -0.2, 0.2)
# PID_gim_vp_para = PID_Incremental(0, 0.3, 0.01, 0.2, -10., 10.)
# 640*640=400000
# 30000
PID_uav_x_para = PID_Position(0, 0.000035, 0.000000001, 0.00002, -0.5, 0.5)
PID_uav_y_para = PID_Position(0, 0.0025, 0.00000001, 0.00015, -0.5, 0.5)
PID_gim_vp_para = PID_Incremental(0, 0.3, 0.01, 0.2, -10., 10.)
PID_uav_vyaw_para = PID_Incremental(0, 0.3, 0.01, 0.2, -10., 10.)
def uav_gimbal_ctrl_front_parallel(x_err, y_err, target_size_err):
    """相机前视，飞机左右控制目标在图像中的x，前后飞控制大小，云台控制pitch控制目标在图像中的Y
        平行模式表示不旋转跟着走，保持一定距离
    """

    uav_target_spd_x = PID_uav_x_para.get_new_ctrl(target_size_err)  # 小的话向前走
    uav_target_spd_y = - PID_uav_y_para.get_new_ctrl(x_err)  # err为正,目标在图像中心左侧，要向左，为正
    gimbal_target_pitch_speed = - PID_gim_vp_para.get_new_ctrl(y_err)  # err为正，目标位于图像中心上侧，要向上转，正着转
    
    # uav_target_spd_x = -k_x * (target_size_ - desired_target_size)  # 小的话向前走
    # uav_target_spd_y = - k_y * x_err  # err为正,目标在图像中心右侧，要向右
    # gimbal_target_pitch_speed = -0.01 * y_err  # err为正，目标位于图像中心下侧，要向下转，负着转
    
    uav_target_spd = [uav_target_spd_x, uav_target_spd_y, 0]
    uav_target_yaw_degree = None
    uav_target_yaw_spd_degree = 0  # yaw
    gimbal_target_angle = None
    gimbal_target_spd = [0, gimbal_target_pitch_speed, 0] # R(uncontrolable)PY
    
    return uav_target_spd, uav_target_yaw_degree, uav_target_yaw_spd_degree, gimbal_target_angle, gimbal_target_spd
    
    # return uav_target_spd_x, uav_target_spd_y, gimbal_target_pitch_speed

def uav_gimbal_ctrl_down():
    """相机下视，飞机左右飞控制目标在图像中的X_img，前后飞控制Y_img，云台控制pitch控制目标在图像中的Y
    """
    pass

def uav_ctrl_gimbal_down():
    """相机下视不动，飞机左右控制X_img，前后控制Y_img，上下控制目标大小
    """
    pass

def uav_ctrl_gimbal_front():
    """相机前视视不动，飞机左右控制X_img，上下控制Y_img，前后控制目标大小
    """
    pass
print_num = 0
uav_flight_height = 1.4
def uav_control_once(sim_mode = False):
    # logger.info("uav ctrl once")
    # print("uav ctrl once")
    # logging.basicConfig(level=logging.INFO,
    #                     filename='LOGS/new.log',
    #                     format='%(asctime)s - INFO] DRV_CMD_TASK_FOLLOW_PERSON Begin')
    if not target_detected:
        Uav.uav_hover()
        return
    if not is_rknn_set:
        print("rknn not set!")
        return
    # 提取目标在图像中的位置误差和大小
    filtered_img_x_err = target_img_x_err_filter.get_value()
    filtered_img_y_err = target_img_y_err_filter.get_value()
    target_size = target_size_filter.get_value()
    # 计算控制率
    # 平行模式
    uav_target_spd, uav_target_yaw_degree, uav_target_yaw_spd_degree, gimbal_target_angle, gimbal_target_spd = uav_gimbal_ctrl_front_parallel(
        filtered_img_x_err, filtered_img_y_err, target_size - desired_target_size
    )
    # FLU 控制高度
    uav_target_spd[2] = - 0.25 * (math.fabs(Uav.pose.z) - uav_flight_height)
    # 提取控制量 并且滤波
    uav_target_spd_x = output_uav_vx_filter.get_value(uav_target_spd[0])
    uav_target_spd_y = output_uav_vy_filter.get_value(uav_target_spd[1])
    uav_target_spd_z = output_uav_vz_filter.get_value(uav_target_spd[2])
    uav_target_yaw_spd_degree = output_uav_vyaw_filter.get_value(uav_target_yaw_spd_degree)
    
    # if gimbal_target_angle is None:
    #     # 不控制angle
    #     gimbal_target_pitch_speed = output_gim_vp_filter.get_value(gimbal_target_spd[1])
    #     gimbal_target_yaw_speed   = output_gim_vy_filter.get_value(gimbal_target_spd[2])
    # else:
    #     # 控制angle
    #     gimbal_target_pitch = output_gim_p_filter.get_value(gimbal_target_angle[1])
    #     gimbal_target_yaw   = output_gim_y_filter.get_value(gimbal_target_angle[2])

    # 限幅控制率
    uav_target_spd_x = saturation(uav_target_spd_x, UAV_MAX_SPEED_X, -UAV_MAX_SPEED_X)
    uav_target_spd_y = saturation(uav_target_spd_y, UAV_MAX_SPEED_Y, -UAV_MAX_SPEED_Y)
    uav_target_spd_z = saturation(uav_target_spd_z, UAV_MAX_SPEED_Z, -UAV_MAX_SPEED_Z)
    uav_target_yaw_spd_degree = saturation(uav_target_yaw_spd_degree, UAV_MAX_SPEED_YAW_DEGREE, -UAV_MAX_SPEED_YAW_DEGREE)
    # 云台已经有satuation了
    # gimbal_target_yaw_speed   = saturation(gimbal_target_yaw_speed)
    # gimbal_target_pitch_speed = saturation(gimbal_target_pitch_speed)
    # 加一个死区，防止摇摆
    uav_target_spd_x = dead_zone(uav_target_spd_x, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE) 
    uav_target_spd_y = dead_zone(uav_target_spd_y, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE) 
    uav_target_spd_z = dead_zone(uav_target_spd_z, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE) 
    # uav_target_yaw_spd_degree = dead_zone(uav_target_yaw_spd_degree, UAV_SPEED_YAW_DEAD_ZONE_DEGREE, UAV_SPEED_YAW_DEAD_ZONE_DEGREE)
    # gimbal_target_yaw_speed   = dead_zone(gimbal_target_yaw_speed, 5, 5)
    # gimbal_target_pitch_speed = dead_zone(gimbal_target_pitch_speed, 5, 5)
    # added forbidan area
    # if Uav.pose.y < -0.5:
    #     uav_target_spd_x = min(0.0, uav_target_spd_x)
    global print_num
    print_num += 1
    if print_num > 5:
        print_num = 0
        print(f"当前目标大小:S: {target_size}")
        print(f"当前目标位置误差： X: {filtered_img_x_err}, Y: {filtered_img_y_err}")
        print(f"设置飞机速度:x: {uav_target_spd_x}, y: {uav_target_spd_y}, z: {uav_target_spd_z}")
        print(f"设置飞机角(速)度:yaw: {uav_target_yaw_degree}, yaw_spd: {uav_target_yaw_spd_degree}")
        print("+"*30)
        print()
        # print(f"设置云台速度:R: P:{gimbal_target_pitch_speed} Y: {gimbal_target_yaw_speed}")
        # print(f"当前云台角度:R: {connect.pose.roll} P: {connect.pose.pitch} Y: {connect.pose.yaw}")
        logger.info(f"当前目标大小:S: {target_size}")
        logger.info(f"设置飞机速度:x: {uav_target_spd_x}, y: {uav_target_spd_y}, z: {uav_target_spd_z}")
        logger.info(f"设置飞机角(速)度:yaw: {uav_target_yaw_degree}, yaw_spd: {uav_target_yaw_spd_degree}")
        # logger.info(f"设置云台速度:R: P:{gimbal_target_pitch_speed} Y: {gimbal_target_yaw_speed}")
        # logger.info(f"当前云台角度:R: {connect.pose.roll} P: {connect.pose.pitch} Y: {connect.pose.yaw}")
    # uav_target_spd_x = 0
    if not sim_mode:
        # 控制输出
        Uav.vel_mode = Uav.VEL_MODE_FRD
        if uav_target_yaw_degree is None:
            if True:
                # yaw 角速度模式
                # Uav.uav_send_speed_FLU(uav_target_spd_x, uav_target_spd_y, uav_target_spd_z, TARGET_YAW_DEGREE) #, uav_target_yaw_spd_degree)
                Uav.vel_set_frd.x, Uav.vel_set_frd.y, Uav.vel_set_frd.z = uav_target_spd_x, -uav_target_spd_y, -uav_target_spd_z
            else:
                # yaw 角手动积分模式
                target_yaw_deg = Uav.pose.yaw * 57.3 + uav_target_yaw_spd_degree * 0.05
                target_yaw_deg = (target_yaw_deg + 180) % 360 - 180
                # Uav.uav_send_speed_FLU(uav_target_spd_x, uav_target_spd_y, uav_target_spd_z, target_yaw_deg) #, 0)
                Uav.vel_set_frd.x, Uav.vel_set_frd.y, Uav.vel_set_frd.z = uav_target_spd_x, -uav_target_spd_y, -uav_target_spd_z
        else:
            Uav.vel_set_frd.x, Uav.vel_set_frd.y, Uav.vel_set_frd.z = uav_target_spd_x, -uav_target_spd_y, -uav_target_spd_z
            # Uav.uav_send_speed_FLU(uav_target_spd_x, uav_target_spd_y, uav_target_spd_z, uav_target_yaw_degree) #, uav_target_yaw_spd_degree, 5)
        # if gimbal_target_angle is None:
        #     # 云台速度模式
        #     connect.send_set_velocity_message(gimbal_target_yaw_speed, gimbal_target_pitch_speed)
        # else:
        #     # 云台角度模式
        #     connect.send_set_pose_message(gimbal_target_yaw, gimbal_target_pitch)


#TODO
pid_controller_x = PID_Position(0, 1, 0.0001, 0.003, -0.3, 0.3)
pid_controller_y = PID_Position(0, 1, 0.0001, 0.003, -0.3, 0.3)
def uav_goto(x,y,sim_mode = False):
    
    # logging.basicConfig(level=logging.INFO,
    #                     filename='LOGS/new.log',
    #                     format='%(asctime)s - INFO] UAV_CMD_TASK_GOTO_WAIT Begin')
    pid_controller_x.ref = x
    pid_controller_y.ref = y
    uav_target_spd_x = pid_controller_x.get_new_ctrl(Uav.pose.x)
    uav_target_spd_y = pid_controller_y.get_new_ctrl(Uav.pose.y)

    # 加一个死区，防止摇摆
    uav_target_spd_x = dead_zone(uav_target_spd_x, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE) 
    uav_target_spd_y = dead_zone(uav_target_spd_y, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE) 
    # uav_target_spd_z = dead_zone(uav_target_spd_z, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)

    # 打印当前位置和姿态
    global print_num
    print_num += 1
    if print_num > 15:
        print_num = 0
        print(f"设置飞机速度:x: {-uav_target_spd_y}, y: {uav_target_spd_x}, z: {0}")
        print(f'当前飞机位置:x: {Uav.pose.x}, y: {Uav.pose.y}')
        print(f'当前目标位置:x: {Uav.goto_pose[0]}, y: {Uav.goto_pose[1]}')
        logger.info(f"设置飞机速度:x: {-uav_target_spd_y}, y: {uav_target_spd_x}, z: {0}")
        logger.info(f'当前飞机位置:x: {Uav.pose.x}, y: {Uav.pose.y}')
        # logging.basicConfig(level=logging.INFO,
        #                 filename='LOGS/new.log',
        #                 format='%(asctime)s - INFO] 当前飞机位置:x: {Uav.pose.x}, y: {Uav.pose.y}')

    if not sim_mode:
        # 控制输出
        Uav.uav_send_speed_FLU(-uav_target_spd_y, uav_target_spd_x, 0, 0)

should_save = False
control_mode = WAITING
last_ctrl_mode = None
TARGET_YAW_DEGREE = 180
# TARGET_YAW_DEGREE = 1
UAV_CTRL_UDP = 0
UAV_CTRL_GCS = 1
UAV_CONTROL_METHOD = UAV_CTRL_GCS
def control_t():
    # 等待rknn线程启动
    print("[INFO] Control thread waiting for RKNN")
    # while not is_rknn_set:
    #     time.sleep(0.2)
    # 开启控制线程
    print("[INFO] Control thread Begin")
    # logging.basicConfig(level=logging.INFO,
    #                     filename='LOGS/new.log',
    #                     format='%(asctime)s - INFO] Control thread Begin')
    # 不用管
    if UAV_CONTROL_METHOD == UAV_CTRL_UDP:
        print("[INFO] Control thread UAV_CTRL_UDP_local")
        while True:
            global control_mode, last_ctrl_mode
            
            if control_mode == ARM:
                if control_mode != last_ctrl_mode:
                    print("ARMING")
                Uav.arm_uav()
            if control_mode == DISARM:
                if control_mode != last_ctrl_mode:
                    print("DISARMING")
                Uav.dis_arm_uav()
            if control_mode == WAITING:
                if control_mode != last_ctrl_mode:
                    print("WAITING")
                pass
            if control_mode == TAKEOFF:
                Uav.takeoff_and_turn(TARGET_YAW_DEGREE)
                control_mode = HOVER
            if control_mode == HOVER:
                if control_mode != last_ctrl_mode:
                    print("hovering")
                Uav.uav_hover()
            if control_mode == TRACK:
                if control_mode != last_ctrl_mode:
                    print("tracking")
                uav_control_once()
            if control_mode == LAND:
                Uav.uav_land()
            last_ctrl_mode = control_mode
            time.sleep(0.05)
        # break
    elif UAV_CONTROL_METHOD == UAV_CTRL_GCS:
        print("[INFO] Control thread UAV_CTRL_GCS")
        # logging.basicConfig(level=logging.INFO,
        #                 filename='LOGS/new.log',
        #                 format='%(asctime)s - INFO] Control thread UAV_CTRL_GCS')
        logger.info("[INFO] Control thread UAV_CTRL_GCS")
        # TODO
        is_began = False
        while True:
            if Uav.mission_state == UAV_CMD_TASK_BEGIN:
                is_began = True
            if not is_began:
                time.sleep(0.05)
                continue
            Uav.mission_state = DRV_CMD_TASK_FOLLOW_PERSON
            logger.info(f"current miss: {Uav.mission_state}")
            if Uav.is_takingoff:
                time.sleep(0.05)
                continue
            if Uav.mission_state == UAV_CMD_TASK_BEGIN:
                # uav_goto(2,0)
                uav_control_once()
            if Uav.mission_state == UAV_CMD_TASK_END:
                # uav_goto(2,2)
                global should_save
                should_save = True
            if Uav.mission_state == UAV_CMD_TASK_GOTO_WAIT:
                # if target_detected:
                #     pass
                #     # uav_control_once()
                # else:
                x = Uav.goto_pose[0]
                y = Uav.goto_pose[1]
                uav_goto(x,y)
            # if Uav.mission_state == UAV_CMD_INFO_TARGET_POS:
                # x = Uav.goto_pose[0]-1
                # y = Uav.goto_pose[1]-1
                # uav_goto(x,y)
            if Uav.mission_state == DRV_CMD_TASK_FOLLOW_PERSON:
                uav_control_once()
            time.sleep(0.05)
    logger.info("[INFO] Control thread End")
    
    


"""=====================================================================================

    目标处理部分

====================================================================================="""
last_process_time = None
def target_process(img):
    global classes
    global target_detected
    global last_process_time
    if last_process_time is None:
        fps = 0
        last_process_time = time.time()
    else:
        fps_filter.add_sample(time.time()-last_process_time)
        fps = 1.0/fps_filter.get_value()
        last_process_time = time.time()
    if classes is None:
        log_info("No Classes detected")
        # time.sleep(0.05)
        target_detected = False
        return fps
    # classes: np.array
    # a = np.array([1])
    max_index = -1
    max_box_size = 0
    
    for (i, one_class) in enumerate(classes) :
        # if one_class != target_class_id:
        # print(one_class)
        # print(type(one_class))
        # print(one_class in target_id_list)
        if not (one_class in target_id_list) or scores[i] < 0.65:
        # if not one_class.startwith(target_class_id):
            # log_info('not target')
            # print(('not target'))
            continue
        # print(boxes[i])
        left, top, right, bottom = boxes[i]
        # top, left, right, bottom = boxes[i]
        box_size = (bottom - top) * (right - left)
        if math.fabs(box_size) > max_box_size:
            max_index = i
            max_box_size = math.fabs(box_size)
    
    if max_index == -1:
        target_detected = False
        return fps
    # print("detected " + str(max_index))
    # print(max_box_size)
    if max_box_size != 0:
        target_size_filter.add_sample(max_box_size)
    target_detected = True
    # top, left, right, bottom = boxes[max_index]
    left, top, right, bottom = boxes[max_index]
    target_y = (top + bottom) / 2.0 
    target_x = (left + right) / 2.0 
    # 定义点的位置和颜色
    point_position = (int(target_x), int(target_y))  # 点的坐标，例如 (x, y) = (250, 250)
    point_color1 = (0, 0, 255)  # 点的颜色，这里是红色，格式为 (B, G, R)
    # 画点
    # 参数分别是：图像、点的位置、点的半径、颜色、厚度(-1 表示填充点)
    cv2.circle(img, point_position, 5, point_color1, -1)
    logger.info(f"目标位置：{point_position[0]},{point_position[1]}")
    
    """
    ----------------------------------------------->X
    |(0,0)
    |
    |
    |                  tar_x,tar_y
    |
    |
    |
    |                                      (img_size_x,img_size_y)
    V
    Y
    """
    img_x_error = SHOW_IMG_SIZE_X/2.0 - target_x    # 正的话向左看
    img_y_error = SHOW_IMG_SIZE_Y/2.0 - target_y    # 正的话向上看
    
    target_img_x_err_filter.add_sample(img_x_error)
    target_img_y_err_filter.add_sample(img_y_error)
    #print(f"检测到最大的种类{CLASSES[classes[max_index]]:9s}, 位于X: {int(target_x):3d} - Y:{int(target_y):3d}, 误差为：X:{img_x_error:3.0f}，Y:{img_y_error:3.0f}")
    
    return fps
    
"""=====================================================================================

    云台控制部分

====================================================================================="""
def gimbal_control(stop = False):
    # 
    if stop:
        connect.send_set_velocity_message(0,0)
        return
    filtered_x_err = target_img_x_err_filter.get_value()
    filtered_y_err = target_img_y_err_filter.get_value()
    connect.send_set_velocity_message(k_yaw*filtered_x_err, -k_pitch*filtered_y_err)

def control_gimbal_t():
    # 等待rknn线程启动
    while not is_rknn_set:
        time.sleep(0.2)
    # 开启云台控制线程
    while True:
        if target_detected:
            gimbal_control()
            time.sleep(0.2)
        else:
            gimbal_control(stop=True)
    pass

def udp_server_t():
    """接收UDP消息，实现控制
    """
    # Localhost IP
    host = '127.0.0.1'
    # Port to listen on
    port = 5001

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the address and port
    server_socket.bind((host, port))

    print(f"UDP server up and listening on {port}")

    # Listen for incoming datagrams
    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Message from {address}: {data.decode()}")
        global control_mode
        control_mode = int(data.decode())
        print(f"setting mode:{MODE_DIC.get(control_mode)}")

        # Optionally, send a response back to the client
        response = "Message received"
        server_socket.sendto(response.encode(), address)

img_sender = DataTransferUDP("192.168.151.201", "192.168.151.168", 30000, 30002, "sender")        
def send_img_t():
    while True:
        try:
            if img_to_save is not None:
                re = img_sender.send_compresses_img(img_to_save)
            time.sleep(0.15)
        except:
            print("发送图片线程出现问题")
target_class_name = "laptop"
target_class_name = "backpack"
target_class_name_list = ["backpack", "laptop", "chair", "suitcase", "toilet", "bottle", "person"]
# target_class_name_list = ["chair"]
target_class_name_list = ["person"]
target_id_list = []
# for (i,c) in enumerate(CLASSES):
#     if c.startswith(target_class_name):
#         target_class_id = i
for target_class_name in target_class_name_list:
    for (i,c) in enumerate(CLASSES):
        if c.startswith(target_class_name):
            target_id_list.append(i)
print("target_id_list:")
print(target_id_list)
k_yaw = 0.19
k_pitch = 0.19
k_x = 0.03
k_y = 0.03
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='处理带有默认值的命令行参数示例')
    parser.add_argument('-nosave', action='store_true', help='不保存文件')
    parser.add_argument('--local_ip', type=str, help='本机IP', default="192.168.1.119")
    parser.add_argument('--gcs_ip', type=str, help='地面站IP', default="192.168.1.104")
    parser.add_argument('--local_port', type=int, help='本机监听端口', default=30000)
    parser.add_argument('--gcs_port', type=int, help='地面站监听端口', default=30000)
    parser.add_argument('--uav_id', type=int, help='UAV ID', default=10)
    parser.add_argument('--param1', type=int, help='备用', default=10)
    parser.add_argument('--param2', type=int, help='备用', default=10)
    parser.add_argument('--param3', type=int, help='备用', default=10)
    parser.add_argument('--param4', type=int, help='备用', default=10)

    parser1 = argparse.ArgumentParser(description='Process some integers.')
    # basic params
    # parser1.add_argument('--model_path', type=str, default="/home/cat/mac_v/pts/yolov5n224.rknn", help='model path, could be .pt or .rknn file')
    parser1.add_argument('--model_path', type=str, default="/home/cat/mac_v/pts/yolov5s.rknn", help='model path, could be .pt or .rknn file')
    parser1.add_argument('--target', type=str, default='rk3588', help='target RKNPU platform')
    parser1.add_argument('--device_id', type=str, default=None, help='device id')
    parser1.add_argument('--img_show', default=True, help='draw the result and show')
    parser1.add_argument('--img_save', action='store_true', default=True, help='save the result')
    # parser.add_argument('--anno_json', type=str, default='../../../datasets/COCO/annotations/instances_val2017.json', help='coco annotation path')
    # parser.add_argument('--img_folder', type=str, default='../model', help='img folder path')
    # parser.add_argument('--coco_map_test', action='store_true', help='enable coco map test')

    # 解析参数
    args = parser.parse_args()
    args1, unkonown_args = parser1.parse_known_args()
    # logging.basicConfig(level=logging.INFO,
    #                     filename='LOGS/new.log',
    #                     format='%(asctime)s - INFO] Control thread End')
    logger = logging.getLogger("main")
    # 启动云台线程
    if False:
        connect = A8MiniConnection()
        connect.open_listening()
        connect.send_set_pose_message(-90,-10)
    # 启动云台测试线程
    if False:
        w1 = threading.Thread(target=gimbal_test_t, args=(connect,))
        w1.start()
        connect.t.start()
    # sys.exit()
    # 启动识别线程
    # if False:
    if True:
        w2 = threading.Thread(target=rknn_t)
        w2.start()
    
    # 启动通讯线程
    # UWB
    if False:
        from handle_uwb import NoopLoopUWB
        uwb1 = NoopLoopUWB('/dev/ttyUSB1', log_ON = False)
    
    # 指令通讯
    if True:
        # from handle_mavlink import data_trans_begin
        # data_trans_begin()
        # from UavOnboard import UAVOnBoard
        # uav = UAVOnBoard()
        pass
    # 图像传输
    if True:
        from ImageTransUdp import DataTransferUDP
        # imgSender = DataTransferUDP(args.local_ip, args.gcs_ip, args.local_port, args.gcs_port, "sender")
        w3 = threading.Thread(target = send_img_t)
        w3.start()
        
    # if True:
    #     from handle_mavlink import data_fcu2gcs_t
    #     w3 = threading.Thread(target=data_fcu2gcs_t)
    #     w3.start()
    
    # if True:
    #     from handle_mavlink import data_gcs2local
    #     w31 = threading.Thread(target=data_gcs2local)
    #     w31.start()
    
    # 启动控制线程
    if True:
        w4 = threading.Thread(target=control_t)
        w4.start()
    
    # 启动云台控制线程
    if False:
        w5 = threading.Thread(target=control_gimbal_t)
        w5.start()
    
    # UDP监听命令
    if False:
        w6 = threading.Thread(target = udp_server_t)
        w6.start()
    
    # 视频保存线程
    if not args.nosave:
        print("启动保存线程")
        w7 = threading.Thread(target = video_save_t)
        w7.start()
    else:
        print("本次程序不保存视频")
