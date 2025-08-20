#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import yaml
import os
import re
import ast
from collections import OrderedDict
from vis import print_c, format_logger

def load_waypoints_from_yaml(yaml_path, is_visualize=True):
    yaml_path = os.path.abspath(yaml_path)

    with open(yaml_path, 'r') as file:
        try:
            yaml_data = yaml.load(file, Loader=yaml.UnsafeLoader)  # Python 2 兼容
        except AttributeError:
            yaml_data = yaml.load(file)  # 回退

    if isinstance(yaml_data, OrderedDict):
        yaml_data = dict(yaml_data)

    waypoint_data = yaml_data.get("waypoint", {})

    waypoints = []
    for wp_id, wp_info in waypoint_data.items():
        pos = wp_info["pos"]  # [x, y, z, yaw]
        ap  = wp_info["ap"]
        transition = wp_info["transition"]
        waypoints.append({
            "id": wp_id,
            "pos": pos,
            "ap": ap,
            "transition": transition
        })

    if is_visualize:                # verbose
        print_c("\n✔ Loaded {} waypoints from: {}".format(len(waypoints), yaml_path), color='green')
        print_c("{:<6} | {:<30} | Transitions".format('ID', 'Position (x,y,z,yaw)'), color='cyan')
        print("-" * 80)

        #for wp in waypoints[:10]:  # alternative 只预览前10个
        for wp in waypoints:
            pos_str = "{}".format(wp['pos'])
            trans_str = "{}".format(wp['transition'])
            print_c("{:<6} | {:<30} | {}".format(wp['id'], pos_str, trans_str))

        if len(waypoints) > 10:
            print_c("... (total {} waypoints)".format(len(waypoints)), color='yellow')

    return waypoints

def load_transitions_from_yaml(yaml_path, is_visualize=True):
    # 获取绝对路径
    yaml_path = os.path.abspath(yaml_path)

    with open(yaml_path, 'r') as file:
        # 读取 YAML 文件内容
        yaml_data = yaml.load(file, Loader=yaml.UnsafeLoader)

    # 转为普通 dict
    if isinstance(yaml_data, OrderedDict):
        yaml_data = dict(yaml_data)

    edges_data = yaml_data.get('edges', [])

    edges_dict = {}
    for edge_entry in edges_data:
        from_id, to_id, attr = edge_entry
        if from_id not in edges_dict:
            edges_dict[from_id] = {}
        edges_dict[from_id][to_id] = {
            "control": attr.get("control"),
            "weight": attr.get("weight")
        }

    if is_visualize:
        print_c("\n✔ Loaded {} edges".format(sum(len(d) for d in edges_dict.values())), color='green')
        print_c("{:<6} -> {:<6} | {:<8} | Weight".format('From', 'To', 'Control'), color='cyan')
        print("-" * 60)
        for from_id, to_dict in edges_dict.items():
            for to_id, attr in to_dict.items():
                print_c("{:<6} -> {:<6} | {:<8} | {}".format(
                    from_id,
                    to_id,
                    attr['control'],
                    attr['weight']
                ))

    return edges_dict

def extract_states_from_x_u_lists(x_u_list):
    # for example : ""'15' '('u',)' '10' '('u',)' '5' '('r',)' '6' '('d',)' '11' '('r',)' '12' '('l',)' '11' '('r',)' '12' '('l',)' '11' '('d',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('r',)' '17' '('l',)' '16' '('u',)' '11' '('d',)' '16' '('l',)' '15' '('d',)' '20' '('u',)' '15' '('d',)' '20' '('u',)' '15' '('r',)' '16' '('r',)' '17' '('l',)' '16' '('d',)' '21' '('l',)' '20' '('u',)' '15' '('d',)' '20' '('r',)' '16' '('u',)' '11' '('r',)' '12' '('l',)' '11' '('u',)' '6' '('u',)' '1' '('d',)' '6' '('l',)' '5' '('u',)' '0' '('r',)' '1' '('d',)' '6' '('l',)' '5' '('d',)' '10' '('r',)' '11' '('d',)' '16' '('l',)' '15' '('u',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('d',)' '21' '('r',)' '17' '('l',)' '16' '('r',)' '17' '('u',)' '12' '('u',)' '7' '('u',)' '2' '('l',)' '1' '('r',)' '2' '('l',)' '1' '('l',)' '0' '('r',)' '1' '('d',)' '6' '('r',)' '7' '('l',)' '6' '('u',)' '1' '('d',)' '6' '('r',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('l',)' '7' '('d',)' '12' '('r',)' '13' '('r',)' '14' '('l',)' '13' '('u',)' '8' '('u',)' '3' '('l',)' '2' '('l',)' '1' '('l',)' '0' '('d',)' '5' '('d',)' '10' '('d',)' '15' '('d',)' '20' '('r',)' '21' '('r',)' '17' '('r',)' '18' '('u',)' '13' '('r',)' '14' '('l',)' '13' '('d',)' '18' '('u',)' '13' '('u',)' '8' '('u',)' '3' '('d',)' '8' '('d',)' '13' '('l',)' '12' '('u',)' '7' '('u',)' '2' '('d',)' '7' '('r',)' '8' '('l',)' '7' '('d',)' '12' '('d',)' '17' '('l',)' '16' '('l',)' '15' '('d',)' '20' '('r',)' '21' '('u',)' '16' '('u',)' '11' '('u',)' '6' '('r',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('d',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('u',)' '3' '('l',)' '2' '('d',)' '7' '('d',)' '12' '('u',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('l',)' '7' '('r',)' '8' '('d',)' '13' '('u',)' '8' '('d',)' '13' '('d',)' '18' '('r',)' '19' '('u',)' '14' '('l',)' '13' '('r',)' '14'"""

    if isinstance(x_u_list, unicode):
        x_u_list = x_u_list.encode('utf-8')
    return re.findall(r"'(\d+)'", x_u_list)

