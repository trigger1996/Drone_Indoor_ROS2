// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__TRAITS_HPP_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__TRAITS_HPP_

#include "drone_ros2_centralized_control/msg/detail/uav_state__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<drone_ros2_centralized_control::msg::UavState>()
{
  return "drone_ros2_centralized_control::msg::UavState";
}

template<>
inline const char * name<drone_ros2_centralized_control::msg::UavState>()
{
  return "drone_ros2_centralized_control/msg/UavState";
}

template<>
struct has_fixed_size<drone_ros2_centralized_control::msg::UavState>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<drone_ros2_centralized_control::msg::UavState>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<drone_ros2_centralized_control::msg::UavState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__TRAITS_HPP_
