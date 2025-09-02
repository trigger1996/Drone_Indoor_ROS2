#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import yaml
import re
import matplotlib.font_manager as fm
from matplotlib import gridspec, cm
from matplotlib.colors import to_rgba, rgb_to_hsv, hsv_to_rgb
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter                                                   # TODO pip3 install bagpy, ONLY AVAILABLE FOR computers USING ROS1
from mpl_toolkits.mplot3d import Axes3D                                                                        #      sudo apt install python3-lz4, pip3 install lz4
from matplotlib.lines import Line2D
import bagpy                                                                                                   #      sudo apt install texlive texlive-font* texlive-latex-* ffmpeg | if failed， then install texlive-full
from bagpy import bagreader
import pandas as pd
import numpy as np
from rich.progress import track, Progress                                                                      # TODO pip3 install rich

# ========== 配置 ==========
#CASE_NAME = '0426_multi'
#CASE_NAME = '0506_single_opaque'
CASE_NAME = '0506_single_non_opaque'
if CASE_NAME == '0426_multi':
    bag_file  = "/home/droneyee/zt_ws/bags/0426_multi_real/2025-08-23-04-26-40.bag"   				    # TODO: 替换为你的bag文件
    yaml_file = "/home/droneyee/zt_ws/src/drone_ros_centeralized_control/map/mdp_planner/yaml/20250426_map_w_edges.yaml"
    # bag_file  = "/home/ghost/ws_droneyee/bags/0426_multi_real/2025-08-23-04-26-40.bag"
    # yaml_file = "/home/ghost/ws_droneyee/src/drone_ros_centeralized_control/map/mdp_planner/yaml/20250426_map_w_edges.yaml"
if CASE_NAME == '0506_single_opaque':
    # opaque
    bag_file  = "/home/droneyee/zt_ws/bags/0506_single_real/[group_1_opaque]2025-08-23-01-03-30.bag"
    yaml_file = '/home/droneyee/zt_ws/src/drone_ros_centeralized_control/map/mdp_planner/yaml/20250506_map_w_edges.yaml'
    # bag_file  = "/home/ghost/ws_droneyee/bags/0506_single_real/[group_1_opaque]2025-08-23-01-03-30.bag"
    # yaml_file = "/home/ghost/ws_droneyee/src/drone_ros_centeralized_control/map/mdp_planner/yaml/20250506_map_w_edges.yaml"
if CASE_NAME == '0506_single_non_opaque':
    # non-opaque
    bag_file  = "/home/droneyee/zt_ws/bags/0506_single_real/[group_1_nonopaque]2025-08-23-00-46-31.bag"
    yaml_file = '/home/droneyee/zt_ws/src/drone_ros_centeralized_control/map/mdp_planner/yaml/20250506_map_w_edges.yaml'
    # bag_file  = "/home/ghost/ws_droneyee/bags/0506_single_real/2025-08-23-04-26-40.bag"
    # yaml_file = "/home/ghost/ws_droneyee/src/drone_ros_centeralized_control/map/mdp_planner/yaml/20250506_map_w_edges.yaml"
#
save_file = "uav_animation.mp4"
#
markers = ["s", "v", "D", "*", "+", "x", "s", "^", "o"]
uav_colors = [(219, 114, 118), (80, 103, 237), (241, 105, 187), (185, 251, 96), (35, 220, 197), (162, 224, 31), (9, 247, 9)]
uav_colors = [tuple(float(x) / 255 for x in color) for color in uav_colors]
#
uav_edge_color = [float(c) / 255 for c in [195, 44, 247]]
#
# 0426 multi
#
if CASE_NAME == '0426_multi':
    optimal_run = """'('0', '5')' '(('b',), ('b',))' '('2', '6')' '(('a',), ('a',))' '('3', '4')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('0', '2')' '(('b',), ('a',))' '('2', '3')' '(('a',), ('b',))' '('3', '0')' '(('b',), ('b',))' '('4', '3')' '(('a',), ('b',))' '('5', '4')' '(('b',), ('a',))' '('6', '3')' '(('b',), ('b',))' '('6', '0')' '(('a',), ('a',))' '('4', '1')' '(('b',), ('a',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')' '(('b',), ('b',))' '('2', '0')' '(('a',), ('b',))' '('3', '2')' '(('b',), ('a',))' '('0', '3')'"""
    waypt_time = { 'start'         : (1755894402.605441, 1755894403.623602),
                   'takeoff_comp'  : (1755894408.624205, 1755894408.397962),
                   'mission_start' : (1755894414.324091, 1755894420.897865),
                   'waypts' : [[1755894414.326147, 1755894424.724148, 1755894435.424167, 1755894448.024158, 1755894461.224113, 1755894471.024157, 1755894477.724170, 1755894490.224121, 1755894499.824163, 1755894508.824120, 1755894521.624237, 1755894533.924196, 1755894554.324164, 1755894565.024187, 1755894576.824165, 1755894576.924166, 1755894584.924181, 1755894591.324185, 1755894597.724246, 1755894605.224140, 1755894618.024156, 1755894630.224134],
                               [1755894420.899955, 1755894433.897894, 1755894442.697838, 1755894450.997849, 1755894458.797859, 1755894468.697840, 1755894480.997858, 1755894489.997795, 1755894500.897948, 1755894511.398056, 1755894522.197844, 1755894532.797759, 1755894542.797868, 1755894554.497933, 1755894564.597862, 1755894574.197863, 1755894587.797833, 1755894603.297947, 1755894620.097832, 1755894628.997824, 1755894638.897993, 1755894654.897213]]}

    ap_color_mapping = { "{'gather'}"   : [(250, 135, 119),  (5,   120, 136)],
                         "{'upload'}"   : [(169, 86,  176),  (86,  169, 79)],
                         "{'recharge'}" : [(46,  175, 255),  (209, 80,  0)],
                         "{''}"         : [(213, 230, 102),  (42,  25,  153)], }  # 0426                                                                                                                        # 0426

