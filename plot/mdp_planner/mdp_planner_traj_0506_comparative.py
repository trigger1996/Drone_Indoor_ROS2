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

#
dataset_bag_mapping = {
    '0506_single_opaque'    : "/home/droneyee/zt_ws/bags/0506_single_real/[group_1_opaque]2025-08-23-01-03-30.bag",  # 请替换为实际路径
    '0506_single_non_opaque': "/home/droneyee/zt_ws/bags/0506_single_real/[group_1_nonopaque]2025-08-23-00-46-31.bag"  # 请替换为实际路径
}
yaml_file = "/home/droneyee/zt_ws/src/drone_ros_centeralized_control/map/mdp_planner/yaml/20250506_map_w_edges.yaml"

uav_colors = [(219, 114, 118), (80, 103, 237), (241, 105, 187), (185, 251, 96), (35, 220, 197), (162, 224, 31),
              (9, 247, 9)]
uav_colors = [tuple(float(x) / 255 for x in color) for color in uav_colors]

ap_color_mapping = {"{'gather'}"     : [(213, 230, 102), (42, 25, 153)],
                    "{'upload'}"     : [(169, 86, 176), (86, 169, 79)],
                    "{'recharge'}"   : [(46,  175, 255), (209, 80, 0)],
                    "{'investigate'}": [(165, 115, 73), (236, 199, 110)],
                    "{''}"           : [(250, 135, 119), (5, 120, 136)], }
ap_color_mapping = {
    key: [tuple(map(lambda x: float(x) / 255, color)) for color in value]
    for key, value in ap_color_mapping.items()
}


# 为不同数据集定义不同的样式
dataset_styles = {
    '0506_single_opaque'    : {'color': to_rgba([x / 255.0 for x in [228, 104,   0]])[:3], 'linestyle': '-',  'marker': 'o', 'label': 'Opaque Trajectory'},
    '0506_single_non_opaque': {'color': to_rgba([x / 255.0 for x in [1,   105, 222]])[:3], 'linestyle': '--', 'marker': 's', 'label': 'Non-Opaque Trajectory'}
}

# 存储所有数据集的信息
all_datasets = {}

#if CASE_NAME == '0506_single_opaque':
if True:
    optimal_run = """'19', '('l',)', '18', '('l',)', '17', '('u',)', '12', '('d',)', '17', '('r',)', '18', '('l',)', '12', '('d',)', '17', '('r',)', '18', '('r',)', '19', '('u',)', '14', '('d',)', '19', '('d',)', '24', '('u',)', '19', '('d',)', '24', '('u',)', '19', '('u',)', '14', '('d',)', '19', '('d',)', '24', '('l',)', '18', '('l',)', '12', '('d',)', '17', '('r',)', '18', '('l',)', '17', '('u',)', '12', '('d',)', '17', '('r',)', '18', '('r',)', '19'"""
    waypt_time = {'start': (1755882215.399430,),
                  'mission_start': (1755882217.999386,),
                  'landing': (1755882377.9013343,)}

    # 存储数据集信息
    all_datasets['0506_single_opaque'] = {
        'optimal_run': optimal_run,
        'waypt_time': waypt_time,
        'ap_color_mapping': ap_color_mapping
    }

#if CASE_NAME == '0506_single_non_opaque':
if True:
    optimal_run = """"'19' '('l',)' '18' '('u',)' '13' '('r',)' '14' '('d',)' '19' '('l',)' '18' '('u',)' '13' '('d',)' '18' '('r',)' '19' '('d',)' '24' '('l',)' '18' '('u',)' '13' '('u',)' '8' '('u',)' '3' '('d',)' '8' '('d',)' '13' '('u',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('u',)' '3' '('l',)' '2' '('r',)' '3' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('d',)' '12' '('l',)' '11' '('l',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21'"""  # TODO
    waypt_time = {'start': (1755881198.227331,),  # TODO need to check csv if use the other bags
                  'mission_start': (1755881200.9272728,)}

    # 存储数据集信息
    all_datasets['0506_single_non_opaque'] = {
        'optimal_run': optimal_run,
        'waypt_time': waypt_time,
        'ap_color_mapping': ap_color_mapping
    }

