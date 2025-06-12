// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_ros2_centralized_control:msg/UavCmd.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__STRUCT_H_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/UavCmd in the package drone_ros2_centralized_control.
typedef struct drone_ros2_centralized_control__msg__UavCmd
{
  std_msgs__msg__Header header;
  int32_t id;
  int32_t is_arm;
} drone_ros2_centralized_control__msg__UavCmd;

// Struct for a sequence of drone_ros2_centralized_control__msg__UavCmd.
typedef struct drone_ros2_centralized_control__msg__UavCmd__Sequence
{
  drone_ros2_centralized_control__msg__UavCmd * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_ros2_centralized_control__msg__UavCmd__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__STRUCT_H_
