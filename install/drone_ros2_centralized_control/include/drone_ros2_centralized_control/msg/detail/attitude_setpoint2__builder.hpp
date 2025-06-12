// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_ros2_centralized_control:msg/AttitudeSetpoint2.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__BUILDER_HPP_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__BUILDER_HPP_

#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace drone_ros2_centralized_control
{

namespace msg
{

namespace builder
{

class Init_AttitudeSetpoint2_fw_control_yaw_wheel
{
public:
  explicit Init_AttitudeSetpoint2_fw_control_yaw_wheel(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 fw_control_yaw_wheel(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_fw_control_yaw_wheel_type arg)
  {
    msg_.fw_control_yaw_wheel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_reset_integral
{
public:
  explicit Init_AttitudeSetpoint2_reset_integral(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_fw_control_yaw_wheel reset_integral(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_reset_integral_type arg)
  {
    msg_.reset_integral = std::move(arg);
    return Init_AttitudeSetpoint2_fw_control_yaw_wheel(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_thrust_body
{
public:
  explicit Init_AttitudeSetpoint2_thrust_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_reset_integral thrust_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_thrust_body_type arg)
  {
    msg_.thrust_body = std::move(arg);
    return Init_AttitudeSetpoint2_reset_integral(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_q_d
{
public:
  explicit Init_AttitudeSetpoint2_q_d(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_thrust_body q_d(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_q_d_type arg)
  {
    msg_.q_d = std::move(arg);
    return Init_AttitudeSetpoint2_thrust_body(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_yaw_sp_move_rate
{
public:
  explicit Init_AttitudeSetpoint2_yaw_sp_move_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_q_d yaw_sp_move_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_yaw_sp_move_rate_type arg)
  {
    msg_.yaw_sp_move_rate = std::move(arg);
    return Init_AttitudeSetpoint2_q_d(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_yaw_body
{
public:
  explicit Init_AttitudeSetpoint2_yaw_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_yaw_sp_move_rate yaw_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_yaw_body_type arg)
  {
    msg_.yaw_body = std::move(arg);
    return Init_AttitudeSetpoint2_yaw_sp_move_rate(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_pitch_body
{
public:
  explicit Init_AttitudeSetpoint2_pitch_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_yaw_body pitch_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_pitch_body_type arg)
  {
    msg_.pitch_body = std::move(arg);
    return Init_AttitudeSetpoint2_yaw_body(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_roll_body
{
public:
  explicit Init_AttitudeSetpoint2_roll_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_pitch_body roll_body(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_roll_body_type arg)
  {
    msg_.roll_body = std::move(arg);
    return Init_AttitudeSetpoint2_pitch_body(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_yaw_rate
{
public:
  explicit Init_AttitudeSetpoint2_yaw_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_roll_body yaw_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_yaw_rate_type arg)
  {
    msg_.yaw_rate = std::move(arg);
    return Init_AttitudeSetpoint2_roll_body(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_pitch_rate
{
public:
  explicit Init_AttitudeSetpoint2_pitch_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_yaw_rate pitch_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_pitch_rate_type arg)
  {
    msg_.pitch_rate = std::move(arg);
    return Init_AttitudeSetpoint2_yaw_rate(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_roll_rate
{
public:
  explicit Init_AttitudeSetpoint2_roll_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_pitch_rate roll_rate(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_roll_rate_type arg)
  {
    msg_.roll_rate = std::move(arg);
    return Init_AttitudeSetpoint2_pitch_rate(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_mode
{
public:
  explicit Init_AttitudeSetpoint2_mode(::drone_ros2_centralized_control::msg::AttitudeSetpoint2 & msg)
  : msg_(msg)
  {}
  Init_AttitudeSetpoint2_roll_rate mode(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return Init_AttitudeSetpoint2_roll_rate(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

class Init_AttitudeSetpoint2_timestamp
{
public:
  Init_AttitudeSetpoint2_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AttitudeSetpoint2_mode timestamp(::drone_ros2_centralized_control::msg::AttitudeSetpoint2::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_AttitudeSetpoint2_mode(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::AttitudeSetpoint2 msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_ros2_centralized_control::msg::AttitudeSetpoint2>()
{
  return drone_ros2_centralized_control::msg::builder::Init_AttitudeSetpoint2_timestamp();
}

}  // namespace drone_ros2_centralized_control

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__ATTITUDE_SETPOINT2__BUILDER_HPP_