if CASE_NAME == '0506_single_opaque':
    optimal_run = """'19', '('l',)', '18', '('l',)', '17', '('u',)', '12', '('d',)', '17', '('r',)', '18', '('l',)', '12', '('d',)', '17', '('r',)', '18', '('r',)', '19', '('u',)', '14', '('d',)', '19', '('d',)', '24', '('u',)', '19', '('d',)', '24', '('u',)', '19', '('u',)', '14', '('d',)', '19', '('d',)', '24', '('l',)', '18', '('l',)', '12', '('d',)', '17', '('r',)', '18', '('l',)', '17', '('u',)', '12', '('d',)', '17', '('r',)', '18', '('r',)', '19'"""
    waypt_time = {'start'         : (1755882215.399430, ),
                  'mission_start' : (1755882217.999386, )}

if CASE_NAME == '0506_single_non_opaque':
    optimal_run = """"'19' '('l',)' '18' '('u',)' '13' '('r',)' '14' '('d',)' '19' '('l',)' '18' '('u',)' '13' '('d',)' '18' '('r',)' '19' '('d',)' '24' '('l',)' '18' '('u',)' '13' '('u',)' '8' '('u',)' '3' '('d',)' '8' '('d',)' '13' '('u',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('u',)' '3' '('l',)' '2' '('r',)' '3' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('d',)' '12' '('l',)' '11' '('l',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21'"""      # TODO
    waypt_time = {'start':         (1755881198.227331,),        # TODO need to check csv if use the other bags
                  'mission_start': (1755881200.9272728,)}

# 0506 single
if CASE_NAME == '0506_single_opaque' or CASE_NAME == '0506_single_non_opaque':
    ap_color_mapping = {"{'gather'}"     : [(213, 230, 102), (42, 25, 153)],
                        "{'upload'}"     : [(169, 86, 176), (86, 169, 79)],
                        "{'recharge'}"   : [(46,  175, 255), (209, 80, 0)],
                        "{'investigate'}": [(165, 115, 73), (236, 199, 110)],
                        "{''}"           : [(250, 135, 119), (5, 120, 136)], }  # 0426

ap_color_mapping = {
    key: [tuple(map(lambda x: float(x) / 255, color)) for color in value]
    for key, value in ap_color_mapping.items()
}
#
fps       = 30
figsize   = (16, 9)   # 宽高比 16:9
init_elev = 22.5      # 初始仰角
init_azim = 57.5      # 初始方位角

# 控制开关
SAVE_VIDEO = True      # 是否保存 mp4
SHOW_VIDEO = True      # 是否播放动画窗口

# 坐标轴设置
IS_INVERT_X_AXIS = True
IS_INVERT_Y_AXIS = True      # north相反, 和拍摄方向一致
SYMMETRIC_AXES = True        # 是否使用对称坐标轴
AXIS_PADDING = 0.5           # 坐标轴边距（米）

# 字体大小配置
UAV_SIZE   = 15               # 单位不同
WAYPT_SIZE = 350              # 单位不同
FONT_SIZE_LABEL = 26
FONT_SIZE_WAYPT = 22
FONT_SIZE_TICK = 18
FONT_SIZE_TITLE = 32
FONT_SIZE_LEGEND = 18
WAYPT_DISPLAY_DURATION = 10.5 # 已到达路点淡出, 显示10秒
#
COST_MULTIPLIERS = 1.

if CASE_NAME == '0426_multi':
    #
    FONT_SIZE_WAYPT = 22
    #
    COST_MULTIPLIERS = 3.5
    #
    IS_WAIT_UNTIL_TIME_EXCEEDED = True
    WAYPT_RADIUS = 0.225
if CASE_NAME == '0506_single_opaque' or CASE_NAME == '0506_single_non_opaque':
    #
    FONT_SIZE_WAYPT = 14
    #
    COST_MULTIPLIERS = 6.5
    #
    IS_WAIT_UNTIL_TIME_EXCEEDED = False
    WAYPT_RADIUS = 0.275

# 0506 single

# 使用 Euclid 字体
plt.rcParams.update({
    "text.usetex" : True,
    "font.family" : "Euclid"
})

# ========== 坐标变换函数 ==========
def transform_coords(x, y, z, source="ENU", target="NEU"):
    """
    通用坐标系转换函数
    支持 ENU, NEU, NED 之间的转换

    Args:
        x, y, z: float
            输入坐标
        source: str
            输入坐标系 ("ENU", "NEU", "NED")
        target: str
            输出坐标系 ("ENU", "NEU", "NED")

    Returns:
        (x_new, y_new, z_new): tuple
            转换后的坐标
    """
    if source == target:
        return x, y, z

    # 统一转成 ENU
    if source == "NEU":
        x, y, z = y, x, z
    elif source == "NED":
        x, y, z = y, x, -z

    # 再从 ENU 转到目标系
    if target == "NEU":
        return y, x, z
    elif target == "NED":
        return y, x, -z
    elif target == "ENU":
        return x, y, z
    else:
        raise ValueError(f"Unknown target frame: {target}")


def rotate_vector(x, y, z, angle_deg=0):
    """
    在水平面旋转向量 (ENU->NEU 后的结果)，方便后续调整
    angle_deg: 绕 Z 轴旋转角度（度）
    """
    theta = np.radians(angle_deg)
    c, s = np.cos(theta), np.sin(theta)
    x_new = c*x - s*y
    y_new = s*x + c*y
    return x_new, y_new, z

def rotate_data_axis_custom(x, y, z):
    #
    # return -y, -x, z          # 这个用plt.gca().invert_xaxis()和plt.gca().invert_yaxis()实现
    return y, x, z

