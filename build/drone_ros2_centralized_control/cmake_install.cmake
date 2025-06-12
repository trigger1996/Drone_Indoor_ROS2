# Install script for directory: /home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/install/drone_ros2_centralized_control")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/rosidl_interfaces" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_index/share/ament_index/resource_index/rosidl_interfaces/drone_ros2_centralized_control")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_c/drone_ros2_centralized_control/" REGEX "/[^/]*\\.h$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/opt/ros/foxy/lib/python3.8/site-packages/ament_package/template/environment_hook/library_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/library_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_generator_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_generator_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_generator_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/libdrone_ros2_centralized_control__rosidl_generator_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_generator_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_generator_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_generator_c.so"
         OLD_RPATH "/opt/ros/foxy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_generator_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_typesupport_fastrtps_c/drone_ros2_centralized_control/" REGEX "/[^/]*\\.cpp$" EXCLUDE)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so"
         OLD_RPATH "/opt/ros/foxy/lib:/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_typesupport_fastrtps_cpp/drone_ros2_centralized_control/" REGEX "/[^/]*\\.cpp$" EXCLUDE)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so"
         OLD_RPATH "/opt/ros/foxy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_fastrtps_cpp.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_typesupport_introspection_c/drone_ros2_centralized_control/" REGEX "/[^/]*\\.h$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so"
         OLD_RPATH "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control:/opt/ros/foxy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_c.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_c.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/libdrone_ros2_centralized_control__rosidl_typesupport_c.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_c.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_c.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_c.so"
         OLD_RPATH "/opt/ros/foxy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_c.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_cpp/drone_ros2_centralized_control/" REGEX "/[^/]*\\.hpp$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_typesupport_introspection_cpp/drone_ros2_centralized_control/" REGEX "/[^/]*\\.hpp$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so"
         OLD_RPATH "/opt/ros/foxy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_introspection_cpp.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so"
         OLD_RPATH "/opt/ros/foxy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__rosidl_typesupport_cpp.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/pythonpath.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/pythonpath.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control/__init__.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(
        COMMAND
        "/usr/bin/python3" "-m" "compileall"
        "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/install/drone_ros2_centralized_control/lib/python3.8/site-packages/drone_ros2_centralized_control/__init__.py"
      )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/msg" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control/msg/" REGEX "/[^/]*\\.py$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so"
         OLD_RPATH "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control:/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control:/opt/ros/foxy/lib:/opt/ros/foxy/share/std_msgs/cmake/../../../lib:/opt/ros/foxy/share/builtin_interfaces/cmake/../../../lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_fastrtps_c.cpython-38-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/drone_ros2_centralized_control__rosidl_typesupport_fastrtps_c__pyext.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so"
         OLD_RPATH "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control:/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control:/opt/ros/foxy/lib:/opt/ros/foxy/share/std_msgs/cmake/../../../lib:/opt/ros/foxy/share/builtin_interfaces/cmake/../../../lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_introspection_c.cpython-38-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/drone_ros2_centralized_control__rosidl_typesupport_introspection_c__pyext.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so"
         OLD_RPATH "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control:/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control:/opt/ros/foxy/lib:/opt/ros/foxy/share/std_msgs/cmake/../../../lib:/opt/ros/foxy/share/builtin_interfaces/cmake/../../../lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/drone_ros2_centralized_control/drone_ros2_centralized_control_s__rosidl_typesupport_c.cpython-38-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/drone_ros2_centralized_control__rosidl_typesupport_c__pyext.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__python.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__python.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__python.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_generator_py/drone_ros2_centralized_control/libdrone_ros2_centralized_control__python.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__python.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__python.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__python.so"
         OLD_RPATH "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control:/opt/ros/foxy/share/std_msgs/cmake/../../../lib:/opt/ros/foxy/share/builtin_interfaces/cmake/../../../lib:/opt/ros/foxy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdrone_ros2_centralized_control__python.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/msg" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_adapter/drone_ros2_centralized_control/msg/UavCmd.idl")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/msg" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_adapter/drone_ros2_centralized_control/msg/UavState.idl")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/msg" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_adapter/drone_ros2_centralized_control/msg/AttitudeSetpoint2.idl")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/msg" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/msg/UavCmd.msg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/msg" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/msg/UavState.msg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/msg" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/msg/AttitudeSetpoint2.msg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/drone_ros2_centralized_control" TYPE PROGRAM FILES
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/example/multiple_uav_ctrl.py"
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/example/multiple_uav_waypts.py"
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/gazebo_sim/gazebo_px4_relay.py"
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/user/mdp/mdp_20250506_single_agent_main.py"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/drone_ros2_centralized_control/utils2" TYPE PROGRAM FILES
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/utils2/functions.py"
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/utils2/PID.py"
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/utils2/vis.py"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/model")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/launch")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/drone_ros2_centralized_control" TYPE DIRECTORY FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/src/MDP_Planner" FILES_MATCHING REGEX "/[^/]*\\.py$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/drone_ros2_centralized_control")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/drone_ros2_centralized_control")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/opt/ros/foxy/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/opt/ros/foxy/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/environment" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_index/share/ament_index/resource_index/packages/drone_ros2_centralized_control")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cExport.cmake"
         "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_generator_cExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_generator_cExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_generator_cExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cExport.cmake"
         "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_introspection_cExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_introspection_cExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_introspection_cExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cExport.cmake"
         "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_cExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_cExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_cExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cppExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cppExport.cmake"
         "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_generator_cppExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cppExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_generator_cppExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_generator_cppExport.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cppExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cppExport.cmake"
         "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_introspection_cppExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cppExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_introspection_cppExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_introspection_cppExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_introspection_cppExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cppExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cppExport.cmake"
         "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_cppExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cppExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake/drone_ros2_centralized_control__rosidl_typesupport_cppExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_cppExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/CMakeFiles/Export/7d0b2c58adc6f0cfc9fbff63be3a21e7/drone_ros2_centralized_control__rosidl_typesupport_cppExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_cmake/rosidl_cmake-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_export_dependencies/ament_cmake_export_dependencies-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_export_libraries/ament_cmake_export_libraries-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_export_targets/ament_cmake_export_targets-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_export_include_directories/ament_cmake_export_include_directories-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_cmake/rosidl_cmake_export_typesupport_libraries-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/rosidl_cmake/rosidl_cmake_export_typesupport_targets-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control/cmake" TYPE FILE FILES
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_core/drone_ros2_centralized_controlConfig.cmake"
    "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/ament_cmake_core/drone_ros2_centralized_controlConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drone_ros2_centralized_control" TYPE FILE FILES "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/drone_ros2_centralized_control__py/cmake_install.cmake")

endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/ywzheng/px4_ros_ws/src/drone_ros2_centralized_control/build/drone_ros2_centralized_control/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
