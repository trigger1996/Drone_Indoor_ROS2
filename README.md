# Drone_Indoor_ROS2

### to install
git clone https://github.com/trigger1996/Drone_Indoor_ROS2 ~/px4_ros_ws/src/drone_ros_centerlized_control
cd drone_ros_centerlized_control
git submodule update --init --recursive


### To update submodules
'''
cd robot_libs/librobot
git pull origin main  # 拉取最新内容
cd ../..
git add robot_libs/librobot
git commit -m "Update submodule librobot"
'''

### 