def calculate_axis_limits(pose_data, waypoints, padding=AXIS_PADDING, symmetric=True):
    """
    计算所有数据的坐标轴范围

    Returns:
        x_lim, y_lim, z_lim: 每个轴的(min, max)范围
    """
    # 初始化极值
    all_x, all_y, all_z = [], [], []

    # 收集所有无人机的位置数据
    for uid, df in pose_data.items():
        # 转换坐标系
        x_coords = []
        y_coords = []
        z_coords = []

        for _, row in df.iterrows():
            x, y, z = transform_coords(row['pose.position.x'],
                                       row['pose.position.y'],
                                       row['pose.position.z'])
            x, y, z = rotate_data_axis_custom(x, y, z)
            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)

        all_x.extend(x_coords)
        all_y.extend(y_coords)
        all_z.extend(z_coords)

    # 收集地图路点数据
    for node_id, node_info in waypoints.items():
        Xned, Yned, Z, yaw = node_info["pos"]
        Xned, Yned, Z = rotate_data_axis_custom(Xned, Yned, Z)
        all_x.append(Xned)
        all_y.append(Yned)
        all_z.append(Z)

    # 转换为numpy数组
    all_x = np.array(all_x)
    all_y = np.array(all_y)
    all_z = np.array(all_z)

    if symmetric:
        # 对称坐标轴范围
        x_range = max(np.abs(all_x).max(), padding)
        y_range = max(np.abs(all_y).max(), padding)
        z_range = max(np.abs(all_z).max(), padding)

        x_lim = (-x_range - padding, x_range + padding)
        y_lim = (-y_range - padding, y_range + padding)
        # z_lim = (0, 2 * z_range + padding)  # Z轴通常从0开始
    else:
        # 非对称坐标轴范围
        x_lim = (all_x.min() - padding, all_x.max() + padding)
        y_lim = (all_y.min() - padding, all_y.max() + padding)
    z_lim = (max(0, all_z.min() - padding), all_z.max() + padding)              # Added, z不用对称

    print(f"X轴范围: {x_lim}")
    print(f"Y轴范围: {y_lim}")
    print(f"Z轴范围: {z_lim}")

    return x_lim, y_lim, z_lim

# ========== 读取地图 ==========
with open(yaml_file, "r") as f:
    data = yaml.load(f, Loader=yaml.UnsafeLoader)

waypoints = data["waypoint"]
edges = data["edges"]

# ========== 读取 rosbag ==========
b = bagreader(bag_file)
topics = b.topic_table["Topics"].tolist()

# 自动检测真正存在的无人机（只要有 pose topic 就算）
pose_topics = [t for t in topics if "/vrpn_client_node/droneyee" in t and "/pose" in t]

# 提取无人机真实 ID
active_uav_ids = sorted(int(t.split("droneyee")[-1].split("/")[0]) for t in pose_topics)

# 建立映射：原始ID -> 连续显示ID (1,2,3,...)
id_map = {uid: i+1 for i, uid in enumerate(active_uav_ids)}

pose_data, odom_data, cmd_data = {}, {}, {}

for uid in active_uav_ids:
    try:
        pose_csv = b.message_by_topic(f"/vrpn_client_node/droneyee{uid}/pose")
        pose_data[uid] = pd.read_csv(pose_csv)
    except Exception:
        print(f"[WARN] No pose data for drone {uid}, skipping ...")
        continue

    try:
        odom_csv = b.message_by_topic(f"/mavrouter/drone_pose_{uid}")
        odom_data[uid] = pd.read_csv(odom_csv)
    except Exception:
        odom_data[uid] = None

    try:
        cmd_csv = b.message_by_topic(f"/cmd_vel_{uid}")
        cmd_data[uid] = pd.read_csv(cmd_csv)
    except Exception:
        cmd_data[uid] = None

def calculate_max_speed(pose_data, odom_data, fps=30):
    """
    计算所有无人机的最大速度

    Args:
        pose_data: dict
            各无人机的位姿数据
        odom_data: dict
            各无人机的里程计数据
        fps: int
            帧率，用于计算每帧的速度

    Returns:
        max_speed: float
            所有无人机的最大速度
    """
    max_speed = 0.
    max_speed_2d = 0.

    # 遍历每架无人机
    for uid in pose_data:
        odom = odom_data.get(uid)
        if odom is None:
            continue  # 如果没有里程计数据，跳过

        # 计算无人机的速度
        velocities = []
        velocities_2d = []
        for t in range(len(odom)):
            # 只取线速度
            vx = odom.iloc[t]['twist.twist.linear.x']
            vy = odom.iloc[t]['twist.twist.linear.y']
            vz = odom.iloc[t]['twist.twist.linear.z']

            # 计算速度的大小
            speed = np.sqrt(vx**2 + vy**2 + vz**2)
            speed_2d = np.sqrt(vx**2 + vy**2)
            velocities.append(speed)
            velocities_2d.append(speed_2d)


        # 获取当前 UAV 的最大速度
        max_uav_speed = max(velocities)
        max_uav_speed_2d = max(velocities_2d)
        max_speed = max(max_speed, max_uav_speed)  # 更新全局最大速度
        max_speed_2d = max(max_speed_2d, max_uav_speed_2d)

    return max_speed, max_speed_2d

# 只保留真正有pose数据的无人机
active_uav_ids = [uid for uid in active_uav_ids if uid in pose_data]

if not active_uav_ids:
    raise RuntimeError("❌ 没有检测到任何无人机的 pose 数据！")

