#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
import os
from collections import OrderedDict

def load_waypoints_from_yaml(yaml_path):
    # 获取相对路径对应的绝对路径，兼容运行路径变化
    yaml_path = os.path.abspath(yaml_path)

    with open(yaml_path, 'r') as file:
        #yaml_data = yaml.load(file, Loader=yaml.FullLoader)
        yaml_data = yaml.load(file, Loader=yaml.UnsafeLoader)

    # 如果是 OrderedDict 格式（例如你 YAML 是使用 OrderedDict dump 的）
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

    return waypoints
#
# uncomment and run this file for debugging
# if __name__ == "__main__":
#     # 指定 YAML 路径（相对路径）
#     yaml_path = "../../model/20250506_map_w_edges.yaml"  # ← 修改这里的“名字.yaml”为你实际的文件名
#     waypoints = load_waypoints_from_yaml(yaml_path)
    
#     print("✅ 读取到的无人机路点如下：")
#     for wp in waypoints:
#         print(f"ID: {wp['id']}, Pos: {wp['pos']}, Transition: {wp['transition']}")
