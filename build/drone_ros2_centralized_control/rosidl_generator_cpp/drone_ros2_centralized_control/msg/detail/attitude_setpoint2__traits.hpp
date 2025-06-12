// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from drone_ros2_centralized_control:msg/AttitudeSetpoint2.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__TRAITS_HPP_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__TRAITS_HPP_

#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<drone_ros2_centralized_control::msg::AttitudeSetpoint2>()
{
  return "drone_ros2_centralized_control::msg::AttitudeSetpoint2";
}

template<>
inline const char * name<drone_ros2_centralized_control::msg::AttitudeSetpoint2>()
{
  return "drone_ros2_centralized_control/msg/AttitudeSetpoint2";
}

template<>
struct has_fixed_size<drone_ros2_centralized_control::msg::AttitudeSetpoint2>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<drone_ros2_centralized_control::msg::AttitudeSetpoint2>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<drone_ros2_centralized_control::msg::AttitudeSetpoint2>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__TRAITS_HPP_
