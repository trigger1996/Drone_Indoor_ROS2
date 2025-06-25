#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
import os
import re
import ast
from collections import OrderedDict
from utils2.vis import print_c, format_logger

def load_waypoints_from_yaml(yaml_path, is_visualize=True):
    # 获取绝对路径
    yaml_path = os.path.abspath(yaml_path)

    with open(yaml_path, 'r') as file:
        # 读取 YAML 文件内容
        yaml_data = yaml.load(file, Loader=yaml.UnsafeLoader)

    # 转为普通 dict
    if isinstance(yaml_data, OrderedDict):
        yaml_data = dict(yaml_data)

    waypoint_data = yaml_data.get("waypoint", {})

    waypoints = []
    for wp_id, wp_info in waypoint_data.items():
        pos = wp_info["pos"]  # [x, y, z, yaw]
        transition = wp_info["transition"]
        waypoints.append({
            "id": wp_id,
            "pos": pos,
            "transition": transition
        })

    if is_visualize:                # verbose
        print_c(f"\n✔ Loaded {len(waypoints)} waypoints from: {yaml_path}", color='green')  # green
        print_c(f"{'ID':<6} | {'Position (x,y,z,yaw)':<30} | Transitions",  color='cyan')  # cyan header
        print("-" * 80)

        #for wp in waypoints[:10]:  # alternative 只预览前10个
        for wp in waypoints:
            pos_str = f"{wp['pos']}"
            trans_str = f"{wp['transition']}"
            print_c(f"{wp['id']:<6} | {pos_str:<30} | {trans_str}")

        if len(waypoints) > 10:
            print_c(f"... (total {len(waypoints)} waypoints)", color='yellow')  # yellow

    return waypoints

def extract_states_from_x_u_lists(x_u_list):
    # for example : ""'15' '('u',)' '10' '('u',)' '5' '('r',)' '6' '('d',)' '11' '('r',)' '12' '('l',)' '11' '('r',)' '12' '('l',)' '11' '('d',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('r',)' '17' '('l',)' '16' '('u',)' '11' '('d',)' '16' '('l',)' '15' '('d',)' '20' '('u',)' '15' '('d',)' '20' '('u',)' '15' '('r',)' '16' '('r',)' '17' '('l',)' '16' '('d',)' '21' '('l',)' '20' '('u',)' '15' '('d',)' '20' '('r',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('u',)' '1' '('d',)' '6' '('l',)' '5' '('u',)' '0' '('r',)' '1' '('d',)' '6' '('l',)' '5' '('d',)' '10' '('r',)' '11' '('d',)' '16' '('l',)' '15' '('u',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('d',)' '21' '('r',)' '17' '('l',)' '16' '('r',)' '17' '('u',)' '12' '('u',)' '7' '('u',)' '2' '('l',)' '1' '('r',)' '2' '('l',)' '1' '('l',)' '0' '('r',)' '1' '('d',)' '6' '('r',)' '7' '('l',)' '6' '('u',)' '1' '('d',)' '6' '('r',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('l',)' '7' '('d',)' '12' '('r',)' '13' '('r',)' '14' '('l',)' '13' '('u',)' '8' '('u',)' '3' '('l',)' '2' '('l',)' '1' '('l',)' '0' '('d',)' '5' '('d',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('r',)' '17' '('r',)' '18' '('u',)' '13' '('r',)' '14' '('l',)' '13' '('d',)' '18' '('u',)' '13' '('u',)' '8' '('u',)' '3' '('d',)' '8' '('d',)' '13' '('l',)' '12' '('u',)' '7' '('u',)' '2' '('d',)' '7' '('r',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('l',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('u',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('l',)' '2' '('d',)' '7' '('d',)' '12' '('u',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('d',)' '13' '('d',)' '18' '('r',)' '19' '('u',)' '14' '('l',)' '13' '('r',)' '14'"""

    x_list = re.findall(r"'(\d+)'", x_u_list)

    return x_list


def extract_states_for_all_robots(x_u_list_all):
    """
    提取所有机器人的状态序列。

    参数：
        x_u_list_all (str): 包含状态-动作对的字符串。

    返回：
        List[List[int]]: 每个机器人一条状态路径。
    """
    # 匹配状态元组：'('数字','数字')'
    state_pattern = re.compile(r"\('(\d+)',\s*'(\d+)'\)")

    # 提取所有状态对
    state_pairs = state_pattern.findall(x_u_list_all)

    if not state_pairs:
        raise ValueError("未找到任何状态对，检查输入格式是否正确")

    # 转换为 int，并按照机器人编号分组
    num_robots = len(state_pairs[0])
    robot_states = [[] for _ in range(num_robots)]

    for pair in state_pairs:
        for i in range(num_robots):
            robot_states[i].append(int(pair[i]))

    return robot_states

def print_waypoint_table_4_single_agent(x_list, waypoints_dict):
    """
    打印纵向表格：路点ID | 坐标(x, y, z)
    
    Usage:
        from collections import OrderedDict

        # x_list 是提取后的路点列表（字符串或整数都可）
        x_list = extract_states_from_x_u_lists(x_u_list)

        # 如果 self.waypoints 是 OrderedDict，确保它是字典结构
        waypoints = dict(self.waypoints)

        # 打印
        print_waypoint_table(x_list, waypoints)    
    """
    # 打印表头
    print_c(f"{'ID':<6} | {'X':>8} {'Y':>8} {'Z':>8}", color='cyan', bold=True, underline=True)
    print_c("-" * 36, color='cyan')

    printed = set()
    for idx in x_list:
        # 去重（可选）
        if idx in printed:
            continue
        printed.add(idx)

        # 处理ID为字符串的情况
        idx_str = str(idx)

        # 获取坐标
        if idx_str in waypoints_dict:
            coords = waypoints_dict[idx_str]
            if isinstance(coords, dict) and {'x', 'y', 'z'} <= coords.keys():
                x, y, z = coords['x'], coords['y'], coords['z']
            elif isinstance(coords, (list, tuple)) and len(coords) == 3:
                x, y, z = coords
            else:
                x, y, z = 'N/A', 'N/A', 'N/A'
        else:
            x, y, z = 'N/A', 'N/A', 'N/A'

        # 打印
        print_c(f"{idx_str:<6} | {x:>8} {y:>8} {z:>8}", color='green')

