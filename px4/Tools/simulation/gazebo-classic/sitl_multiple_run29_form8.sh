#!/bin/bash
# run multiple instances of the 'px4' binary, with the gazebo SITL simulation
# It assumes px4 is already built, with 'make px4_sitl_default sitl_gazebo-classic'

# The simulator is expected to send to TCP port 4560+i for i in [0, N-1]
# For example gazebo can be run like this:
#./Tools/simulation/gazebo-classic/sitl_multiple_run.sh -n 10 -m iris

export GAZEBO_LOG_LEVEL=ERROR
echo "NO WARNING MODE!!!"
sleep 2
JSON_FILE="/home/$USERNAME/ws_px4/src/configs/missionCFG.json"

function cleanup() {
	pkill -x px4
	pkill gzclient
	pkill gzserver
}

function spawn_model() {
	MODEL=$1
	N=$2 #Instance Number
	X=$3
	Y=$4
	YAW=${5:=0.0}
	# X=${X:=0.0}
	# Y=${Y:=$((3*${N}))}

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

	gz model --spawn-file=/tmp/${MODEL}_${N}.sdf --model-name=${MODEL}_${N} -x ${X} -y ${Y} -z 0.83 -Y ${YAW}

	popd &>/dev/null

}

if [ "$1" == "-h" ] || [ "$1" == "--help" ]
then
	echo "Usage: $0 [-n <num_vehicles>] [-m <vehicle_model>] [-w <world>] [-s <script>]"
	echo "-s flag is used to script spawning vehicles e.g. $0 -s iris:3,plane:2"
	exit 1
fi

while getopts n:m:w:s:t:l: option
do
	case "${option}"
	in
		n) NUM_VEHICLES=${OPTARG};;
		m) VEHICLE_MODEL=${OPTARG};;
		w) WORLD=${OPTARG};;
		s) SCRIPT=${OPTARG};;
		t) TARGET=${OPTARG};;
		l) LABEL=_${OPTARG};;
	esac
done

num_vehicles=${NUM_VEHICLES:=3}
world=${WORLD:=empty}
target=${TARGET:=px4_sitl_default}
vehicle_model=${VEHICLE_MODEL:="iris"}
export PX4_SIM_MODEL=gazebo-classic_${vehicle_model}

echo ${SCRIPT}
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
src_path="$SCRIPT_DIR/../../.."

build_path=${src_path}/build/${target}
mavlink_udp_port=14560
mavlink_tcp_port=4560

echo "killing running instances"
pkill -x px4 || true

sleep 1

source ${src_path}/Tools/simulation/gazebo-classic/setup_gazebo.bash ${src_path} ${src_path}/build/${target}

# To use gazebo_ros ROS2 plugins
if [[ -n "$ROS_VERSION" ]] && [ "$ROS_VERSION" == "2" ]; then
	ros_args="-s libgazebo_ros_init.so -s libgazebo_ros_factory.so"
else
	ros_args=""
fi

echo "Starting gazebo"
gzserver ${src_path}/Tools/simulation/gazebo-classic/sitl_gazebo-classic/worlds/${world}.world --verbose $ros_args &
echo "wating for 3 seconds....."
sleep 3

n=0
if [ -z ${SCRIPT} ]; then
	if [ $num_vehicles -gt 255 ]
	then
		echo "Tried spawning $num_vehicles vehicles. The maximum number of supported vehicles is 255"
		exit 1
	fi

	# while [ $n -lt $num_vehicles ]; do
	# 	# 遍历 "INITIAL_POS" 中的 UAV 坐标
		
	# 	spawn_model ${vehicle_model} $(($n + 1))
	# 	n=$(($n + 1))
	# done
	INITIAL_POS=$(jq -r '.INITIAL_POS' "$JSON_FILE")
	INITIAL_YAW=$(jq -r '.INITIAL_YAW_NED_RAD' "$JSON_FILE")
	
	echo "--------NED INIT POS: $INITIAL_POS"
	echo "--------NED INIT YAW: $INITIAL_YAW"
	# ENU --> NED
	INITIAL_YAW=$(echo "-$INITIAL_YAW + 1.57" | bc)

	# rerange to (-pi, pi]
	PI=3.1415926

	# Check if INITIAL_YAW is greater than PI
	if (( $(echo "$INITIAL_YAW > $PI" | bc -l) )); then
		INITIAL_YAW=$(echo "$INITIAL_YAW - $PI * 1.999" | bc)
	fi

	# Check if INITIAL_YAW is less than -PI
	if (( $(echo "$INITIAL_YAW < -$PI" | bc -l) )); then
		INITIAL_YAW=$(echo "$INITIAL_YAW + $PI * 2" | bc)
	fi
	# INITIAL_YAW=$(echo "$INITIAL_YAW" | awk '{if ($1 > 3.141592653589793) $1 -= 6.283185307179586; if ($1 <= -3.141592653589793) $1 += 6.283185307179586; print $1}')
	echo "--------ENU INIT YAW: $INITIAL_YAW"
	for UAV in $(echo "$INITIAL_POS" | jq -r 'keys[]'); do
			# 提取 UAV 的编号（例如 UAV1 的编号为 1）
			N=$(echo "$UAV" | grep -o '[0-9]*')

			# 获取 X 和 Y 坐标
			X=$(echo "$INITIAL_POS" | jq -r ".${UAV}[1]")
			Y=$(echo "$INITIAL_POS" | jq -r ".${UAV}[0]")
			echo "+++++++initial pos NED is set to ENU"
			echo "SPAWNING UAV$N @ENU X: $X, Y: $Y, YAW: $INITIAL_YAW"
			# 调用 spawn_model 函数
			spawn_model ${vehicle_model} "$N" "$X" "$Y" "$INITIAL_YAW"
	done
else
	IFS=,
	for target in ${SCRIPT}; do
		target="$(echo "$target" | tr -d ' ')" #Remove spaces
		target_vehicle=$(echo $target | cut -f1 -d:)
		target_number=$(echo $target | cut -f2 -d:)
		target_x=$(echo $target | cut -f3 -d:)
		target_y=$(echo $target | cut -f4 -d:)

		if [ $n -gt 255 ]
		then
			echo "Tried spawning $n vehicles. The maximum number of supported vehicles is 255"
			exit 1
		fi

		m=0
		while [ $m -lt ${target_number} ]; do
			export PX4_SIM_MODEL=gazebo-classic_${target_vehicle}
			spawn_model ${target_vehicle}${LABEL} $(($n + 1)) $target_x $target_y
			m=$(($m + 1))
			n=$(($n + 1))
		done
	done

fi
trap "cleanup" SIGINT SIGTERM EXIT

echo "Starting gazebo client"
gzclient
