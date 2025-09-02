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
CASE_NAME = '0506_single_opaque'
#CASE_NAME = '0506_single_non_opaque'
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

# TODO
# 0426 multi
uav_colors = [(219, 114, 118), (80, 103, 237), (241, 105, 187), (185, 251, 96), (35, 220, 197), (162, 224, 31), (9, 247, 9)]
uav_colors = [tuple(float(x) / 255 for x in color) for color in uav_colors]
#
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

ap_color_mapping = {"{'gather'}": [(250, 135, 119), (5, 120, 136)],
                    "{'upload'}": [(169, 86, 176), (86, 169, 79)],
                    "{'recharge'}": [(46, 175, 255), (209, 80, 0)],
                    "{''}": [(213, 230, 102), (42, 25, 153)], }  # 0426                                                                                                                        # 0426
if CASE_NAME == '0506_single_opaque':
    optimal_run = """'19', '('l',)', '18', '('l',)', '17', '('u',)', '12', '('d',)', '17', '('r',)', '18', '('l',)', '12', '('d',)', '17', '('r',)', '18', '('r',)', '19', '('u',)', '14', '('d',)', '19', '('d',)', '24', '('u',)', '19', '('d',)', '24', '('u',)', '19', '('u',)', '14', '('d',)', '19', '('d',)', '24', '('l',)', '18', '('l',)', '12', '('d',)', '17', '('r',)', '18', '('l',)', '17', '('u',)', '12', '('d',)', '17', '('r',)', '18', '('r',)', '19'"""
    waypt_time = {'start'         : (1755882215.399430, ),
                  'mission_start' : (1755882217.999386, ),
                  'landing' : (1755882377.9013343,)}

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

# 0506 single

ap_color_mapping = {
    key: [tuple(map(lambda x: float(x) / 255, color)) for color in value]
    for key, value in ap_color_mapping.items()
}
#
fps       = 30
figsize   = (16, 9)   # 宽高比 16:9
init_elev = 22.5      # 初始仰角
init_azim = 57.5      # 初始方位角

# 坐标轴设置
IS_INVERT_X_AXIS = True
IS_INVERT_Y_AXIS = True      # north相反, 和拍摄方向一致
SYMMETRIC_AXES = True
AXIS_PADDING = 0.5

UAV_SIZE = 15
WAYPT_SIZE = 350
FONT_SIZE_LABEL = 26
FONT_SIZE_WAYPT = 22
FONT_SIZE_TICK = 18
FONT_SIZE_TITLE = 32
FONT_SIZE_LEGEND = 18
COST_MULTIPLIERS = 3.5                      # TODO

IS_WAIT_UNTIL_TIME_EXCEEDED = True          # TODO
WAYPT_RADIUS = 0.225

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

# 使用 Euclid 字体
plt.rcParams.update({
    "text.usetex" : True,
    "font.family" : "Euclid"
})

# ========== 坐标变换函数 ==========
def transform_coords(x, y, z, source="ENU", target="NEU"):
    if source == target:
        return x, y, z

    if source == "NEU":
        x, y, z = y, x, z
    elif source == "NED":
        x, y, z = y, x, -z

    if target == "NEU":
        return y, x, z
    elif target == "NED":
        return y, x, -z
    elif target == "ENU":
        return x, y, z
    else:
        raise ValueError(f"Unknown target frame: {target}")

def rotate_data_axis_custom(x, y, z):
    return y, x, z

# ========== 读取地图 ==========
with open(yaml_file, "r") as f:
    data = yaml.load(f, Loader=yaml.UnsafeLoader)

waypoints = data["waypoint"]
edges = data["edges"]

# ========== 读取 rosbag ==========
b = bagreader(bag_file)
topics = b.topic_table["Topics"].tolist()

pose_topics = [t for t in topics if "/vrpn_client_node/droneyee" in t and "/pose" in t]

active_uav_ids = sorted(int(t.split("droneyee")[-1].split("/")[0]) for t in pose_topics)

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

def interpolate(df, t):
    if df is None or t < df['Time'].min() or t > df['Time'].max():
        return None
    return df.iloc[(df['Time']-t).abs().argmin()]

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

# ========== 时间对齐 ==========
t_min = min(df['Time'].min() for df in pose_data.values())
t_max = max(df['Time'].max() for df in pose_data.values())
duration = t_max - t_min
nframes = int(duration * fps)