def extract_states_from_x_u_lists(x_u_list):
    # for example : ""'15' '('u',)' '10' '('u',)' '5' '('r',)' '6' '('d',)' '11' '('r',)' '12' '('l',)' '11' '('r',)' '12' '('l',)' '11' '('d',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('r',)' '17' '('l',)' '16' '('u',)' '11' '('d',)' '16' '('l',)' '15' '('d',)' '20' '('u',)' '15' '('d',)' '20' '('u',)' '15' '('r',)' '16' '('r',)' '17' '('l',)' '16' '('d',)' '21' '('l',)' '20' '('u',)' '15' '('d',)' '20' '('r',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('u',)' '1' '('d',)' '6' '('l',)' '5' '('u',)' '0' '('r',)' '1' '('d',)' '6' '('l',)' '5' '('d',)' '10' '('r',)' '11' '('d',)' '16' '('l',)' '15' '('u',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('d',)' '21' '('r',)' '17' '('l',)' '16' '('r',)' '17' '('u',)' '12' '('u',)' '7' '('u',)' '2' '('l',)' '1' '('r',)' '2' '('l',)' '1' '('l',)' '0' '('r',)' '1' '('d',)' '6' '('r',)' '7' '('l',)' '6' '('u',)' '1' '('d',)' '6' '('r',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('l',)' '7' '('d',)' '12' '('r',)' '13' '('r',)' '14' '('l',)' '13' '('u',)' '8' '('u',)' '3' '('l',)' '2' '('l',)' '1' '('l',)' '0' '('d',)' '5' '('d',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('r',)' '17' '('r',)' '18' '('u',)' '13' '('r',)' '14' '('l',)' '13' '('d',)' '18' '('u',)' '13' '('u',)' '8' '('u',)' '3' '('d',)' '8' '('d',)' '13' '('l',)' '12' '('u',)' '7' '('u',)' '2' '('d',)' '7' '('r',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('l',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('u',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('l',)' '2' '('d',)' '7' '('d',)' '12' '('u',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('d',)' '13' '('d',)' '18' '('r',)' '19' '('u',)' '14' '('l',)' '13' '('r',)' '14'"""

    # 如果输入是 bytes，就解码为 str
    if isinstance(x_u_list, bytes):
        x_u_list = x_u_list.decode('utf-8')

    return re.findall(r"'(\d+)'", x_u_list)

def extract_states_from_joint_x_u_lists(x_u_list_str, num_drones=None):
    """
    输入:
        x_u_list_str: 含联合轨迹的字符串，例如:
            "('0','5','2') (('a',),('a',),('a',)) ('1','4','3') ..."
        num_drones: 无人机数量（可选，推荐传入）
    输出:
        list of list，每个子 list 是一个无人机的完整轨迹
        例如:
            [[0, 1, 0],   # 第1架无人机
             [5, 4, 3],   # 第2架无人机
             [2, 3, 0]]   # 第3架无人机
    """

    if isinstance(x_u_list_str, bytes):
        x_u_list_str = x_u_list_str.decode('utf-8')

    # 提取所有数字
    numbers = re.findall(r"'(\d+)'", x_u_list_str)

    if not numbers:
        return []

    # 转换为整数
    numbers = [int(n) for n in numbers]

    # 自动推测无人机数量
    if num_drones is None:
        for n in range(1, 10):  # 最多支持10架
            if len(numbers) % n == 0:
                num_drones = n
                break
        else:
            raise ValueError("无法自动推测无人机数量，请手动传入 num_drones")

    # 总步数
    steps = len(numbers) // num_drones

    # 重新分配给每个无人机
    drone_trajs = [[] for _ in range(num_drones)]
    for i in range(steps):
        for d in range(num_drones):
            drone_trajs[d].append(numbers[i * num_drones + d])

    return drone_trajs

# ========== 预先计算坐标轴范围 ==========
x_lim, y_lim, z_lim = calculate_axis_limits(pose_data, waypoints,
                                           padding=AXIS_PADDING,
                                           symmetric=SYMMETRIC_AXES)
v_xyz_lim, v_xy_lim = calculate_max_speed(pose_data, odom_data, fps=fps)

# ========== 时间对齐 ==========
t_min = min(df['Time'].min() for df in pose_data.values())
t_max = max(df['Time'].max() for df in pose_data.values())
duration = t_max - t_min
nframes = int(duration * fps)

# ========== 绘图准备 ==========
fig = plt.figure(figsize=figsize)
gs = gridspec.GridSpec(1, 2, width_ratios=[1.65,1], wspace=0.25)  # 调整间距和大小
ax3d = fig.add_subplot(gs[0], projection="3d")
ax2d = fig.add_subplot(gs[1])

# 设置初始 3D 视角
ax3d.view_init(elev=init_elev, azim=init_azim)

# 设置坐标轴范围
ax3d.set_xlim(x_lim)
ax3d.set_ylim(y_lim)
ax3d.set_zlim(z_lim)
ax2d.set_xlim(x_lim)
ax2d.set_ylim(y_lim)
#
# ax3d.set_xlim(ax3d.get_xlim()[::-1])
# ax3d.set_ylim(ax3d.get_ylim()[::-1])
# ax2d.invert_xaxis()
if IS_INVERT_Y_AXIS:
    ax2d.invert_yaxis()
if IS_INVERT_X_AXIS:
    ax2d.invert_xaxis()

