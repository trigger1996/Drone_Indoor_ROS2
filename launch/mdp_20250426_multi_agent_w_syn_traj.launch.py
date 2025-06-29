from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import math

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
        '20250426_map_w_edges.yaml'
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
                executable='mdp_20250426_multi_agent_w_syn_traj_main.py',
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
