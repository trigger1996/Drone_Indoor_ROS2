cmake_minimum_required(VERSION 3.10)
project(drone_ros2_centralized_control)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rosidl_default_runtime REQUIRED)
find_package(rosidl_typesupport_c REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(px4_msgs REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

set(msg_files
  "msg/UavCmd.msg"
  "msg/UavState.msg"
  "msg/AttitudeSetpoint2.msg"
  DEPENDENCIES std_msgs
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# 安装 Python 脚本（确保文件有执行权限）
install(PROGRAMS
  src/example/multiple_uav_ctrl.py
  src/example/multiple_uav_waypts.py
  src/gazebo_sim/gazebo_px4_relay.py
  #
  src/user/mdp/mdp_20250506_single_agent_main.py
  #
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  src/utils2/functions.py
  src/utils2/PID.py
  src/utils2/vis.py
  DESTINATION lib/${PROJECT_NAME}/utils2
)

install(DIRECTORY model
  DESTINATION share/${PROJECT_NAME}
)

# 安装 launch 文件
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# 安装 Python 子模块 MDP_Planner
install(DIRECTORY src/MDP_Planner
  DESTINATION lib/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.py"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