def draw_map(ax3d, ax2d):
    for node_id, node_info in waypoints.items():
        # x_enu, y_enu, z, yaw = node_info["pos"]
        ap = node_info["ap"][0]
        ap_2_display = r"$\{" + re.sub(r"^\{['\"](.*)['\"]\}$", r"\1", ap) + r"\}$"  # 去掉单引号和双引号  # 去掉单引号和双引号
        # Xned, Yned, Z = transform_coords(x_enu, y_enu, z)
        Xned, Yned, Z, yaw = node_info["pos"]                       # TODO modify yaw if in need
        Z = 0.75                                                    # force set Z

        # Added
        # 坐标轴x, y旋转
        Xned, Yned, Z  = rotate_data_axis_custom(Xned, Yned, Z)

        if ap in ap_color_mapping.keys():
            center_color = ap_color_mapping[ap][0]
            edge_color   = ap_color_mapping[ap][1]
        else:
            center_color = [ float(c) / 255 for c in [147, 224, 255] ]
            edge_color   = [ float(c) / 255 for c in [38,  157, 128] ]

        ax3d.scatter(Xned, Yned, Z, c=center_color,  edgecolors=edge_color, s=WAYPT_SIZE, linewidths=1.5, alpha=0.85)
        ax3d.text(Xned, Yned, Z, f"{node_id}\n{ap_2_display}", fontsize=FONT_SIZE_WAYPT, zorder=200)
        ax2d.scatter(Xned, Yned, c=center_color,     edgecolors=edge_color, s=WAYPT_SIZE, linewidths=1.5, alpha=0.85)
        ax2d.text(Xned, Yned, f"{node_id}\n{ap_2_display}",    fontsize=FONT_SIZE_WAYPT, zorder=200)

    for edge in edges:
        src, dst, attr = edge
        x1, y1, z1, _ = waypoints[src]["pos"]
        x2, y2, z2, _ = waypoints[dst]["pos"]
        # X1, Y1, Z1 = transform_coords(x1, y1, z1)
        # X2, Y2, Z2 = transform_coords(x2, y2, z2)
        X1, Y1, Z1 = x1, y1, z1
        X2, Y2, Z2 = x2, y2, z2

        Z1 = Z2 = 0.75  # force set Z

        # Added
        # 坐标轴x, y旋转
        X1, Y1, Z1  = rotate_data_axis_custom(X1, Y1, Z1)
        X2, Y2, Z2  = rotate_data_axis_custom(X2, Y2, Z2)

        ax3d.plot([X1, X2], [Y1, Y2], [Z1, Z2], "gray", alpha=0.5, linewidth=3.25)
        ax2d.plot([X1, X2], [Y1, Y2], "gray", alpha=0.5, linewidth=3.25)

    ax3d.set_xlabel("$y$ (East)  /$m$",     fontsize=FONT_SIZE_LABEL, labelpad=15)            # "North [m]"       这是为了和实验室以及拍摄的电脑方向一致
    ax3d.set_ylabel("$x$ (North) /$m$",     fontsize=FONT_SIZE_LABEL, labelpad=15)            # "East [m]"
    ax3d.set_zlabel("$z$ (Altitude) /$m$",  fontsize=FONT_SIZE_LABEL, labelpad=15)
    ax2d.set_xlabel("$y$ (East)  /$m$",     fontsize=FONT_SIZE_LABEL, labelpad=7.5)                 # "North [m]"
    ax2d.set_ylabel("$x$ (North) /$m$",     fontsize=FONT_SIZE_LABEL, labelpad=7.5)                 # "East [m]"
    ax3d.set_title("3D Trajectory",         fontsize=FONT_SIZE_TITLE, pad=22)
    ax2d.set_title("Horizontal Projection", fontsize=FONT_SIZE_TITLE, pad=22)

    # 添加刻度标签字体大小设置
    ax3d.tick_params(axis='x', labelsize=FONT_SIZE_TICK)
    ax3d.tick_params(axis='y', labelsize=FONT_SIZE_TICK)
    ax3d.tick_params(axis='z', labelsize=FONT_SIZE_TICK)
    ax2d.tick_params(axis='x', labelsize=FONT_SIZE_TICK)
    ax2d.tick_params(axis='y', labelsize=FONT_SIZE_TICK)

draw_map(ax3d, ax2d)

#
# "o" - 圆形    "s" - 正方形   "^" - 正三角形  "v" - 倒三角形  "D" - 菱形    "*" - 星形    "+" - 加号    "x" - 叉号
uav_markers = {}
for i, uid in enumerate(active_uav_ids):
    disp_id = id_map[uid]
    uav_markers[uid] = {
        "pos3d": ax3d.plot([], [], [], markers[i % len(markers)], markersize=UAV_SIZE, markeredgewidth=2.5, color=uav_colors[i % len(uav_colors)], markeredgecolor=uav_edge_color, label=f"UAV {disp_id}")[0],
        "vel3d": ax3d.quiver(0,0,0,0,0,0,length=0.5,color="red"),
        "cmd3d": ax3d.quiver(0,0,0,0,0,0,length=0.5,color="black"),
        "pos2d": ax2d.plot([], [], markers[i % len(markers)], markersize=UAV_SIZE, markeredgewidth=2.5, color=uav_colors[i % len(uav_colors)], markeredgecolor=uav_edge_color, label=f"UAV {disp_id}")[0],
        "vel2d": ax2d.quiver(0,0,0,0,color="red"),
        "cmd2d": ax2d.quiver(0,0,0,0,color="black"),
    }

#
# 'upper right'：图例位于右上角   'lower left'：图例位于左下角    'lower right'：图例位于右下角   'center'：图例位于图形的中央  'center left'：图例位于左侧居中  'center right'：图例位于右侧居中 'upper center'：图例位于上方居中 'lower center'：图例位于下方居中
# 0：'best'，自动选择最佳位置   1：'upper right' 2：'upper left'  3：'lower left'  4：'lower right' 5：'center left' 6：'center right'    7：'lower center'    8：'upper center'    9：'center'
ax3d.legend(fontsize=FONT_SIZE_LEGEND, loc=0)            # 共用即可
#ax2d.legend(fontsize=FONT_SIZE_LEGEND)

# ========== 动画准备函数 ==========
def interpolate(df, t):
    if df is None or t < df['Time'].min() or t > df['Time'].max():
        return None
    return df.iloc[(df['Time']-t).abs().argmin()]

def get_edge_info(edges_list, id_last, id_curr):
    """在 edges_list 中查找从 id_last 到 id_curr 的边信息"""
    for edge in edges_list:
        if edge[0] == str(id_last) and edge[1] == str(id_curr):
            return edge[2]  # 返回属性字典
    raise ValueError(f"No edge from {id_last} to {id_curr} in map...")

# ========== 动画函数 ==========
#
#
# 在全局定义真实的时间戳列表
# 使用真实的时间戳可以保证动画与数据的时间对齐。我来修改代码，使用真实的时间值，同时保持fps尽量接近设定值。
real_timestamps = {}
for uid in active_uav_ids:
    uav_data = pose_data[uid]
    real_timestamps[uid] = uav_data["Time"]

