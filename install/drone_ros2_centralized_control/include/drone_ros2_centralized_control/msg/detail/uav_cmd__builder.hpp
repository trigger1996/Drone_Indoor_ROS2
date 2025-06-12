// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_ros2_centralized_control:msg/UavCmd.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__BUILDER_HPP_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__BUILDER_HPP_

#include "drone_ros2_centralized_control/msg/detail/uav_cmd__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace drone_ros2_centralized_control
{

namespace msg
{

namespace builder
{

class Init_UavCmd_is_arm
{
public:
  explicit Init_UavCmd_is_arm(::drone_ros2_centralized_control::msg::UavCmd & msg)
  : msg_(msg)
  {}
  ::drone_ros2_centralized_control::msg::UavCmd is_arm(::drone_ros2_centralized_control::msg::UavCmd::_is_arm_type arg)
  {
    msg_.is_arm = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavCmd msg_;
};

class Init_UavCmd_id
{
public:
  explicit Init_UavCmd_id(::drone_ros2_centralized_control::msg::UavCmd & msg)
  : msg_(msg)
  {}
  Init_UavCmd_is_arm id(::drone_ros2_centralized_control::msg::UavCmd::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_UavCmd_is_arm(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavCmd msg_;
};

class Init_UavCmd_header
{
public:
  Init_UavCmd_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UavCmd_id header(::drone_ros2_centralized_control::msg::UavCmd::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_UavCmd_id(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavCmd msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_ros2_centralized_control::msg::UavCmd>()
{
  return drone_ros2_centralized_control::msg::builder::Init_UavCmd_header();
}

}  // namespace drone_ros2_centralized_control

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__BUILDER_HPP_
