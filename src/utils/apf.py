#!/usr/bin/python2
# -*- coding: UTF-8 -*-
import math
import numpy as np
from utils2.vis import print_c

def compute_apf_force(position, goal=None, obstacles=None, 
                      k_att=1.0, k_rep=100.0, rep_radius=2.0):
    """
    人工势场避碰算法 (Python 2兼容版)
    参数：
        position: 当前坐标 (x, y)
        goal: 目标坐标 (x, y)
        obstacles: 障碍物列表，每个为 (x, y)
        k_att: 吸引力系数
        k_rep: 斥力系数
        rep_radius: 斥力影响范围
    返回：
        总合力向量 np.array([fx, fy])
    """
    pos = np.array(position, dtype=float)
    # 吸引力
    if goal is not None:
        goal = np.array(goal, dtype=float)
        att_force = -k_att * (pos - goal)
    else:
        att_force = np.zeros(2)

    # 斥力初始化
    rep_force = np.zeros(2)
    if obstacles is not None:
        for obs in obstacles:
            if np.array_equal(position, obs):
                continue

            obs_pos = np.array(obs, dtype=float)
            diff = pos - obs_pos
            dist = np.linalg.norm(diff)
            if dist < 1.e-3:
                continue  # 避免除以0
            if dist < rep_radius:
                rep = k_rep * (1.0 / dist - 1.0 / rep_radius) / (dist ** 3) * diff
                rep_force += rep

    # 合力
    total_force = att_force + rep_force
    return total_force

def normalize_force(force, max_speed=1.0):
    """将合力归一化为最大速度限制 (Python 2兼容版)"""
    norm = np.linalg.norm(force)
    if norm > max_speed:
        return force / norm * max_speed
    return force

def combination_func(u_original, u_apf):
    """
    合并原始控制指令和APF避障修正 (Python 2兼容版)
    """
    u_output = u_original + u_apf

    # 如果方向相反，且APF修正幅度大于原始控制，则抑制
    if u_original * u_apf < 0.0:
        if math.fabs(u_apf) > math.fabs(u_original):
            u_output = 0.0
    return u_output

def add_random_repulsion(force, max_random_strength=0.2):
    """
    添加随机方向斥力 (Python 2兼容版)
    """
    # 生成随机方向单位向量
    theta = np.random.uniform(0, 2 * np.pi)
    random_direction = np.array([np.cos(theta), np.sin(theta)])

    # 生成随机幅度
    magnitude = np.random.uniform(0, max_random_strength)

    # 合成扰动
    random_force = magnitude * random_direction

    return force + random_force

def apf_collision_avoidance(uav_pos, other_uav_pos, u, k, radius, is_visualize=True, visualize_force_threshold=0.33):
    '''
    APF避碰控制器 (Python 2兼容版)
    参数：
        uav_pos        : [x, y] 当前无人机位置
        other_uav_pos  : dict of {drone_id: [x, y]} 
        u              : 原始速度向量 [vx, vy]
        k              : 斥力系数
        radius         : 斥力影响半径
        is_visualize   : 是否打印APF强度
    返回：
        修正后的速度 (vx', vy')
    '''
    if not other_uav_pos:
        return u[0], u[1]
    
    # 当前坐标
    pos = np.array(uav_pos, dtype=float)

    # 构建障碍物列表
    obstacles = [np.array(p, dtype=float) for p in other_uav_pos.values()]

    # 计算合力（只考虑斥力）
    force = compute_apf_force(position=pos, goal=None, obstacles=obstacles, 
                            k_att=0.0, k_rep=k, rep_radius=radius)

    norm = np.linalg.norm(force)
    if norm > 0.:
        force = add_random_repulsion(force, max_random_strength=0.2)

    # 可视化检测
    if is_visualize and np.linalg.norm(force) > visualize_force_threshold:
        print("[APF WARNING] 强斥力检测: force = {}, \t无人机位置: {}, \t障碍物位置: {}".format(
            force, uav_pos, other_uav_pos))

    # 合并原始速度与斥力矢量
    ux_p = combination_func(u[0], force[0])
    uy_p = combination_func(u[1], force[1])

    return ux_p, uy_p

