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
    # 吸引力
    if goal is not None:
        goal = np.array(goal, dtype=float)
        att_force = -k_att * (pos - goal)
    else:
        att_force = np.zeros(2)

    # print(f"pos: {pos} | goal: {goal} | att_force: {att_force}")

    # 斥力初始化
    if obstacles != None:
        rep_force = np.zeros(2)

        for obs in obstacles:
            if np.array_equal(position, obs):
                continue                        # 

            obs_pos = np.array(obs, dtype=float)
            diff = pos - obs_pos
            dist = np.linalg.norm(diff)
            if dist < 1.e-3:
                continue  # 避免除以0
            if dist < rep_radius:
                # 计算斥力，离障碍越近斥力越大
                rep = k_rep * (1.0 / dist - 1.0 / rep_radius) / (dist ** 3) * diff
                rep_force += rep
    else:
        rep_force = np.zeros(2)

    # 合力
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
    APF避碰控制器，基于compute_apf_force函数（二维）
    参数：
        uav_pos        : [x, y] 当前无人机位置
        other_uav_pos  : dict of {drone_id: [x, y]} ← 其他无人机坐标
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

    # 构建障碍物列表（二维坐标）
    obstacles = [np.array(p, dtype=float) for p in other_uav_pos.values()]

    # 计算合力（此处 goal=None，只考虑斥力）
    force = compute_apf_force(position=pos, goal=None, obstacles=obstacles, k_att=0.0, k_rep=k, rep_radius=radius)

    # 可视化检测
    if is_visualize:
        if np.linalg.norm(force) > visualize_force_threshold:
            print(f"[APF WARNING] 强斥力检测: force = {force}, "
                  f"\t无人机位置: {uav_pos}, "
                  f"\t障碍物位置: {other_uav_pos}")

    # 分别合并原始速度与斥力矢量
    ux_p = combination_func(u[0], force[0])
    uy_p = combination_func(u[1], force[1])

    return ux_p, uy_p