# 处理颜色映射
# for dataset_name, dataset_info in all_datasets.items():
#     ap_color_mapping = dataset_info['ap_color_mapping']
#     all_datasets[dataset_name]['ap_color_mapping'] = {
#         key: [tuple(map(lambda x: float(x) / 255, color)) for color in value]
#         for key, value in ap_color_mapping.items()
#     }

#
fps = 30
figsize = (16, 9)  # 宽高比 16:9
init_elev = 22.5  # 初始仰角
init_azim = 57.5  # 初始方位角

# 坐标轴设置
IS_INVERT_X_AXIS = True
IS_INVERT_Y_AXIS = True  # north相反, 和拍摄方向一致
SYMMETRIC_AXES = True
AXIS_PADDING = 0.5

UAV_SIZE = 15
WAYPT_SIZE = 350
FONT_SIZE_LABEL = 26
FONT_SIZE_WAYPT = 14
FONT_SIZE_TICK = 18
FONT_SIZE_TITLE = 32
FONT_SIZE_LEGEND = 18
COST_MULTIPLIERS = 6.5

IS_WAIT_UNTIL_TIME_EXCEEDED = False
WAYPT_RADIUS = 0.275

# 设置不同数据集的参数
for dataset_name in all_datasets.keys():
    all_datasets[dataset_name]['FONT_SIZE_WAYPT'] = 14
    all_datasets[dataset_name]['COST_MULTIPLIERS'] = 6.5
    all_datasets[dataset_name]['IS_WAIT_UNTIL_TIME_EXCEEDED'] = False
    all_datasets[dataset_name]['WAYPT_RADIUS'] = 0.275

# 使用 Euclid 字体
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Euclid"
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
all_pose_data = {}
all_odom_data = {}
all_cmd_data = {}

for dataset_name in all_datasets.keys():
    bag_file = dataset_bag_mapping[dataset_name]

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
            print(f"[WARN] No pose data for drone {uid} in {dataset_name}, skipping ...")
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

    # 只保留真正有pose数据的无人机
    active_uav_ids = [uid for uid in active_uav_ids if uid in pose_data]

    all_pose_data[dataset_name] = pose_data
    all_odom_data[dataset_name] = odom_data
    all_cmd_data[dataset_name] = cmd_data


def calculate_axis_limits(all_pose_data, waypoints, padding=AXIS_PADDING, symmetric=True):
    """
    计算所有数据的坐标轴范围
    """
    # 初始化极值
    all_x, all_y, all_z = [], [], []

    # 收集所有数据集的所有无人机的位置数据
    for dataset_name, pose_data in all_pose_data.items():
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
    else:
        # 非对称坐标轴范围
        x_lim = (all_x.min() - padding, all_x.max() + padding)
        y_lim = (all_y.min() - padding, all_y.max() + padding)
    z_lim = (max(0, all_z.min() - padding), all_z.max() + padding)

    print(f"X轴范围: {x_lim}")
    print(f"Y轴范围: {y_lim}")
    print(f"Z轴范围: {z_lim}")

    return x_lim, y_lim, z_lim


def interpolate(df, t):
    if df is None or t < df['Time'].min() or t > df['Time'].max():
        return None
    return df.iloc[(df['Time'] - t).abs().argmin()]


# ========== 预先计算坐标轴范围 ==========
x_lim, y_lim, z_lim = calculate_axis_limits(all_pose_data, waypoints,
                                            padding=AXIS_PADDING,
                                            symmetric=SYMMETRIC_AXES)
# ========== 绘图准备 ==========
# 第一张图：3D和2D对比图
fig_comparison = plt.figure(figsize=(16, 8))
gs_comparison = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=0.25)

# 创建子图
ax_3d = fig_comparison.add_subplot(gs_comparison[0], projection='3d')  # 3D轨迹对比
ax_2d = fig_comparison.add_subplot(gs_comparison[1])  # 2D投影对比

# 设置坐标轴范围
ax_3d.set_xlim(x_lim)
ax_3d.set_ylim(y_lim)
ax_3d.set_zlim(z_lim)
ax_3d.view_init(elev=init_elev, azim=init_azim)

ax_2d.set_xlim(x_lim)
ax_2d.set_ylim(y_lim)
if IS_INVERT_Y_AXIS:
    ax_2d.invert_yaxis()
if IS_INVERT_X_AXIS:
    ax_2d.invert_xaxis()

