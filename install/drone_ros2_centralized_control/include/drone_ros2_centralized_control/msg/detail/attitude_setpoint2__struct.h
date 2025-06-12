// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_ros2_centralized_control:msg/AttitudeSetpoint2.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__STRUCT_H_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/AttitudeSetpoint2 in the package drone_ros2_centralized_control.
typedef struct drone_ros2_centralized_control__msg__AttitudeSetpoint2
{
  uint64_t timestamp;
  int32_t mode;
  float roll_rate;
  float pitch_rate;
  float yaw_rate;
  float roll_body;
  float pitch_body;
  float yaw_body;
  float yaw_sp_move_rate;
  float q_d[4];
  float thrust_body[3];
  bool reset_integral;
  bool fw_control_yaw_wheel;
} drone_ros2_centralized_control__msg__AttitudeSetpoint2;

// Struct for a sequence of drone_ros2_centralized_control__msg__AttitudeSetpoint2.
typedef struct drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence
{
  drone_ros2_centralized_control__msg__AttitudeSetpoint2 * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__STRUCT_H_
