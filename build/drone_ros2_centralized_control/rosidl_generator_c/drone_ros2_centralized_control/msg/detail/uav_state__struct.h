// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__STRUCT_H_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'RELATIVE_TIMESTAMP_INVALID'.
enum
{
  drone_ros2_centralized_control__msg__UavState__RELATIVE_TIMESTAMP_INVALID = 2147483647l
};

/// Constant 'CLIPPING_X'.
enum
{
  drone_ros2_centralized_control__msg__UavState__CLIPPING_X = 1
};

/// Constant 'CLIPPING_Y'.
enum
{
  drone_ros2_centralized_control__msg__UavState__CLIPPING_Y = 2
};

/// Constant 'CLIPPING_Z'.
enum
{
  drone_ros2_centralized_control__msg__UavState__CLIPPING_Z = 4
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/UavState in the package drone_ros2_centralized_control.
typedef struct drone_ros2_centralized_control__msg__UavState
{
  std_msgs__msg__Header header;
  uint64_t timestamp;
  int32_t id;
  int32_t mavtype;
  int32_t autopilot;
  int32_t base_mode;
  int32_t custom_mode;
  int32_t system_status;
  int32_t connected;
  int8_t is_armed;
  float bat_voltage;
  float bat_remaining;
  float q[4];
  float gyro_rad[3];
  uint32_t gyro_integral_dt;
  int32_t accelerometer_timestamp_relative;
  float accelerometer_m_s2[3];
  uint32_t accelerometer_integral_dt;
  uint8_t accelerometer_clipping;
  uint8_t gyro_clipping;
  bool xy_valid;
  bool z_valid;
  bool v_xy_valid;
  bool v_z_valid;
  float x;
  float y;
  float z;
  float vx;
  float vy;
  float vz;
  float ax;
  float ay;
  float az;
  float heading;
  float delta_heading;
  bool heading_good_for_control;
  double lat;
  double lon;
  float alt;
  float eph;
  float epv;
  float terrain_alt;
  bool terrain_alt_valid;
  bool dead_reckoning;
} drone_ros2_centralized_control__msg__UavState;

// Struct for a sequence of drone_ros2_centralized_control__msg__UavState.
typedef struct drone_ros2_centralized_control__msg__UavState__Sequence
{
  drone_ros2_centralized_control__msg__UavState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_ros2_centralized_control__msg__UavState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__STRUCT_H_
