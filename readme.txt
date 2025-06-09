#
# https://docs.px4.io/main/en/ros2/offboard_control.html#foxy

#
# STEP 1 
# install px4 ros supports
# 	this application is for udp bridge for new Px4 firmware and Gazebo
#	DO NOT use ros compilations
git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
cd Micro-XRCE-DDS-Agent
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig /usr/local/lib/

	# if the aforementioned process fails, then re-install cmake
	wget https://github.com/Kitware/CMake/releases/download/v3.23.0/cmake-3.23.0-linux-x86_64.tar.gz		# higher version is available at https://github.com/Kitware/CMake/releases
	tar -xzvf cmake-3.23.0-linux-x86_64.tar.gz
	sudo mv cmake-3.23.0-linux-x86_64 /opt/cmake
	sudo ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake
	sudo ln -s /opt/cmake/bin/ctest /usr/local/bin/ctest
	cmake --version

#
# STEP 2 
# establish ROS workspace
mkdir px4_ros_ws
cd px4_ros_ws
mkdir src
colcon build
cd src
git clone https://github.com/PX4/px4_msgs.git
git clone https://github.com/PX4/px4_ros_com.git
source /opt/ros/foxy/setup.bash
source ~/px4_ros_ws/install/setup.bash

#
# STEP 3 
# establish multi-uav simulation
# https://docs.px4.io/main/en/sim_gazebo_classic/multi_vehicle_simulation.html
# Tools/simulation/gazebo-classic/sitl_multiple_run.sh [-m <model>] [-n <number_of_vehicles>] [-w <world>] [-s <script>] [-t <target>] [-l <label>]
# e.g.
# ./Tools/simulation/gazebo-classic/sitl_multiple_run.sh -m iris -n 4
#
# Terminal 1
source ~/src/PX4-Autopilot/Tools/simulation/gazebo-classic/sitl_multiple_run.sh -s "iris:3"
#
# Terminal 2
MicroXRCEAgent udp4 -p 8888
#
# Terminal 3
cd px4_ros_ws/
colcon build									# optional
source install/setup.bash
clear										# optional
# different_examples
ros2 launch drone_ros2_centralized_control example_trajectory_ctrl.launch.py	# 用来展示不同控制模式
ros2 launch drone_ros2_centralized_control example_waypt_ctrl.launch.py	# 面向路点的带有时间约束的控制
