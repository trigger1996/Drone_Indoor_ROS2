// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__BUILDER_HPP_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__BUILDER_HPP_

#include "drone_ros2_centralized_control/msg/detail/uav_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace drone_ros2_centralized_control
{

namespace msg
{

namespace builder
{

class Init_UavState_dead_reckoning
{
public:
  explicit Init_UavState_dead_reckoning(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  ::drone_ros2_centralized_control::msg::UavState dead_reckoning(::drone_ros2_centralized_control::msg::UavState::_dead_reckoning_type arg)
  {
    msg_.dead_reckoning = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_terrain_alt_valid
{
public:
  explicit Init_UavState_terrain_alt_valid(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_dead_reckoning terrain_alt_valid(::drone_ros2_centralized_control::msg::UavState::_terrain_alt_valid_type arg)
  {
    msg_.terrain_alt_valid = std::move(arg);
    return Init_UavState_dead_reckoning(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_terrain_alt
{
public:
  explicit Init_UavState_terrain_alt(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_terrain_alt_valid terrain_alt(::drone_ros2_centralized_control::msg::UavState::_terrain_alt_type arg)
  {
    msg_.terrain_alt = std::move(arg);
    return Init_UavState_terrain_alt_valid(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_epv
{
public:
  explicit Init_UavState_epv(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_terrain_alt epv(::drone_ros2_centralized_control::msg::UavState::_epv_type arg)
  {
    msg_.epv = std::move(arg);
    return Init_UavState_terrain_alt(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_eph
{
public:
  explicit Init_UavState_eph(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_epv eph(::drone_ros2_centralized_control::msg::UavState::_eph_type arg)
  {
    msg_.eph = std::move(arg);
    return Init_UavState_epv(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_alt
{
public:
  explicit Init_UavState_alt(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_eph alt(::drone_ros2_centralized_control::msg::UavState::_alt_type arg)
  {
    msg_.alt = std::move(arg);
    return Init_UavState_eph(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_lon
{
public:
  explicit Init_UavState_lon(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_alt lon(::drone_ros2_centralized_control::msg::UavState::_lon_type arg)
  {
    msg_.lon = std::move(arg);
    return Init_UavState_alt(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_lat
{
public:
  explicit Init_UavState_lat(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_lon lat(::drone_ros2_centralized_control::msg::UavState::_lat_type arg)
  {
    msg_.lat = std::move(arg);
    return Init_UavState_lon(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_heading_good_for_control
{
public:
  explicit Init_UavState_heading_good_for_control(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_lat heading_good_for_control(::drone_ros2_centralized_control::msg::UavState::_heading_good_for_control_type arg)
  {
    msg_.heading_good_for_control = std::move(arg);
    return Init_UavState_lat(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_delta_heading
{
public:
  explicit Init_UavState_delta_heading(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_heading_good_for_control delta_heading(::drone_ros2_centralized_control::msg::UavState::_delta_heading_type arg)
  {
    msg_.delta_heading = std::move(arg);
    return Init_UavState_heading_good_for_control(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_heading
{
public:
  explicit Init_UavState_heading(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_delta_heading heading(::drone_ros2_centralized_control::msg::UavState::_heading_type arg)
  {
    msg_.heading = std::move(arg);
    return Init_UavState_delta_heading(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_az
{
public:
  explicit Init_UavState_az(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_heading az(::drone_ros2_centralized_control::msg::UavState::_az_type arg)
  {
    msg_.az = std::move(arg);
    return Init_UavState_heading(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_ay
{
public:
  explicit Init_UavState_ay(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_az ay(::drone_ros2_centralized_control::msg::UavState::_ay_type arg)
  {
    msg_.ay = std::move(arg);
    return Init_UavState_az(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_ax
{
public:
  explicit Init_UavState_ax(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_ay ax(::drone_ros2_centralized_control::msg::UavState::_ax_type arg)
  {
    msg_.ax = std::move(arg);
    return Init_UavState_ay(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_vz
{
public:
  explicit Init_UavState_vz(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_ax vz(::drone_ros2_centralized_control::msg::UavState::_vz_type arg)
  {
    msg_.vz = std::move(arg);
    return Init_UavState_ax(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_vy
{
public:
  explicit Init_UavState_vy(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_vz vy(::drone_ros2_centralized_control::msg::UavState::_vy_type arg)
  {
    msg_.vy = std::move(arg);
    return Init_UavState_vz(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_vx
{
public:
  explicit Init_UavState_vx(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_vy vx(::drone_ros2_centralized_control::msg::UavState::_vx_type arg)
  {
    msg_.vx = std::move(arg);
    return Init_UavState_vy(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_z
{
public:
  explicit Init_UavState_z(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_vx z(::drone_ros2_centralized_control::msg::UavState::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_UavState_vx(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_y
{
public:
  explicit Init_UavState_y(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_z y(::drone_ros2_centralized_control::msg::UavState::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_UavState_z(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_x
{
public:
  explicit Init_UavState_x(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_y x(::drone_ros2_centralized_control::msg::UavState::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_UavState_y(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_v_z_valid
{
public:
  explicit Init_UavState_v_z_valid(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_x v_z_valid(::drone_ros2_centralized_control::msg::UavState::_v_z_valid_type arg)
  {
    msg_.v_z_valid = std::move(arg);
    return Init_UavState_x(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_v_xy_valid
{
public:
  explicit Init_UavState_v_xy_valid(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_v_z_valid v_xy_valid(::drone_ros2_centralized_control::msg::UavState::_v_xy_valid_type arg)
  {
    msg_.v_xy_valid = std::move(arg);
    return Init_UavState_v_z_valid(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_z_valid
{
public:
  explicit Init_UavState_z_valid(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_v_xy_valid z_valid(::drone_ros2_centralized_control::msg::UavState::_z_valid_type arg)
  {
    msg_.z_valid = std::move(arg);
    return Init_UavState_v_xy_valid(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_xy_valid
{
public:
  explicit Init_UavState_xy_valid(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_z_valid xy_valid(::drone_ros2_centralized_control::msg::UavState::_xy_valid_type arg)
  {
    msg_.xy_valid = std::move(arg);
    return Init_UavState_z_valid(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_gyro_clipping
{
public:
  explicit Init_UavState_gyro_clipping(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_xy_valid gyro_clipping(::drone_ros2_centralized_control::msg::UavState::_gyro_clipping_type arg)
  {
    msg_.gyro_clipping = std::move(arg);
    return Init_UavState_xy_valid(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_accelerometer_clipping
{
public:
  explicit Init_UavState_accelerometer_clipping(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_gyro_clipping accelerometer_clipping(::drone_ros2_centralized_control::msg::UavState::_accelerometer_clipping_type arg)
  {
    msg_.accelerometer_clipping = std::move(arg);
    return Init_UavState_gyro_clipping(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_accelerometer_integral_dt
{
public:
  explicit Init_UavState_accelerometer_integral_dt(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_accelerometer_clipping accelerometer_integral_dt(::drone_ros2_centralized_control::msg::UavState::_accelerometer_integral_dt_type arg)
  {
    msg_.accelerometer_integral_dt = std::move(arg);
    return Init_UavState_accelerometer_clipping(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_accelerometer_m_s2
{
public:
  explicit Init_UavState_accelerometer_m_s2(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_accelerometer_integral_dt accelerometer_m_s2(::drone_ros2_centralized_control::msg::UavState::_accelerometer_m_s2_type arg)
  {
    msg_.accelerometer_m_s2 = std::move(arg);
    return Init_UavState_accelerometer_integral_dt(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_accelerometer_timestamp_relative
{
public:
  explicit Init_UavState_accelerometer_timestamp_relative(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_accelerometer_m_s2 accelerometer_timestamp_relative(::drone_ros2_centralized_control::msg::UavState::_accelerometer_timestamp_relative_type arg)
  {
    msg_.accelerometer_timestamp_relative = std::move(arg);
    return Init_UavState_accelerometer_m_s2(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_gyro_integral_dt
{
public:
  explicit Init_UavState_gyro_integral_dt(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_accelerometer_timestamp_relative gyro_integral_dt(::drone_ros2_centralized_control::msg::UavState::_gyro_integral_dt_type arg)
  {
    msg_.gyro_integral_dt = std::move(arg);
    return Init_UavState_accelerometer_timestamp_relative(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_gyro_rad
{
public:
  explicit Init_UavState_gyro_rad(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_gyro_integral_dt gyro_rad(::drone_ros2_centralized_control::msg::UavState::_gyro_rad_type arg)
  {
    msg_.gyro_rad = std::move(arg);
    return Init_UavState_gyro_integral_dt(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_q
{
public:
  explicit Init_UavState_q(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_gyro_rad q(::drone_ros2_centralized_control::msg::UavState::_q_type arg)
  {
    msg_.q = std::move(arg);
    return Init_UavState_gyro_rad(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_bat_remaining
{
public:
  explicit Init_UavState_bat_remaining(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_q bat_remaining(::drone_ros2_centralized_control::msg::UavState::_bat_remaining_type arg)
  {
    msg_.bat_remaining = std::move(arg);
    return Init_UavState_q(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_bat_voltage
{
public:
  explicit Init_UavState_bat_voltage(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_bat_remaining bat_voltage(::drone_ros2_centralized_control::msg::UavState::_bat_voltage_type arg)
  {
    msg_.bat_voltage = std::move(arg);
    return Init_UavState_bat_remaining(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_is_armed
{
public:
  explicit Init_UavState_is_armed(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_bat_voltage is_armed(::drone_ros2_centralized_control::msg::UavState::_is_armed_type arg)
  {
    msg_.is_armed = std::move(arg);
    return Init_UavState_bat_voltage(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_connected
{
public:
  explicit Init_UavState_connected(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_is_armed connected(::drone_ros2_centralized_control::msg::UavState::_connected_type arg)
  {
    msg_.connected = std::move(arg);
    return Init_UavState_is_armed(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_system_status
{
public:
  explicit Init_UavState_system_status(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_connected system_status(::drone_ros2_centralized_control::msg::UavState::_system_status_type arg)
  {
    msg_.system_status = std::move(arg);
    return Init_UavState_connected(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_custom_mode
{
public:
  explicit Init_UavState_custom_mode(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_system_status custom_mode(::drone_ros2_centralized_control::msg::UavState::_custom_mode_type arg)
  {
    msg_.custom_mode = std::move(arg);
    return Init_UavState_system_status(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_base_mode
{
public:
  explicit Init_UavState_base_mode(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_custom_mode base_mode(::drone_ros2_centralized_control::msg::UavState::_base_mode_type arg)
  {
    msg_.base_mode = std::move(arg);
    return Init_UavState_custom_mode(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_autopilot
{
public:
  explicit Init_UavState_autopilot(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_base_mode autopilot(::drone_ros2_centralized_control::msg::UavState::_autopilot_type arg)
  {
    msg_.autopilot = std::move(arg);
    return Init_UavState_base_mode(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_mavtype
{
public:
  explicit Init_UavState_mavtype(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_autopilot mavtype(::drone_ros2_centralized_control::msg::UavState::_mavtype_type arg)
  {
    msg_.mavtype = std::move(arg);
    return Init_UavState_autopilot(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_id
{
public:
  explicit Init_UavState_id(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_mavtype id(::drone_ros2_centralized_control::msg::UavState::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_UavState_mavtype(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_timestamp
{
public:
  explicit Init_UavState_timestamp(::drone_ros2_centralized_control::msg::UavState & msg)
  : msg_(msg)
  {}
  Init_UavState_id timestamp(::drone_ros2_centralized_control::msg::UavState::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_UavState_id(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

class Init_UavState_header
{
public:
  Init_UavState_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UavState_timestamp header(::drone_ros2_centralized_control::msg::UavState::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_UavState_timestamp(msg_);
  }

private:
  ::drone_ros2_centralized_control::msg::UavState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_ros2_centralized_control::msg::UavState>()
{
  return drone_ros2_centralized_control::msg::builder::Init_UavState_header();
}

}  // namespace drone_ros2_centralized_control

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__BUILDER_HPP_