# 第二张图：单独的2D平面图
fig_2d_only = plt.figure(figsize=(12, 10))
ax_2d_only = fig_2d_only.add_subplot(111)

# 设置坐标轴范围
ax_2d_only.set_xlim(x_lim)
ax_2d_only.set_ylim(y_lim)
if IS_INVERT_Y_AXIS:
    ax_2d_only.invert_yaxis()
if IS_INVERT_X_AXIS:
    ax_2d_only.invert_xaxis()


# 绘制地图函数
def draw_3d_map(ax):
    for node_id, node_info in waypoints.items():
        ap = node_info["ap"][0]
        ap_2_display = r"$\{" + re.sub(r"^\{['\"](.*)['\"]\}$", r"\1", ap) + r"\}$"
        Xned, Yned, Z, yaw = node_info["pos"]
        Xned, Yned, Z = rotate_data_axis_custom(Xned, Yned, Z)
        Z = 0.75

        if ap in ap_color_mapping.keys():
            center_color = ap_color_mapping[ap][0]
            edge_color   = ap_color_mapping[ap][1]
        else:
            center_color = [ float(c) / 255 for c in [147, 224, 255] ]
            edge_color   = [ float(c) / 255 for c in [38,  157, 128] ]

        ax.scatter(Xned, Yned, Z, c=[center_color],  edgecolors=[edge_color], s=WAYPT_SIZE, linewidths=1.5, alpha=0.85)
        ax.text(Xned, Yned, Z, f"$q_{{{node_id}}}$\n${ap_2_display}$", fontsize=FONT_SIZE_WAYPT, zorder=200)

    for edge in edges:
        src, dst, attr = edge
        x1, y1, z1, _ = waypoints[src]["pos"]
        x2, y2, z2, _ = waypoints[dst]["pos"]
        X1, Y1, Z1 = x1, y1, z1
        X2, Y2, Z2 = x2, y2, z2

        X1, Y1, Z1 = rotate_data_axis_custom(X1, Y1, Z1)
        X2, Y2, Z2 = rotate_data_axis_custom(X2, Y2, Z2)
        Z1 = Z2 = 0.75

        ax.plot([X1, X2], [Y1, Y2], [Z1, Z2], "gray", alpha=0.5, linewidth=3.25)

    ax.set_xlabel("$y$ (East) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=15)
    ax.set_ylabel("$x$ (North) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=15)
    ax.set_zlabel("$z$ (Altitude) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=15)
    ax.set_title("3D Trajectory", fontsize=FONT_SIZE_TITLE, pad=22)

    ax.tick_params(axis='x', labelsize=FONT_SIZE_TICK)
    ax.tick_params(axis='y', labelsize=FONT_SIZE_TICK)
    ax.tick_params(axis='z', labelsize=FONT_SIZE_TICK)

def draw_2d_map(ax, title="2D Projection Comparison"):
    for node_id, node_info in waypoints.items():
        ap = node_info["ap"][0]
        ap_2_display = r"$\{" + re.sub(r"^\{['\"](.*)['\"]\}$", r"\1", ap) + r"\}$"
        Xned, Yned, Z, yaw = node_info["pos"]
        Xned, Yned, Z = rotate_data_axis_custom(Xned, Yned, Z)

        if ap in ap_color_mapping.keys():
            center_color = ap_color_mapping[ap][0]
            edge_color   = ap_color_mapping[ap][1]
        else:
            center_color = [ float(c) / 255 for c in [147, 224, 255] ]
            edge_color   = [ float(c) / 255 for c in [38,  157, 128] ]

        ax.scatter(Xned, Yned, c=[center_color], edgecolors=[edge_color], s=WAYPT_SIZE, linewidths=1.5, alpha=0.85)
        ax.text(Xned, Yned, f"$q_{{{node_id}}}$\n${ap_2_display}$", fontsize=FONT_SIZE_WAYPT, zorder=200)

    for edge in edges:
        src, dst, attr = edge
        x1, y1, z1, _ = waypoints[src]["pos"]
        x2, y2, z2, _ = waypoints[dst]["pos"]
        X1, Y1, Z1 = x1, y1, z1
        X2, Y2, Z2 = x2, y2, z2

        X1, Y1, Z1 = rotate_data_axis_custom(X1, Y1, Z1)
        X2, Y2, Z2 = rotate_data_axis_custom(X2, Y2, Z2)

        ax.plot([X1, X2], [Y1, Y2], "gray", alpha=0.5, linewidth=3.25)

    ax.set_xlabel("$y$ (East) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=7.5)
    ax.set_ylabel("$x$ (North) /$m$", fontsize=FONT_SIZE_LABEL, labelpad=7.5)
    ax.set_title(title, fontsize=FONT_SIZE_TITLE, pad=22)

    ax.tick_params(axis='x', labelsize=FONT_SIZE_TICK)
    ax.tick_params(axis='y', labelsize=FONT_SIZE_TICK)


def adjust_opacity(base_color, opacity_factor):
    """根据给定的透明度因子调整颜色的透明度"""
    if len(base_color) == 3:
        base_color = np.append(base_color, 1.0)
    r, g, b = base_color[:3]
    a = base_color[3]
    new_alpha = np.clip(a * opacity_factor, 0, 1)
    return (r, g, b, new_alpha)


# 绘制无人机轨迹
def plot_uav_trajectory_3d(ax, dataset_name, pose_data, style):
    """在3D图上绘制轨迹"""
    for ui, uid in enumerate(pose_data.keys()):
        uav_data = pose_data[uid]
        times = uav_data["Time"]
        x, y, z = [], [], []

        for ti, t in enumerate(times):
            pose = interpolate(uav_data, t)
            if pose is not None:
                X, Y, Z = transform_coords(pose['pose.position.x'],
                                           pose['pose.position.y'],
                                           pose['pose.position.z'])
                X, Y, Z = rotate_data_axis_custom(X, Y, Z)
                x.append(X)
                y.append(Y)
                z.append(Z)

        # 采样减少数据点
        sample_rate = 10
        x = x[::sample_rate]
        y = y[::sample_rate]
        z = z[::sample_rate]

        # 计算透明度
        alpha_vals = np.linspace(0.35, 0.95, len(x))
        base_color = to_rgba(style['color'])[:3]

        # 绘制轨迹
        for j in range(1, len(x)):
            adjusted_color = adjust_opacity(base_color, alpha_vals[j])
            label = style['label'] if ui == 0 and j == len(x) - 1 else ""
            ax.plot([x[j - 1], x[j]], [y[j - 1], y[j]], [z[j - 1], z[j]],
                    color=adjusted_color, lw=2, label=label,
                    linestyle=style['linestyle'], zorder=25)


def plot_uav_trajectory_2d(ax, dataset_name, pose_data, style):
    """在2D图上绘制轨迹"""
    for ui, uid in enumerate(pose_data.keys()):
        uav_data = pose_data[uid]
        times = uav_data["Time"]
        x, y = [], []

        for ti, t in enumerate(times):
            pose = interpolate(uav_data, t)
            if pose is not None:
                X, Y, Z = transform_coords(pose['pose.position.x'],
                                           pose['pose.position.y'],
                                           pose['pose.position.z'])
                X, Y, Z = rotate_data_axis_custom(X, Y, Z)
                x.append(X)
                y.append(Y)

        # 采样减少数据点
        sample_rate = 10
        x = x[::sample_rate]
        y = y[::sample_rate]

        # 计算透明度
        alpha_vals = np.linspace(0.35, 0.95, len(x))
        base_color = to_rgba(style['color'])[:3]

        # 绘制轨迹
        for j in range(1, len(x)):
            adjusted_color = adjust_opacity(base_color, alpha_vals[j])
            label = style['label'] if ui == 0 and j == len(x) - 1 else ""
            ax.plot([x[j - 1], x[j]], [y[j - 1], y[j]],
                    color=adjusted_color, lw=2, label=label,
                    linestyle=style['linestyle'], zorder=25)


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

# 新增的函数 - 绘制参考轨迹
def plot_ref_trajectories(ax_3d, ax_2d, ax_2d_only, dataset_name, optimal_run, style):
    """绘制参考轨迹"""
    # 获取无人机数量
    pose_data = all_pose_data[dataset_name]
    num_drones = len(pose_data.keys())

    team_run = extract_states_from_joint_x_u_lists(optimal_run, num_drones=num_drones)

    for i in range(0, num_drones):
        for t in range(1, len(team_run[i])):
            label_t = f"{style['label']} Reference" if i == 0 and t == len(team_run[i]) - 1 else ""
            base_color = to_rgba(style['color'])[:3]  # 使用数据集的颜色
            alpha_vals = np.linspace(0.55, 0.975, len(team_run))
            adjusted_color = adjust_opacity(base_color, alpha_vals[i])

            uav_state_i_last = team_run[i][t - 1]
            uav_state_i = team_run[i][t]

            x1, y1, z1, _ = waypoints[str(uav_state_i_last)]["pos"]
            x2, y2, z2, _ = waypoints[str(uav_state_i)]["pos"]
            X1, Y1, Z1 = x1, y1, z1
            X2, Y2, Z2 = x2, y2, z2

            X1, Y1, Z1 = rotate_data_axis_custom(X1, Y1, Z1)
            X2, Y2, Z2 = rotate_data_axis_custom(X2, Y2, Z2)

            Z1 = Z2 = 0.75  # set Z in force

            # 在所有三个轴上绘制参考轨迹
            ax_3d.plot([X1, X2], [Y1, Y2], [Z1, Z2],
                       color=adjusted_color, lw=1.5, linestyle='--', label=label_t, zorder=35)
            ax_2d.plot([X1, X2], [Y1, Y2],
                       color=adjusted_color, lw=1.5, linestyle='--', label=label_t, zorder=35)
            ax_2d_only.plot([X1, X2], [Y1, Y2],
                            color=adjusted_color, lw=1.5, linestyle='--', label=label_t, zorder=35)


# 新增的函数 - 绘制到达的航点
def plot_arrived_waypts(ax_3d, ax_2d, ax_2d_only, dataset_name, pose_data, optimal_run, waypt_time, style, is_add_lengend=True):
    """绘制到达的航点"""

    def get_edge_info(edges_list, id_last, id_curr):
        """在 edges_list 中查找从 id_last 到 id_curr 的边信息"""
        for edge in edges_list:
            if edge[0] == str(id_last) and edge[1] == str(id_curr):
                return edge[2]  # 返回属性字典
        raise ValueError(f"No edge from {id_last} to {id_curr} in map...")

    # 获取无人机数量
    num_drones = len(pose_data.keys())
    team_run = extract_states_from_joint_x_u_lists(optimal_run, num_drones=num_drones)
    waypt_index = [0 for ui in range(0, num_drones)]
    waypt_to_add = [[] for ui in range(0, num_drones)]
    is_reached_waypt_legend_added = not is_add_lengend

    # accumulated cost_list
    transition_cost_list = [[0.] for ui in range(0, num_drones)]
    accumulated_time_list = [[0.] for ui in range(0, num_drones)]

    for ui, uid in enumerate(pose_data.keys()):
        for i in range(1, len(team_run[ui])):
            id_last = team_run[ui][i - 1]  # 节点 ID
            id_curr = team_run[ui][i]

            try:
                cost_t = 0.
                # 计算成本（只适用于单无人机情况）
                pos_last = waypoints[str(id_last)]["pos"]
                pos_now = waypoints[str(id_curr)]["pos"]

                dx = pos_now[0] - pos_last[0]
                dy = pos_now[1] - pos_last[1]
                dz = pos_now[2] - pos_last[2]

                cost_t = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2) * all_datasets[dataset_name]['COST_MULTIPLIERS']

                acc_cost_t = accumulated_time_list[ui][-1] + cost_t
                transition_cost_list[ui].append(cost_t)
                accumulated_time_list[ui].append(acc_cost_t)
            except KeyError:
                raise ValueError(f"No edge from {id_last} to {id_curr} in map...")

    for ui, uid in enumerate(pose_data.keys()):
        uav_data = pose_data[uid]
        times = uav_data["Time"]
        x, y, z = [], [], []

        # 获取任务开始时间
        mission_start_time = waypt_time['mission_start']
        if isinstance(mission_start_time, (list, tuple)):
            mission_start_time = mission_start_time[0] if ui < len(mission_start_time) else mission_start_time[0]

        # 通过时间点绘制轨迹
        for ti, t in enumerate(times):
            # 确定起飞时间, 起飞时间之前的不算
            if t < mission_start_time:
                continue
            if dataset_name == '0506_single_opaque' and 'landing' in waypt_time and t > min(
                    waypt_time['landing']) + 1.5:
                continue

            pose = interpolate(uav_data, t)
            if pose is not None:
                X, Y, Z = transform_coords(pose['pose.position.x'], pose['pose.position.y'], pose['pose.position.z'])
                X, Y, Z = rotate_data_axis_custom(X, Y, Z)
                x.append(X)
                y.append(Y)
                z.append(Z)

                # 计算当前位置是否到达目标
                target = waypoints[str(team_run[ui][waypt_index[ui]])]["pos"]
                target = transform_coords(target[0], target[1], target[2])
                err_x = target[0] - X
                err_y = target[1] - Y
                err_z = target[2] - Z
                dist = math.sqrt(err_x ** 2 + err_y ** 2)

                # Decision
                should_switch_waypoint = False
                limited_time = mission_start_time + accumulated_time_list[ui][waypt_index[ui]]
                is_exceed_current_time = t > limited_time

                if all_datasets[dataset_name]['IS_WAIT_UNTIL_TIME_EXCEEDED']:
                    # 要等到时间到了再换点
                    if dist < all_datasets[dataset_name]['WAYPT_RADIUS'] and is_exceed_current_time:
                        should_switch_waypoint = True
                else:
                    # 提前到达或时间到了都可以换点
                    if dist < all_datasets[dataset_name]['WAYPT_RADIUS'] or is_exceed_current_time:
                        should_switch_waypoint = True

                if should_switch_waypoint:
                    if waypt_index[ui] < len(team_run[ui]) - 1:
                        waypt_index[ui] += 1
                        waypt_to_add[ui].append((X, Y, Z))

        for j in range(0, len(waypt_to_add[ui])):
            #label_t = f"{style['label']} Reached Waypoint" if not is_reached_waypt_legend_added else ""
            label_t = f"Reached Waypoint" if not is_reached_waypt_legend_added else ""
            X, Y, Z = waypt_to_add[ui][j]
            waypt_color = [float(c) / 255 for c in [243, 232, 168]]
            waypt_edge_color = [float(c) / 255 for c in [105, 145, 203]]

            # 在所有三个轴上绘制到达的航点
            ax_3d.scatter(X, Y, Z, s=60, facecolors=waypt_color,
                          edgecolors=waypt_edge_color, linewidths=1.5, label=label_t, zorder=100)
            ax_2d.scatter(X, Y, s=60, facecolors=waypt_color,
                          edgecolors=waypt_edge_color, linewidths=1.5, label=label_t, zorder=100)
            ax_2d_only.scatter(X, Y, s=60, facecolors=waypt_color,
                               edgecolors=waypt_edge_color, linewidths=1.5, label=label_t, zorder=100)

            # 确保 legend 只加一次
            if not is_reached_waypt_legend_added:
                is_reached_waypt_legend_added = True


# 绘制地图
draw_3d_map(ax_3d)
draw_2d_map(ax_2d, "")
draw_2d_map(ax_2d_only, "")

# 为每个数据集绘制轨迹
for i, dataset_name in enumerate(all_datasets.keys()):
    style = dataset_styles[dataset_name]
    pose_data = all_pose_data[dataset_name]
    dataset_info = all_datasets[dataset_name]

    # 绘制实际轨迹
    plot_uav_trajectory_3d(ax_3d, dataset_name, pose_data, style)
    plot_uav_trajectory_2d(ax_2d, dataset_name, pose_data, style)
    plot_uav_trajectory_2d(ax_2d_only, dataset_name, pose_data, style)

    # 绘制参考轨迹
    plot_ref_trajectories(ax_3d, ax_2d, ax_2d_only, dataset_name, dataset_info['optimal_run'], style)

    # 绘制到达的航点
    is_add_legend = True if i == len(all_datasets.keys()) - 1 else False
    plot_arrived_waypts(ax_3d, ax_2d, ax_2d_only, dataset_name, pose_data,
                        dataset_info['optimal_run'], dataset_info['waypt_time'], style, is_add_lengend=is_add_legend)

# 添加图例
ax_3d.legend(loc='upper left', fontsize=FONT_SIZE_LEGEND)
#ax_2d.legend(loc='upper left', fontsize=FONT_SIZE_LEGEND)
ax_2d_only.legend(loc='lower left', fontsize=FONT_SIZE_LEGEND)

# 调整布局并显示
plt.figure(fig_comparison.number)
plt.tight_layout()

plt.figure(fig_2d_only.number)
plt.tight_layout()

plt.show()