# 找到所有无人机的共同时间范围
all_times = []
for uid in active_uav_ids:
    all_times.extend(real_timestamps[uid])

min_time = min(all_times)
max_time = max(all_times)
total_duration = max_time - min_time

# 计算总帧数，保持fps接近设定值
total_frames = int(total_duration * fps)

# 为每一帧预先计算对应的时间戳
frame_times = []
for frame in range(total_frames):
    # 计算该帧对应的归一化时间位置 (0到1之间)
    normalized_time = frame / total_frames
    # 映射到真实的时间范围
    target_time = min_time + normalized_time * total_duration
    #target_time = normalized_time * total_duration
    frame_times.append(target_time)

#
# 初始化全局变量用于存储参考轨迹和到达点
team_run = extract_states_from_joint_x_u_lists(optimal_run, num_drones=len(active_uav_ids))
waypt_index  = [0 for ui in range(0, len(active_uav_ids))]          # 当前完成的路径的个数
waypt_to_add = [[] for ui in range(0, len(active_uav_ids))]         # 已完成
waypt_arrived_time = [[] for _ in range(len(active_uav_ids))]      # 每个无人机一个时间戳列表, 用于后续淡出显示
ref_lines_3d = []                                                   # 画图变量
ref_lines_2d = []
arrived_waypts_3d = []
arrived_waypts_2d = []

# 需要在全局定义 accumulated_time_list
accumulated_time_list = []
for ui, uid in enumerate(active_uav_ids):
    acc_time = [0.0]
    for i in range(1, len(team_run[ui])):
        id_last = team_run[ui][i - 1]
        id_curr = team_run[ui][i]

        if CASE_NAME == '0426_multi':
            #
            edge_info = get_edge_info(edges, id_last, id_curr)
            cost_t = edge_info['weight'] * COST_MULTIPLIERS
        if CASE_NAME == '0506_single_opaque' or CASE_NAME == '0506_single_non_opaque':
            #
            pos_last = waypoints[str(team_run[ui][id_last])]["pos"]
            pos_now  = waypoints[str(team_run[ui][id_curr])]["pos"]

            dx = pos_now[0] - pos_last[0]
            dy = pos_now[1] - pos_last[1]
            dz = pos_now[2] - pos_last[2]

            cost_t = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2) * COST_MULTIPLIERS
        acc_time.append(acc_time[-1] + cost_t)
    accumulated_time_list.append(acc_time)

def check_arrived_waypts(frame):
    global waypt_index, waypt_to_add, waypt_arrived_time
    for ui, uid in enumerate(active_uav_ids):
        uav_data = pose_data[uid]
        times = uav_data["Time"]
        x, y, z = [], [], []

        # 通过时间点绘制轨迹
        # 这里用的t是绝对时间单位不一样, 算了不管他了
        t = frame_times[frame]
        if t < waypt_time['mission_start'][ui]:
            continue

        pose = interpolate(uav_data, t)
        if pose is not None:
            X, Y, Z = transform_coords(pose['pose.position.x'], pose['pose.position.y'], pose['pose.position.z'])
            X, Y, Z = rotate_data_axis_custom(X, Y, Z)
            x.append(X)
            y.append(Y)
            z.append(Z)

            # Added
            # 计算当前位置是否到达目标
            target = waypoints[str(team_run[ui][waypt_index[ui]])]["pos"]
            target = transform_coords(target[0], target[1], target[2])
            err_x = target[0] - X
            err_y = target[1] - Y
            err_z = target[2] - Z
            dist = math.sqrt(err_x ** 2 + err_y ** 2)
            #
            # Decision
            should_switch_waypoint = False

            limited_time = waypt_time['mission_start'][ui] + accumulated_time_list[ui][waypt_index[ui]]

            is_exceed_current_time = t > limited_time  # current_time > limited_time + self.task_start_instant

            if IS_WAIT_UNTIL_TIME_EXCEEDED:
                # 要等到时间到了再换点
                if dist < WAYPT_RADIUS and is_exceed_current_time:
                    should_switch_waypoint = True
            else:
                # 提前到达或时间到了都可以换点
                if dist < WAYPT_RADIUS or is_exceed_current_time:
                    should_switch_waypoint = True

            if should_switch_waypoint == True:
                if waypt_index[ui] < len(team_run[ui]) - 1:
                    print(f"UAV {ui + 1} reached waypoint {team_run[ui][waypt_index[ui]]} | {waypt_index[ui]} / {len(team_run[ui])} at time {t:.2f}s")

                    waypt_index[ui] += 1
                    # 记录路点坐标和到达时间
                    waypt_to_add[ui].append((X, Y, Z))
                    waypt_arrived_time[ui].append(t)  # 记录当前时间戳

