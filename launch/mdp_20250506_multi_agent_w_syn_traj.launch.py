from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import math


def generate_launch_description():
    declare_drone_num = DeclareLaunchArgument(
        'drone_num',
        default_value='2',
        description='Number of drones to control (up to 10)'
    )

    return LaunchDescription([
        declare_drone_num,
        OpaqueFunction(function=launch_setup)
    ])


def launch_setup(context, *args, **kwargs):
    drone_num = int(LaunchConfiguration('drone_num').perform(context))
    
    file_path = PathJoinSubstitution([
        FindPackageShare('drone_ros2_centralized_control'),
        'model',
        '20250506_map_w_edges.yaml'
    ]).perform(context)

    initial_yaw = 90. * math.pi / 180.
    pose_params = {}

    for i in range(1, 11):
        X_t = 0.0
        Y_t = 3 * i
        Z_t = 0.83
        X = Y_t
        Y = X_t
        Z =   0.            # alternative: -Z_t; here we force set the initial z to zero
        yaw = 0.0

        pose_params[f'initial_pose_{i}_x']   = float(X)
        pose_params[f'initial_pose_{i}_y']   = float(Y)
        pose_params[f'initial_pose_{i}_z']   = float(Z)
        pose_params[f'initial_pose_{i}_yaw'] = float(yaw)

    nodes = []

    for i in range(1, 11):
        if i > drone_num:
            continue

        remaps = [
            (f'/cmd_arm_disarm_{i}',         '/uav_cmd'),
            (f'/cmd_vel_{i}',               f'/px4_{i}/cmd_vel'),
            (f'/mavrouter/drone_pose_{i}',  f'/px4_{i}/odom'),
            (f'/mavrouter/drone_state_{i}', f'/px4_{i}/state'),
        ]

        for j in range(1, 11):
            if j == i:
                continue
            remaps.append(
                (f'/mavrouter/drone_pose_{j}', f'/px4_{j}/odom')
            )

        params = {
            'drone_id': i,
            'drone_num': drone_num,
            'map_file': file_path,
            **pose_params
        }

        nodes.append(
            Node(
                package='drone_ros2_centralized_control',
                executable='mdp_20250506_multi_agent_w_syn_traj_main.py',
                name=f'mdp_run_uav_{i}',
                output='screen',
                parameters=[params],
                remappings=remaps
            )
        )

    # Gazebo relay nodes
    nodes.append(
        Node(
            package='drone_ros2_centralized_control',
            executable='gazebo_px4_relay.py',
            name='gazebo_px4_relay',
            output='screen',
            parameters=[{'uav_ids': list(range(1, drone_num + 1))}]
        )
    )

    nodes.append(
        Node(
            package='drone_ros2_centralized_control',
            executable='gazebo_controller.py',
            name='gazebo_controller',
            output='screen',
            parameters=[{'map_file': file_path}]
        )
    )

    return nodes