# ========== 绘图准备 ==========
# 创建3个图，每个图独立显示

# 图一：三维坐标子图 + 二维坐标子图
fig1 = plt.figure(figsize=(16, 9))
gs = gridspec.GridSpec(1, 2, width_ratios=[1.65,1], wspace=0.35)  # 调整间距和大小
ax3d = fig1.add_subplot(gs[0], projection='3d')  # 1行2列，选择第1个子图
ax2d = fig1.add_subplot(gs[1])  # 1行2列，选择第2个子图

# 图二：只显示三维坐标子图
fig2 = plt.figure(figsize=(16, 9))
ax3d_trajectory = fig2.add_subplot(111, projection='3d')  # 只有一个子图

# 图三：只显示二维坐标子图
fig3 = plt.figure(figsize=(16, 9))
ax2d_xy = fig3.add_subplot(111)  # 只有一个子图

# 设置坐标轴范围
ax3d.set_xlim(x_lim)
ax3d.set_ylim(y_lim)
ax3d.set_zlim(z_lim)
ax2d.set_xlim(x_lim)
ax2d.set_ylim(y_lim)
ax3d_trajectory.set_xlim(x_lim)
ax3d_trajectory.set_ylim(y_lim)
ax2d_xy.set_xlim(x_lim)
ax2d_xy.set_ylim(y_lim)
#
if IS_INVERT_Y_AXIS:
    ax2d.invert_yaxis()
    #ax2d_xy.invert_yaxis()     # might be better
if IS_INVERT_X_AXIS:
    ax2d.invert_xaxis()
    #ax2d_xy.invert_xaxis()

# 设置初始 3D 视角
ax3d.view_init(elev=init_elev, azim=init_azim)
ax3d_trajectory.view_init(elev=init_elev, azim=init_azim)