def extract_states_from_joint_x_u_lists(x_u_list_str, num_drones=None):
    """
    输入:
        x_u_list_str: 含联合轨迹的字符串，例如:
            "('0','5') (('a',),('a',)) ('1','4') ..."
        num_drones: 无人机数量（可选，推荐传入以避免歧义）
    输出:
        list of tuple，每个元组是一时刻所有无人机的状态，例如:
            [('0','5'), ('1','4'), ('0','3'), ...]  # 对 2 架无人机
            [('0','5','2'), ('1','4','3'), ...]     # 对 3 架无人机
    """

    if isinstance(x_u_list_str, unicode):
        x_u_list_str = x_u_list_str.encode('utf-8')

    # 提取所有数字（状态编号）
    numbers = re.findall(r"'(\d+)'", x_u_list_str)

    if not numbers:
        return []

    # 自动推测无人机数量
    if num_drones is None:
        # 你给的字符串是联合轨迹，每一时刻 = N 架无人机的状态
        # 假设长度可以整除无人机数
        for n in range(1, 10):  # 最多 10 架无人机
            if len(numbers) % n == 0:
                num_drones = n
                break
        else:
            raise ValueError("无法自动推测无人机数量，请手动传入 num_drones")

    # 按照无人机数量分组
    joint_x_u_list = []
    for i in range(0, len(numbers), num_drones):
        joint_x_u_list.append(tuple(numbers[i:i+num_drones]))

    return joint_x_u_list


def extract_states_for_all_robots(x_u_list_all):
    """
    提取所有机器人的状态序列。

    参数：
        x_u_list_all (str): 包含状态-动作对的字符串。

    返回：
        List[List[int]]: 每个机器人一条状态路径。
    """
    if isinstance(x_u_list_all, unicode):
        x_u_list_all = x_u_list_all.encode('utf-8')

    # 匹配状态元组：'('数字','数字')'
    state_pattern = re.compile(r"\('(\d+)',\s*'(\d+)'\)")
    state_pairs = state_pattern.findall(x_u_list_all)

    if not state_pairs:
        raise ValueError("No valid state pairs found")

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
    print_c("{:<6} | {:>8} {:>8} {:>8}".format('ID', 'X', 'Y', 'Z'), 
           color='cyan', styles=['bold', 'underline'])
    print_c("-" * 36, color='cyan')

    printed = set()
    for idx in x_list:
        idx_str = str(idx)
        if idx_str in printed:
            continue
        printed.add(idx_str)

        coords = waypoints_dict.get(idx_str, {})
        if isinstance(coords, dict):
            x = coords.get('x', 'N/A')
            y = coords.get('y', 'N/A')
            z = coords.get('z', 'N/A')
        elif isinstance(coords, (list, tuple)) and len(coords) >= 3:
            x, y, z = coords[:3]
        else:
            x = y = z = 'N/A'

        print_c("{:<6} | {:>8} {:>8} {:>8}".format(
            idx_str, str(x), str(y), str(z)), color='green')