def plot_traj_and_vel_vectors(frame):
    # 处理零向量
    def is_valid_vector(u, v, w):
        """检查向量是否有效"""
        return (not np.isnan(u) and not np.isnan(v) and not np.isnan(w) and
                not np.isinf(u) and not np.isinf(v) and not np.isinf(w))

    def adjust_color_saturation(base_color, factor):
        """根据给定的因子调整颜色的饱和度"""
        # 如果 base_color 只有 3 个元素（RGB），就添加 alpha 通道，默认 alpha 为 1.0（完全不透明）
        if len(base_color) == 3:
            base_color = np.append(base_color, 1.0)  # 添加 alpha 通道

        # H, S, V 是颜色的色调、饱和度和明度
        h, s, v = rgb_to_hsv(base_color[:3])  # 解包为3个值
        a = base_color[3]  # alpha 通道

        # 调整饱和度
        s = np.clip(s * factor, 0, 1)

        # 将新的饱和度应用回 RGB 中
        new_color = hsv_to_rgb([h, s, v])

        return to_rgba((new_color[0], new_color[1], new_color[2], a))

    def safe_quiver_3d(ax, x, y, z, u, v, w, base_color=to_rgba("blue")[:3], **kwargs):
        """安全的3D箭头绘制，避免零向量"""
        global v_xyz_lim
        if not is_valid_vector(u, v, w):
            u, v, w = 0, 0, 0  # 如果无效，设为零向量

        magnitude = np.sqrt(u ** 2 + v ** 2 + w ** 2)
        # 渐变色
        saturation_factor = np.clip(magnitude / v_xyz_lim, 0.5, 1.0)  # 根据大小调整饱和度
        color = adjust_color_saturation(base_color, saturation_factor)  # 调整颜色饱和度

        if magnitude < 1e-6:  # 接近零的向量
            # 不绘制箭头或者绘制一个很小的点
            return ax.quiver(x, y, z, 0, 0, 1e-6, color=color, **kwargs)
        else:
            return ax.quiver(x, y, z, u, v, w, color=color, **kwargs)

    def safe_quiver_2d(ax, x, y, u, v, base_color='blue', **kwargs):
        """安全的2D箭头绘制，避免零向量"""
        global v_xy_lim
        if not is_valid_vector(u, v, 0):  # w -> no need
            u, v = 0, 0  # 如果无效，设为零向量

        magnitude = np.sqrt(u ** 2 + v ** 2)
        # 渐变色
        saturation_factor = np.clip(magnitude / v_xy_lim, 0.5, 1.0)  # 根据大小调整饱和度
        color = adjust_color_saturation(base_color, saturation_factor)  # 调整颜色饱和度

        if magnitude < 1e-6:  # 接近零的向量
            # 不绘制箭头或者绘制一个很小的点
            return ax.quiver(x, y, 1e-6, 1e-6, color=color, **kwargs)
        else:
            return ax.quiver(x, y, u, v, color=color, **kwargs)

    def add_arrow_legend(ax):
        """为3D和2D箭头添加legend"""
        # 创建一个Line2D对象作为箭头的代表（使用一个假的箭头）
        arrow_legend = Line2D([0], [0], color='red', marker='>', markersize=10, label="Velocity (Arrow)")
        cmd_legend = Line2D([0], [0], color='green', marker='>', markersize=10, label="Command (Arrow)")

        # 返回箭头的图例条目
        return [arrow_legend, cmd_legend]

    legend_entries = []

    #t = t_min + frame / fps
    t = frame_times[frame]
    #
    for uid in active_uav_ids:
        pose = interpolate(pose_data[uid], t)
        odom = interpolate(odom_data.get(uid), t) if odom_data.get(uid) is not None else None
        cmd  = interpolate(cmd_data.get(uid), t) if cmd_data.get(uid) is not None else None
        if pose is None:
            continue

        X, Y, Z = transform_coords(pose['pose.position.x'], pose['pose.position.y'], pose['pose.position.z'])           # ENU -> NEU
        vx, vy, vz = (odom['twist.twist.linear.x'], odom['twist.twist.linear.y'], odom['twist.twist.linear.z']) if odom is not None else (0,0,0)
        cx, cy, cz = (cmd['linear.x'], cmd['linear.y'], cmd['linear.z']) if cmd is not None else (0,0,0)

        # ENU -> NED
        vx, vy, vz = rotate_vector(vx, vy, vz, angle_deg=0)   # 应用旋转函数
        cx, cy, cz = rotate_vector(cx, cy, cz, angle_deg=0)
        vz = -vz
        cz = -cz
        # 坐标轴x, y旋转
        X,  Y,  Z  = rotate_data_axis_custom(X,  Y,  Z)
        vx, vy, vz = rotate_data_axis_custom(vx, vy, vz)
        cx, cy, cz = rotate_data_axis_custom(cx, cy, cz)

        # 3D
        uav_markers[uid]["pos3d"].set_data([X], [Y])
        uav_markers[uid]["pos3d"].set_3d_properties([Z])
        uav_markers[uid]["vel3d"].remove()
        # uav_markers[uid]["vel3d"] = ax3d.quiver(X, Y, Z, vx, vy, vz, length=1.5, color="red")
        uav_markers[uid]["vel3d"] = safe_quiver_3d(ax3d, X, Y, Z, vx, vy, vz, base_color=to_rgba("red")[:3], length=0.95, linewidth=3.25, zorder=9)        # TODO
        uav_markers[uid]["cmd3d"].remove()
        # uav_markers[uid]["cmd3d"] = ax3d.quiver(X, Y, Z, cx, cy, cz, length=1.5, color="green")
        uav_markers[uid]["cmd3d"] = safe_quiver_3d(ax3d, X, Y, Z, cx, cy, cz, base_color=to_rgba("green")[:3], length=0.95, linewidth=3.25, zorder=9)

        # 2D
        # Added
        #
        # # TODO, CTIRICAL 由于之前的y轴旋转不会带动箭头的y旋转, 只有2D才有
        if IS_INVERT_Y_AXIS:
            vy_2d = -vy                                    # 现在还是NED, 转x, 如果rotate_data_axis_custom先运行就要转y
            cy_2d = -cy
        else:
            vy_2d = vy
            cy_2d = cy
        if IS_INVERT_X_AXIS:
            vx_2d = -vx  # 现在还是NED, 转x, 如果rotate_data_axis_custom先运行就要转y
            cx_2d = -cx
        else:
            vx_2d = vx
            cx_2d = cx
        uav_markers[uid]["pos2d"].set_data([X], [Y])
        uav_markers[uid]["vel2d"].remove()
        # uav_markers[uid]["vel2d"] = ax2d.quiver(X, Y, vx, vy, color="red")
        uav_markers[uid]["vel2d"] = safe_quiver_2d(ax2d, X, Y, vx_2d, vy_2d, base_color=to_rgba("red")[:3], scale=1.025, headwidth=5.25, headlength=4.25, zorder=9)
        uav_markers[uid]["cmd2d"].remove()
        # uav_markers[uid]["cmd2d"] = ax2d.quiver(X, Y, cx, cy, color="green")
        uav_markers[uid]["cmd2d"] = safe_quiver_2d(ax2d, X, Y, cx_2d, cy_2d, base_color=to_rgba("green")[:3], scale=1.025, headwidth=5.25, headlength=4.25, zorder=9)

        # 添加 UAV 的图例
        legend_entries.append(uav_markers[uid]["pos3d"])

    # 3D 箭头图例
    arrow_legend_entries = add_arrow_legend(ax3d)
    legend_entries.extend(arrow_legend_entries)

    # 更新图例
    ax3d.legend(handles=legend_entries, fontsize=FONT_SIZE_LEGEND, loc='upper left')        # 共用
    #ax2d.legend(handles=legend_entries, fontsize=FONT_SIZE_LEGEND, loc='upper left')

    return []