# 绘制地图
def draw_3d_map(ax3d):
    for node_id, node_info in waypoints.items():
        ap = node_info["ap"][0]
        ap_2_display = r"$\{" + re.sub(r"^\{['\"](.*)['\"]\}$", r"\1", ap) + r"\}$"  # 去掉单引号和双引号
        Xned, Yned, Z, yaw = node_info["pos"]
        Xned, Yned, Z = rotate_data_axis_custom(Xned, Yned, Z)
        Z = 0.75                                                    # for set Z

        if ap in ap_color_mapping.keys():
            center_color = ap_color_mapping[ap][0]
            edge_color   = ap_color_mapping[ap][1]
        else:
            center_color = [ float(c) / 255 for c in [147, 224, 255] ]
            edge_color   = [ float(c) / 255 for c in [38,  157, 128] ]

        ax3d.scatter(Xned, Yned, Z, c=[center_color],  edgecolors=[edge_color], s=WAYPT_SIZE, linewidths=1.5, alpha=0.85)
        ax3d.text(Xned, Yned, Z, f"{node_id}\n{ap_2_display}", fontsize=FONT_SIZE_WAYPT, zorder=200)

    for edge in edges:
        src, dst, attr = edge
        x1, y1, z1, _ = waypoints[src]["pos"]
        x2, y2, z2, _ = waypoints[dst]["pos"]
        X1, Y1, Z1 = x1, y1, z1
        X2, Y2, Z2 = x2, y2, z2

        X1, Y1, Z1  = rotate_data_axis_custom(X1, Y1, Z1)
        X2, Y2, Z2  = rotate_data_axis_custom(X2, Y2, Z2)

        Z1 = Z2 = 0.75                      # set Z in force

        ax3d.plot([X1, X2], [Y1, Y2], [Z1, Z2], "gray", alpha=0.5, linewidth=3.25)

    ax3d.set_xlabel("$y$ (East)  /$m$", fontsize=FONT_SIZE_LABEL, labelpad=15)
    ax3d.set_ylabel("$x$ (North) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=15)
    ax3d.set_zlabel("$z$ (Altitude) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=15)
    ax3d.set_title("3D Trajectory", fontsize=FONT_SIZE_TITLE, pad=22)

    ax3d.tick_params(axis='x', labelsize=FONT_SIZE_TICK)
    ax3d.tick_params(axis='y', labelsize=FONT_SIZE_TICK)
    ax3d.tick_params(axis='z', labelsize=FONT_SIZE_TICK)

def draw_2d_map(ax2d):
    for node_id, node_info in waypoints.items():
        ap = node_info["ap"][0]
        ap_2_display = r"$\{" + re.sub(r"^\{['\"](.*)['\"]\}$", r"\1", ap) + r"\}$"  # 去掉单引号和双引号
        Xned, Yned, Z, yaw = node_info["pos"]
        Xned, Yned, Z = rotate_data_axis_custom(Xned, Yned, Z)

        if ap in ap_color_mapping.keys():
            center_color = ap_color_mapping[ap][0]
            edge_color   = ap_color_mapping[ap][1]
        else:
            center_color = [ float(c) / 255 for c in [147, 224, 255] ]
            edge_color   = [ float(c) / 255 for c in [38,  157, 128] ]

        ax2d.scatter(Xned, Yned, c=[center_color], edgecolors=[edge_color], s=WAYPT_SIZE, linewidths=1.5, alpha=0.85)
        ax2d.text(Xned, Yned, f"{node_id}\n{ap_2_display}", fontsize=FONT_SIZE_WAYPT, zorder=200)

    for edge in edges:
        src, dst, attr = edge
        x1, y1, z1, _ = waypoints[src]["pos"]
        x2, y2, z2, _ = waypoints[dst]["pos"]
        X1, Y1, Z1 = x1, y1, z1
        X2, Y2, Z2 = x2, y2, z2

        X1, Y1, Z1  = rotate_data_axis_custom(X1, Y1, Z1)
        X2, Y2, Z2  = rotate_data_axis_custom(X2, Y2, Z2)

        ax2d.plot([X1, X2], [Y1, Y2], "gray", alpha=0.5, linewidth=3.25)

    ax2d.set_xlabel("$y$ (East)  /$m$", fontsize=FONT_SIZE_LABEL, labelpad=7.5)
    ax2d.set_ylabel("$x$ (North) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=7.5)
    ax2d.set_title("Horizontal Projection", fontsize=FONT_SIZE_TITLE, pad=22)

    ax2d.tick_params(axis='x', labelsize=FONT_SIZE_TICK)
    ax2d.tick_params(axis='y', labelsize=FONT_SIZE_TICK)

def adjust_opacity(base_color, opacity_factor):
    """根据给定的透明度因子调整颜色的透明度"""
    # 如果 base_color 只有 3 个元素（RGB），就添加 alpha 通道，默认 alpha 为 1.0（完全不透明）
    if len(base_color) == 3:
        base_color = np.append(base_color, 1.0)  # 添加 alpha 通道

    # 获取原始的 RGB 和 alpha 通道
    r, g, b = base_color[:3]
    a = base_color[3]

    # 调整透明度
    new_alpha = np.clip(a * opacity_factor, 0, 1)  # 确保透明度在 0 到 1 之间

    # 返回修改后的 RGBA 颜色
    return to_rgba((r, g, b, new_alpha))

# 绘制无人机轨迹
def plot_uav_trajectory():
    for ui, uid in enumerate(active_uav_ids):
        uav_data = pose_data[uid]
        times = uav_data["Time"]
        x, y, z = [], [], []

        # 通过时间点绘制轨迹
        for ti, t in enumerate(times):
            pose = interpolate(uav_data, t)
            if pose is not None:
                X, Y, Z = transform_coords(pose['pose.position.x'], pose['pose.position.y'], pose['pose.position.z'])
                X, Y, Z = rotate_data_axis_custom(X, Y, Z)
                x.append(X)
                y.append(Y)
                z.append(Z)

        # 每隔sample_rate个数据点绘制一次
        sample_rate = 10                # TODO for debugging
        x = x[::sample_rate]
        y = y[::sample_rate]
        z = z[::sample_rate]

        # 计算透明度因子：使用时间或轨迹长度来计算透明度
        alpha_vals = np.linspace(0.35, 0.875, len(x))

        # 计算颜色并调整透明度
        # 假设我们使用 'red' 作为基础颜色，透明度随着轨迹的时间/长度渐变
        base_color = to_rgba(uav_colors[ui])[:3]  # RGB部分

        # 绘制XYZ轨迹，颜色根据时间渐变 为每个点调整透明度并应用颜色渐变
        for j in range(1, len(x)):
            adjusted_color = adjust_opacity(base_color, alpha_vals[j])
            # 绘制轨迹段并为每条线设置 label
            label = f"UAV {ui+1} Trajectory" if j == len(x) - 1 else ""  # 只为第一段轨迹设置 label
            ax3d.plot([x[j-1], x[j]], [y[j-1], y[j]], [z[j-1], z[j]],            color=adjusted_color, lw=2, label=label, zorder=25)
            ax2d.plot([x[j-1], x[j]], [y[j-1], y[j]],                            color=adjusted_color, lw=2, label=label, zorder=25)
            ax3d_trajectory.plot([x[j-1], x[j]], [y[j-1], y[j]], [z[j-1], z[j]], color=adjusted_color, lw=2, label=label, zorder=25)
            ax2d_xy.plot([x[j-1], x[j]], [y[j-1], y[j]],                         color=adjusted_color, lw=2, label=label, zorder=25)

def plot_ref_trajectories():
    # TODO
    team_run = extract_states_from_joint_x_u_lists(optimal_run, num_drones=len(active_uav_ids))
    for i in range(0, len(active_uav_ids)):
        for t in range(1, len(team_run[i])):
            label_t = f"Reference {i+1} Trajectory" if t == len(team_run[i]) - 1 else ""  # 只为第一段轨迹设置 label
            base_color = to_rgba(uav_colors[i])[:3]  # RGB部分
            alpha_vals = np.linspace(0.35, 0.95, len(team_run))
            adjusted_color = adjust_opacity(base_color, alpha_vals[i])

            uav_state_i_last = team_run[i][t - 1]
            uav_state_i      = team_run[i][t]

            x1, y1, z1, _ = waypoints[str(uav_state_i_last)]["pos"]
            x2, y2, z2, _ = waypoints[str(uav_state_i)]["pos"]
            X1, Y1, Z1 = x1, y1, z1
            X2, Y2, Z2 = x2, y2, z2

            X1, Y1, Z1  = rotate_data_axis_custom(X1, Y1, Z1)
            X2, Y2, Z2  = rotate_data_axis_custom(X2, Y2, Z2)

            Z1 = Z2 = 0.75  # set Z in force

            # '-' 实线（默认） '--' 虚线 '-.' 点划线 ':' 点线
            ax3d.plot([X1, X2], [Y1, Y2], [Z1, Z2],            color=adjusted_color, lw=1.5, linestyle='--', label=label_t, zorder=35)         # zorder越大层次越靠前
            ax2d.plot([X1, X2], [Y1, Y2],                      color=adjusted_color, lw=1.5, linestyle='--', label=label_t, zorder=35)
            ax3d_trajectory.plot([X1, X2], [Y1, Y2], [Z1, Z2], color=adjusted_color, lw=1.5, linestyle='--', label=label_t, zorder=35)
            ax2d_xy.plot([X1, X2], [Y1, Y2],                   color=adjusted_color, lw=1.5, linestyle='--', label=label_t, zorder=35)


def plot_arrived_waypts():
    def get_edge_info(edges_list, id_last, id_curr):
        """在 edges_list 中查找从 id_last 到 id_curr 的边信息"""
        for edge in edges_list:
            if edge[0] == str(id_last) and edge[1] == str(id_curr):
                return edge[2]  # 返回属性字典
        raise ValueError(f"No edge from {id_last} to {id_curr} in map...")

    team_run = extract_states_from_joint_x_u_lists(optimal_run, num_drones=len(active_uav_ids))
    waypt_index = [0 for ui in range(0, len(active_uav_ids))]
    waypt_to_add = [[] for ui in range(0, len(active_uav_ids))]
    is_reached_waypt_legend_added = False

    # step 1
    # accumulated cost_list
    transition_cost_list  = [[0.] for ui in range(0, len(active_uav_ids))]
    accumulated_time_list = [[0.] for ui in range(0, len(active_uav_ids))]
    for ui, uid in enumerate(active_uav_ids):
        for i in range(1, team_run[ui].__len__()):
            id_last = team_run[ui][i - 1]  # 节点 ID
            id_curr = team_run[ui][i]
            #
            try:
                cost_t = 0.
                if CASE_NAME == '0426_multi':
                    #
                    edge_info = get_edge_info(edges, id_last, id_curr)
                    cost_t = edge_info['weight'] * COST_MULTIPLIERS
                if CASE_NAME == '0506_single_opaque' or CASE_NAME == '0506_single_non_opaque':
                    #
                    pos_last = waypoints[str(team_run[ui][id_last])]["pos"]
                    pos_now = waypoints[str(team_run[ui][id_curr])]["pos"]

                    dx = pos_now[0] - pos_last[0]
                    dy = pos_now[1] - pos_last[1]
                    dz = pos_now[2] - pos_last[2]

                    cost_t = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2) * COST_MULTIPLIERS

                acc_cost_t = accumulated_time_list[ui][accumulated_time_list[ui].__len__() - 1] + cost_t
                transition_cost_list[ui].append(cost_t)
                accumulated_time_list[ui].append(acc_cost_t)
            except KeyError:
                raise ValueError("No edge from %s to %s in map..." % (str(id_last), str(id_curr),))

    for ui, uid in enumerate(active_uav_ids):
        uav_data = pose_data[uid]
        times = uav_data["Time"]
        x, y, z = [], [], []

        # 通过时间点绘制轨迹
        for ti, t in enumerate(times):
            #
            # 确定起飞时间, 起飞时间之前的不算
            if t < waypt_time['mission_start'][ui]:
                continue
            if CASE_NAME == '0506_single_opaque' and t > min(waypt_time['landing']) + 1.5:
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
                # X, Y, Z = rotate_data_axis_custom(X, Y, Z)                      # no need
                err_x = target[0] - X
                err_y = target[1] - Y
                err_z = target[2] - Z
                dist = math.sqrt(err_x ** 2 + err_y ** 2)
                #
                # Decision
                should_switch_waypoint = False

                limited_time = waypt_time['mission_start'][ui] + accumulated_time_list[ui][waypt_index[ui]]

                is_exceed_current_time = t > limited_time  # TODO  current_time > limited_time + self.task_start_instant

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
                        waypt_index[ui] += 1

                    waypt_to_add[ui].append((X, Y, Z))

        for j in range(0, len(waypt_to_add[ui])):
            label_t = f"Reached Waypoint" if not is_reached_waypt_legend_added else ""  # 只为第一段轨迹设置 label
            X, Y, Z = waypt_to_add[ui][j]
            waypt_color      = [float(c) / 255 for c in [243, 232, 168]]
            waypt_edge_color = [float(c) / 255 for c in [105,  145, 203]]
            ax3d.scatter(X, Y, Z, s=60,            facecolors=waypt_color, edgecolors=waypt_edge_color, linewidths=1.5, label=label_t, zorder=100)
            ax2d.scatter(X, Y, s=60,               facecolors=waypt_color, edgecolors=waypt_edge_color, linewidths=1.5, label=label_t, zorder=100)
            ax3d_trajectory.scatter(X, Y, Z, s=60, facecolors=waypt_color, edgecolors=waypt_edge_color, linewidths=1.5, label=label_t, zorder=100)
            ax2d_xy.scatter(X, Y, s=60,            facecolors=waypt_color, edgecolors=waypt_edge_color, linewidths=1.5, label=label_t, zorder=100)


            # 确保 legend 只加一次
            if not is_reached_waypt_legend_added:
                is_reached_waypt_legend_added = True

# 绘制所有轨迹
draw_3d_map(ax3d)
draw_3d_map(ax3d_trajectory)
draw_2d_map(ax2d)
draw_2d_map(ax2d_xy)
plot_uav_trajectory()
plot_ref_trajectories()
plot_arrived_waypts()

if CASE_NAME == '0426_multi':
    #
    ax3d.legend(loc='upper left', fontsize=FONT_SIZE_LEGEND)
    ax2d_xy.legend(loc='upper left', fontsize=FONT_SIZE_LEGEND)
    ax3d_trajectory.legend(loc='upper left', fontsize=FONT_SIZE_LEGEND)
if CASE_NAME == '0506_single_opaque' or CASE_NAME == '0506_single_non_opaque':
    #
    ax3d.legend(loc='upper left', fontsize=FONT_SIZE_LEGEND)
    ax2d_xy.legend(loc='upper right', fontsize=FONT_SIZE_LEGEND)
    ax3d_trajectory.legend(loc='upper left', fontsize=FONT_SIZE_LEGEND)

# 分别显示三个图
plt.show()
