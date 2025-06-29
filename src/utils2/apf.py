#!/usr/bin/pyhton2
# -*- coding: UTF-8 -*-
import math
import numpy as np
from utils2.vis import print_c

def compute_apf_force(position, goal=None, obstacles=None, 
                      k_att=1.0, k_rep=100.0, rep_radius=2.0):
    """
    人工势场避碰算法
    参数：
        position: 当前坐标 (x, y)
        goal: 目标坐标 (x, y)
        obstacles: 障碍物列表，每个为 (x, y)
        k_att: 吸引力系数
        k_rep: 斥力系数
        rep_radius: 斥力影响范围（距离越远斥力越小）
    返回：
        总合力向量 np.array([fx, fy])
    """
    pos = np.array(position, dtype=float)
    goal = np.array(goal, dtype=float)

    # 吸引力
    if goal != None:
        att_force = -k_att * (pos - goal)
    else:
        att_force = 0.

    # 斥力初始化
    if obstacles != None:
        rep_force = np.zeros(2)

        for obs in obstacles:
            if position == obs:
                continue                                # 

            obs_pos = np.array(obs, dtype=float)
            diff = pos - obs_pos
            dist = np.linalg.norm(diff)
            if dist < 1e-5:
                continue  # 避免除以0
            if dist < rep_radius:
                # 计算斥力，离障碍越近斥力越大
                rep = k_rep * (1.0 / dist - 1.0 / rep_radius) / (dist ** 3) * diff
                rep_force += rep
    else:
        rep_force = 0.

    # 合力
    total_force = att_force + rep_force
    return total_force

def compute_apf_force_scalar(position, goal=None, obstacles=None, 
                             k_att=1.0, k_rep=100.0, rep_radius=2.0):
    """
    单轴人工势场避碰算法（适用于 x 或 y 坐标标量值）
    
    参数：
        position: 当前坐标（标量 float）
        goal: 目标坐标（标量 float）
        obstacles: 障碍物坐标列表，每个为 float（即某一维坐标）
        k_att: 吸引力系数
        k_rep: 斥力系数
        rep_radius: 斥力作用半径
    返回：
        合力值（float）
    """
    pos = float(position)

    # 吸引力
    if goal is not None:
        att_force = -k_att * (pos - float(goal))
    else:
        att_force = 0.0

    # 斥力
    rep_force = 0.0
    if obstacles is not None:
        for obs in obstacles:
            obs_pos = float(obs)
            diff = pos - obs_pos
            dist = abs(diff)
            if dist < 1e-5:
                continue  # 避免除0
            if dist < rep_radius:
                rep = k_rep * (1.0 / dist - 1.0 / rep_radius) / (dist ** 3) * diff
                rep_force += rep

    total_force = att_force + rep_force
    return total_force

def normalize_force(force, max_speed=1.0):
    """将合力归一化为最大速度限制"""
    norm = np.linalg.norm(force)
    if norm > max_speed:
        return force / norm * max_speed
    return force


def combination_func(u_original, u_apf):
    """
    合并原始控制指令和APF避障修正。
    如果两者方向相反，且APF修正更强，则将输出设为0以避免冲突。
    """
    u_output = u_original + u_apf

    # 如果方向相反，且APF修正幅度大于原始控制，则抑制
    if u_original * u_apf < 0.:
        if math.fabs(u_apf) > math.fabs(u_original):
            u_output = 0.0
    return u_output

def apf_collision_avoidance(uav_pos, other_uav_pos, u, k, radius, is_visualize=True, visualize_force_threshold=0.33):
    '''
        uav_pos        : [x, y]
        other_uav_pos  : dict of {drone_id: [x, y]}  ← 比如 {1: [1.1, 0.4]}
        u              : 原始速度向量 [vx, vy]
    '''
    if not other_uav_pos:
        return u[0], u[1]
    
    x_curr = uav_pos[0]
    y_curr = uav_pos[1]

    x_t = [pos[0] for pos in other_uav_pos.values()]
    y_t = [pos[1] for pos in other_uav_pos.values()]

    ux_apf = compute_apf_force_scalar(x_curr, obstacles=x_t, k_rep=k, rep_radius=radius)
    uy_apf = compute_apf_force_scalar(y_curr, obstacles=y_t, k_rep=k, rep_radius=radius)

    if is_visualize:
        if abs(ux_apf) > visualize_force_threshold or abs(uy_apf) > visualize_force_threshold:
            print(f"[APF WARNING] 强斥力检测: ux_apf = {ux_apf:.3f}, uy_apf = {uy_apf:.3f}, "
                  f"\t 无人机位置: ({x_curr:.2f}, {y_curr:.2f})",
                  f"\t 无人机速度: ({u[0]:.2f},   {u[1]:.2f})")

    ux_p = combination_func(u[0], ux_apf)
    uy_p = combination_func(u[1], uy_apf)

    return ux_p, uy_p