def format_waypoint_table_4_single_agent(sorted_waypoint_list):
    """
    返回带颜色的格式化纵向表格字符串（Python 2兼容版）
    """
    ansi_colors = {
        'black': '30', 'red': '31', 'green': '32',
        'yellow': '33', 'blue': '34', 'magenta': '35',
        'cyan': '36', 'white': '37', 'reset': '0'
    }

    def color_text(text, color, bold=False):
        text = text if isinstance(text, str) else str(text)
        color_code = ansi_colors.get(color, '')
        bold_code = '1;' if bold else ''
        return "\033[{}{}m{}\033[0m".format(bold_code, color_code, text)

    # 表头
    header = "{}    | {}    {}    {}    {}".format(
        color_text('ID', 'white', bold=True).ljust(6),
        color_text('X', 'white', bold=True).rjust(8),
        color_text('Y', 'white', bold=True).rjust(8),
        color_text('Z', 'white', bold=True).rjust(8),
        color_text('YAW', 'white', bold=True).rjust(8)
    )
    divider = color_text("-" * len(header), 'blue')
    lines = [header, divider]

    for id_str, pos in sorted_waypoint_list:
        id_str = str(id_str)
        if isinstance(pos, (list, tuple)) and len(pos) >= 3:
            coords = map(str, pos[:4])
            x, y, z, yaw = coords if len(coords) == 4 else (coords + ('N/A',))[:4]
        else:
            x = y = z = yaw = 'N/A'

        line = "{} | {}    {}    {}    {}".format(
            color_text(id_str.ljust(6), 'cyan'),
            color_text(x.rjust(8), 'yellow'),
            color_text(y.rjust(8), 'yellow'),
            color_text(z.rjust(8), 'yellow'),
            color_text(yaw.rjust(8), 'yellow')
        )
        lines.append(line)

    return '\n'.join(lines)

def format_waypoints_table_with_costs_4_single_agent(sorted_waypoints, transition_cost_list, accumulated_time_list):
    """
    格式化带成本的路点表格（Python 2兼容版）
    """
    ansi_colors = {
        'black': '30', 'red': '31', 'green': '32',
        'yellow': '33', 'blue': '34', 'magenta': '35',
        'cyan': '36', 'white': '37', 'reset': '0'
    }

    def color_text(text, color, bold=False):
        text = text if isinstance(text, str) else str(text)
        color_code = ansi_colors.get(color, '')
        bold_code = '1;' if bold else ''
        return "\033[{}{}m{}\033[0m".format(bold_code, color_code, text)

    # 表头
    header = "{} | {}  {}  {}  {} | {}  {}".format(
        color_text('ID', 'white', True).ljust(6),
        color_text('X', 'white', True).rjust(8),
        color_text('Y', 'white', True).rjust(8),
        color_text('Z', 'white', True).rjust(8),
        color_text('YAW', 'white', True).rjust(8),
        color_text('dt', 'white', True).rjust(8),
        color_text('AccumT', 'white', True).rjust(10)
    )
    print(2333)
    divider = color_text("-" * len(header), 'blue')
    lines = [header, divider]

    for i, (id_str, pos) in enumerate(sorted_waypoints):
        id_str = str(id_str)
        if isinstance(pos, (list, tuple)) and len(pos) >= 4:
            x, y, z, yaw = ["{:.3f}".format(float(v)) for v in pos[:4]]
        else:
            x = y = z = yaw = 'N/A'

        delta_t = "{:.3f}".format(float(transition_cost_list[i])) if i < len(transition_cost_list) else "N/A"
        accum_t = "{:.3f}".format(float(accumulated_time_list[i])) if i < len(accumulated_time_list) else "N/A"

        line = "{} | {}  {}  {}  {} | {}  {}".format(
            color_text(id_str.ljust(6), 'cyan'),
            color_text(x.rjust(8), 'yellow'),
            color_text(y.rjust(8), 'yellow'),
            color_text(z.rjust(8), 'yellow'),
            color_text(yaw.rjust(8), 'yellow'),
            color_text(delta_t.rjust(8), 'magenta'),
            color_text(accum_t.rjust(10), 'green')
        )
        lines.append(line)

    if len(sorted_waypoints) > 10:
        result = format_logger("... (total {} waypoints)".format(len(sorted_waypoints)), 
                             color='bright_green', styles='bold')
        lines.append(result)

    return '\n'.join(lines)

#
# uncomment and run this file for debugging
# if __name__ == "__main__":
#     # 指定 YAML 路径（相对路径）
#     yaml_path = "../../map/20250506_map_w_edges.yaml"  # ← 修改这里的“名字.yaml”为你实际的文件名
#     waypoints = load_waypoints_from_yaml(yaml_path)
    
#     print("✅ 读取到的无人机路点如下：")
#     for wp in waypoints:
#         print(f"ID: {wp['id']}, Pos: {wp['pos']}, Transition: {wp['transition']}")
