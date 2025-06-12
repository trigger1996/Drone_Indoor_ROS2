from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import PythonExpression
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # 声明 drone_num 参数并设置默认值为 '3'
    drone_num = LaunchConfiguration('drone_num')

    declare_drone_num = DeclareLaunchArgument(
        'drone_num',
        default_value='3',
        description='Number of drones to control (up to 10)'
    )

    file_path = PathJoinSubstitution([
        FindPackageShare('drone_ros2_centralized_control'),
        'model',
        'mapt.yaml'
    ])

    nodes = []

    # 启动多个无人机控制节点（最多支持10架）
    for i in range(1, 11):                                                                  # maximal number只能写死
        nodes.append(
            Node(
                package='drone_ros2_centralized_control',
                executable='mdp_20250506_single_agent_main.py',
                name=f'mdp_run_uav_{i}',
                output='screen',
                parameters=[{'drone_id': i,
                             'map_file': file_path}],
                remappings=[
                    (f'/cmd_arm_disarm_{i}',         '/uav_cmd'),
                    (f'/cmd_vel_{i}',               f'/px4_{i}/cmd_vel'),
                    (f'/mavrouter/drone_pose_{i}',  f'/px4_{i}/odom'),
                    (f'/mavrouter/drone_state_{i}', f'/px4_{i}/state'),
                ],                             
                condition=IfCondition(PythonExpression([drone_num, ' >= ', str(i)]))        # 这里会break出去
            )
        )

    # Gazebo 转发节点（默认控制1和2号无人机，可根据 drone_num 修改）
    nodes.append(
        Node(
            package='drone_ros2_centralized_control',  # 替换为你的包名
            executable='gazebo_px4_relay.py',
            name='gazebo_px4_relay',
            output='screen',
            parameters=[{'uav_ids': [1, 2, 3]}]  # 可根据 drone_num 设置动态生成
        )
    )

    return LaunchDescription([declare_drone_num] + nodes)
