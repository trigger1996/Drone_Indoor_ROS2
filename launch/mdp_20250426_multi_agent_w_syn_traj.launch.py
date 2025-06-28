import math
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
    '''
    # 默认初始航向角为0, 在gazebo内向东
    function spawn_model() {
        MODEL=$1
        N=$2 #Instance Number
        X=$3
        Y=$4
        X=${X:=0.0}
        Y=${Y:=$((3*${N}))}

        SUPPORTED_MODELS=("iris" "plane" "standard_vtol" "rover" "r1_rover" "typhoon_h480")
        if [[ " ${SUPPORTED_MODELS[*]} " != *"$MODEL"* ]];
        then
            echo "ERROR: Currently only vehicle model $MODEL is not supported!"
            echo "       Supported Models: [${SUPPORTED_MODELS[@]}]"
            trap "cleanup" SIGINT SIGTERM EXIT
            exit 1
        fi

        working_dir="$build_path/rootfs/$n"
        [ ! -d "$working_dir" ] && mkdir -p "$working_dir"

        pushd "$working_dir" &>/dev/null
        echo "starting instance $N in $(pwd)"
        $build_path/bin/px4 -i $N -d "$build_path/etc" >out.log 2>err.log &

        set --
        set -- ${@} ${src_path}/Tools/simulation/gazebo-classic/sitl_gazebo-classic/scripts/jinja_gen.py
        set -- ${@} ${src_path}/Tools/simulation/gazebo-classic/sitl_gazebo-classic/models/${MODEL}/${MODEL}.sdf.jinja
        set -- ${@} ${src_path}/Tools/simulation/gazebo-classic/sitl_gazebo-classic
        set -- ${@} --mavlink_tcp_port $((4560+${N}))
        set -- ${@} --mavlink_udp_port $((14560+${N}))
        set -- ${@} --mavlink_id $((1+${N}))
        set -- ${@} --gst_udp_port $((5600+${N}))
        set -- ${@} --video_uri $((5600+${N}))
        set -- ${@} --mavlink_cam_udp_port $((14530+${N}))
        set -- ${@} --output-file /tmp/${MODEL}_${N}.sdf

        python3 ${@}

        echo "Spawning ${MODEL}_${N} at ${X} ${Y}"

        gz model --spawn-file=/tmp/${MODEL}_${N}.sdf --model-name=${MODEL}_${N} -x ${X} -y ${Y} -z 0.83

        popd &>/dev/null

    }
    '''
    drone_num = LaunchConfiguration('drone_num')

    declare_drone_num = DeclareLaunchArgument(
        'drone_num',
        default_value='2',                                                                  # Modified
        description='Number of drones to control (up to 10)'
    )

    file_path = PathJoinSubstitution([
        FindPackageShare('drone_ros2_centralized_control'),
        'model',
        '20250426_map_w_edges.yaml'
    ])

    nodes = []
    # 为每个无人机构建 initial_pose 参数，包含所有其他无人机的初始位置
    pose_params = {}
    initial_yaw = 90. * math.pi / 180.
    for i in range(1, 11):
        X_t = 0.0
        Y_t = 3 * i
        Z_t = 0.83
        X = Y_t
        Y = X_t
        Z = -Z_t
        yaw = 0.0

        pose_params[f'initial_pose_{i}_x'] = X
        pose_params[f'initial_pose_{i}_y'] = Y
        pose_params[f'initial_pose_{i}_z'] = Z
        pose_params[f'initial_pose_{i}_yaw'] = yaw

        print(f"initial_pose_{i}: x={X:.2f}, y={Y:.2f}, z={Z:.2f}, yaw={yaw:.2f}")
        print("-" * 20)

    # 启动多个无人机控制节点（最多支持10架）
    for i in range(1, 11):                                                                  # maximal number只能写死
        remaps = [
                (f'/cmd_arm_disarm_{i}',         '/uav_cmd'),
                (f'/cmd_vel_{i}',               f'/px4_{i}/cmd_vel'),
                (f'/mavrouter/drone_pose_{i}',  f'/px4_{i}/odom'),
                (f'/mavrouter/drone_state_{i}', f'/px4_{i}/state'),
            ]

        # 添加其他 UAV 的 pose 订阅 remapping
        for j in range(1, 11):
            if j == i:
                continue
            remaps.append(
                (f'/mavrouter/drone_pose_{j}', f'/px4_{j}/odom')
            )

        nodes.append(
            Node(
                package='drone_ros2_centralized_control',
                executable='mdp_20250426_multi_agent_w_syn_traj_main.py',
                name=f'mdp_run_uav_{i}',
                output='screen',
                parameters=[
                    {'drone_id': i,
                    'drone_num': drone_num,
                    'map_file': file_path,
                    **pose_params                                                           # 包含所有无人机的初始位置
                    }
                ],
                remappings=remaps,
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
            parameters=[{'uav_ids': [1, 2]}]  # 可根据 drone_num 设置动态生成
        )
    )

    nodes.append(
        Node(
            package='drone_ros2_centralized_control',
            executable='gazebo_controller.py',
            name='gazebo_controller',
            output='screen',
            parameters=[{'map_file': file_path}],
        )
    )

    return LaunchDescription([declare_drone_num] + nodes)