def format_waypoint_table_4_single_agent(sorted_waypoint_list):
    """
    返回带颜色的格式化纵向表格字符串：路点ID | 坐标(x, y, z)，用于ROS2日志打印。
    """
    ansi_colors = {
        'black': '30', 'red': '31', 'green': '32',
        'yellow': '33', 'blue': '34', 'magenta': '35',
        'cyan': '36', 'white': '37', 'reset': '0'
    }

    def color_text(text, color, bold=False):
        color_code = ansi_colors.get(color, '')
        if bold:
            return f"\033[1;{color_code}m{text}\033[0m"
        return f"\033[{color_code}m{text}\033[0m"

    # 表头
    header = f"{color_text('ID',  'white', bold=True):<6}    | " \
             f"{color_text('X',   'white', bold=True):>8}    " \
             f"{color_text('Y',   'white', bold=True):>8}    " \
             f"{color_text('Z',   'white', bold=True):>8}    "  \
             f"{color_text('YAW', 'white', bold=True):>8}"
    divider = color_text("-" * (len(header)), 'blue')
    lines = [header, divider]

    for id_str, pos in sorted_waypoint_list:
        if isinstance(pos, (list, tuple)) and len(pos) >= 3:
            x, y, z, yaw = map(str, pos[:4])
            x_colored   = color_text(x,   'yellow')
            y_colored   = color_text(y,   'yellow')
            z_colored   = color_text(z,   'yellow')
            yaw_colored = color_text(yaw, 'yellow')
        else:
            x_colored = y_colored = z_colored = yaw_colored = color_text('N/A', 'red')

        id_colored = color_text(f"{id_str:<6}", 'cyan')
        line = f"{id_colored} | {x_colored:>8}    {y_colored:>8}    {z_colored:>8}    {yaw_colored:>8}"
        lines.append(line)

    return '\n'.join(lines)

def format_waypoints_table_with_costs_4_single_agent(sorted_waypoints, transition_cost_list, accumulated_time_list):
    """
    格式化带有 transition cost 和累计时间的路点表格。
    参数:
        sorted_waypoints: [(id_str, [x, y, z, yaw]), ...]
        transition_cost_list: [float]，与路点一一对应，从1开始是每段的cost
        accumulated_time_list: [float]，累计长度（或时间）
    返回:
        字符串：格式化带颜色表格
    """
    ansi_colors = {
        'black': '30', 'red': '31', 'green': '32',
        'yellow': '33', 'blue': '34', 'magenta': '35',
        'cyan': '36', 'white': '37', 'reset': '0'
    }

    def color_text(text, color, bold=False):
        code = ansi_colors.get(color, '')
        return f"\033[{1 if bold else 0};{code}m{text}\033[0m"

    header = (
        f"{color_text('ID',  'white', True):<6} | "
        f"{color_text('X',   'white', True):>8}  "
        f"{color_text('Y',   'white', True):>8}  "
        f"{color_text('Z',   'white', True):>8}  "
        f"{color_text('YAW', 'white', True):>8} | "
        f"{color_text('Δt',  'white', True):>8}  "
        f"{color_text('AccumT', 'white', True):>10}"
    )
    divider = color_text("-" * len(header), 'blue')
    lines = [header, divider]

    for i, (id_str, pos) in enumerate(sorted_waypoints):
        if isinstance(pos, (list, tuple)) and len(pos) >= 4:
            x, y, z, yaw = pos[:4]
            x_f, y_f, z_f, yaw_f = map(lambda v: f"{v:.3f}", [x, y, z, yaw])
        else:
            x_f = y_f = z_f = yaw_f = 'N/A'

        delta_t = f"{transition_cost_list[i]:.3f}" if i < len(transition_cost_list) else "N/A"
        accum_t = f"{accumulated_time_list[i]:.3f}" if i < len(accumulated_time_list) else "N/A"

        line = (
            f"{color_text(id_str, 'cyan'):<6} | "
            f"{color_text(x_f, 'yellow'):>8}  "
            f"{color_text(y_f, 'yellow'):>8}  "
            f"{color_text(z_f, 'yellow'):>8}  "
            f"{color_text(yaw_f, 'yellow'):>8} | "
            f"{color_text(delta_t, 'magenta'):>8}  "
            f"{color_text(accum_t, 'green'):>10}"
        )
        lines.append(line)

    if len(sorted_waypoints) > 10:
        result = format_logger(f"... (total {len(sorted_waypoints)} waypoints)", color='bright_green', styles='bold')
        lines.append(result)

    return '\n'.join(lines)

#
# uncomment and run this file for debugging
# if __name__ == "__main__":
#     # 指定 YAML 路径（相对路径）
#     yaml_path = "../../model/20250506_map_w_edges.yaml"  # ← 修改这里的“名字.yaml”为你实际的文件名
#     waypoints = load_waypoints_from_yaml(yaml_path)
    
#     print("✅ 读取到的无人机路点如下：")
#     for wp in waypoints:
#         print(f"ID: {wp['id']}, Pos: {wp['pos']}, Transition: {wp['transition']}")
