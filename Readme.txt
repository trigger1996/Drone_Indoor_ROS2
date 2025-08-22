#
# THIS IS FOR REAL DRONES!
#
# Step 1
roslaunch vrpn_client_ros sample_test_200.launch                                # initialize vrpn
#
# Step 2
roslaunch network_interface droneyee_vrpn_swarm_mocapCarsCopters.launch         # vrpn -> ros
#
# Step 3
cd zt_ws/
source devel/setup.bash
rosrun drone_ros_centeralized_control MavRouter_standard_ROS_2_0.py             # ros -> mavlink
#
# Step 4
# run examples, or OTHER ros nodes to send target velocities
rosrun drone_ros_centeralized_control mdp_planner_0506_single_agent.py

#
# processes on OUR drones
ssh cat@192.168.151.20x
#
See drone_ros_centeralized_control/__move_to_onboard_computer/droneyee_adapter/readme_how_to_use to enable mavlink-router


# installation
git clone https://github.com/trigger1996/Drone_Indoor_ROS2
mv ./Drone_Indoor_ROS2/ ./drone_ros_centeralized_control/
cd drone_ros_centeralized_control/
git checkout ros1