def plot_ref_trajectories(frame):
    """绘制参考轨迹 - 只显示上一个路点到当前目标"""
    global ref_lines_3d, ref_lines_2d

    # 清除之前的参考轨迹
    for line in ref_lines_3d:
        line.remove()
    for line in ref_lines_2d:
        line.remove()

    ref_lines_3d = []
    ref_lines_2d = []

    #t = t_min + frame / fps
    t = frame_times[frame]

    for ui, uid in enumerate(active_uav_ids):
        # 获取当前无人机的位置
        if waypt_index[ui] < 1:
            continue

        #
        # 之前已经转换过坐标了
        last_waypt_index = team_run[ui][waypt_index[ui] - 1]
        curr_waypt_index = team_run[ui][waypt_index[ui]]
        X1, Y1, Z1, _ = waypoints[str(last_waypt_index)]["pos"]
        X2, Y2, Z2, _ = waypoints[str(curr_waypt_index)]["pos"]
        #
        X1, Y1, Z1 = transform_coords(X1, Y1, Z1)
        X2, Y2, Z2 = transform_coords(X2, Y2, Z2)
        # X1, Y1, Z1 = rotate_data_axis_custom(X1, Y1, Z1)          # TODO to check
        # X2, Y2, Z2 = rotate_data_axis_custom(X2, Y2, Z2)

        Z1 = Z2 = 0.75  # set Z in force

        # 绘制参考轨迹
        line3d = ax3d.plot([X1, X2], [Y1, Y2], [Z1, Z2], color=to_rgba(uav_colors[ui], 0.75), lw=1.5, linestyle='--', zorder=35)
        line2d = ax2d.plot([X1, X2], [Y1, Y2], color=to_rgba(uav_colors[ui], 0.75), lw=1.5, linestyle='--', zorder=35)

        ref_lines_3d.extend(line3d)
        ref_lines_2d.extend(line2d)


def plot_arrived_waypts(frame):
    """绘制已到达的路点 - 带有淡出效果"""
    global arrived_waypts_3d, arrived_waypts_2d, waypt_arrived_time

    # 清除之前的到达点
    for scatter in arrived_waypts_3d:
        scatter.remove()
    for scatter in arrived_waypts_2d:
        scatter.remove()

    arrived_waypts_3d = []
    arrived_waypts_2d = []

    t = frame_times[frame]

    for ui, uid in enumerate(active_uav_ids):
        waypts_to_show = []

        for i, (waypt_time, waypt_coords) in enumerate(zip(waypt_arrived_time[ui], waypt_to_add[ui])):
            time_since_arrival = t - waypt_time

            if time_since_arrival <= WAYPT_DISPLAY_DURATION:
                waypts_to_show.append((waypt_coords, time_since_arrival))

        # 绘制带淡出效果的路点
        for (X, Y, Z), time_since_arrival in waypts_to_show:
            # 计算透明度（随时间淡出）
            alpha = 1.0 - (time_since_arrival / WAYPT_DISPLAY_DURATION)
            alpha = max(0, min(1, alpha))  # 限制在0-1范围内

            waypt_color = [float(c) / 255 for c in [243, 232, 168]] + [alpha]
            waypt_edge_color = [float(c) / 255 for c in [105, 145, 203]] + [alpha]

            scatter3d = ax3d.scatter(X, Y, Z, s=60, facecolors=waypt_color, edgecolors=waypt_edge_color,
                                     linewidths=1.5, zorder=100)
            scatter2d = ax2d.scatter(X, Y, s=60, facecolors=waypt_color, edgecolors=waypt_edge_color,
                                     linewidths=1.5, zorder=100)

            arrived_waypts_3d.append(scatter3d)
            arrived_waypts_2d.append(scatter2d)

def update(frame):
    check_arrived_waypts(frame)

    ani_traj_vel = plot_traj_and_vel_vectors(frame)
    ani_ref      = plot_ref_trajectories(frame)
    ani_arrived  = plot_arrived_waypts(frame)

    return ani

# ================= 保存和播放 =================
ani = FuncAnimation(fig, update, frames=nframes, interval=1000/fps, blit=False)

if SHOW_VIDEO:
    plt.show()

    # TO illustrate final rpy
    current_azim = ax3d.azim
    current_elev = ax3d.elev
    current_roll = ax3d.roll  # 注意：roll属性可能在较旧的Matplotlib版本中不可用

    print(f"当前方位角 (azim): {current_azim}")
    print(f"当前仰角 (elev): {current_elev}")
    print(f"当前翻滚角 (roll): {current_roll}")

if SAVE_VIDEO:
    print("🎬 保存视频中...")
    writer = FFMpegWriter(fps=fps, metadata=dict(artist="me"))
    with Progress() as progress:
        task = progress.add_task("[green]Writing frames...", total=nframes)
        writer.setup(fig, save_file, dpi=100)
        for frame in track(range(nframes), description="Rendering frames"):
            update(frame)
            writer.grab_frame()
            progress.update(task, advance=1)
        writer.finish()
    print(f"✅ 已保存视频到 {save_file}")

