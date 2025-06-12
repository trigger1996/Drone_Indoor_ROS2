// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__STRUCT_HPP_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__drone_ros2_centralized_control__msg__UavState __attribute__((deprecated))
#else
# define DEPRECATED__drone_ros2_centralized_control__msg__UavState __declspec(deprecated)
#endif

namespace drone_ros2_centralized_control
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct UavState_
{
  using Type = UavState_<ContainerAllocator>;

  explicit UavState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->id = 0l;
      this->mavtype = 0l;
      this->autopilot = 0l;
      this->base_mode = 0l;
      this->custom_mode = 0l;
      this->system_status = 0l;
      this->connected = 0l;
      this->is_armed = 0;
      this->bat_voltage = 0.0f;
      this->bat_remaining = 0.0f;
      std::fill<typename std::array<float, 4>::iterator, float>(this->q.begin(), this->q.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->gyro_rad.begin(), this->gyro_rad.end(), 0.0f);
      this->gyro_integral_dt = 0ul;
      this->accelerometer_timestamp_relative = 0l;
      std::fill<typename std::array<float, 3>::iterator, float>(this->accelerometer_m_s2.begin(), this->accelerometer_m_s2.end(), 0.0f);
      this->accelerometer_integral_dt = 0ul;
      this->accelerometer_clipping = 0;
      this->gyro_clipping = 0;
      this->xy_valid = false;
      this->z_valid = false;
      this->v_xy_valid = false;
      this->v_z_valid = false;
      this->x = 0.0f;
      this->y = 0.0f;
      this->z = 0.0f;
      this->vx = 0.0f;
      this->vy = 0.0f;
      this->vz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->heading = 0.0f;
      this->delta_heading = 0.0f;
      this->heading_good_for_control = false;
      this->lat = 0.0;
      this->lon = 0.0;
      this->alt = 0.0f;
      this->eph = 0.0f;
      this->epv = 0.0f;
      this->terrain_alt = 0.0f;
      this->terrain_alt_valid = false;
      this->dead_reckoning = false;
    }
  }

  explicit UavState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    q(_alloc),
    gyro_rad(_alloc),
    accelerometer_m_s2(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->id = 0l;
      this->mavtype = 0l;
      this->autopilot = 0l;
      this->base_mode = 0l;
      this->custom_mode = 0l;
      this->system_status = 0l;
      this->connected = 0l;
      this->is_armed = 0;
      this->bat_voltage = 0.0f;
      this->bat_remaining = 0.0f;
      std::fill<typename std::array<float, 4>::iterator, float>(this->q.begin(), this->q.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->gyro_rad.begin(), this->gyro_rad.end(), 0.0f);
      this->gyro_integral_dt = 0ul;
      this->accelerometer_timestamp_relative = 0l;
      std::fill<typename std::array<float, 3>::iterator, float>(this->accelerometer_m_s2.begin(), this->accelerometer_m_s2.end(), 0.0f);
      this->accelerometer_integral_dt = 0ul;
      this->accelerometer_clipping = 0;
      this->gyro_clipping = 0;
      this->xy_valid = false;
      this->z_valid = false;
      this->v_xy_valid = false;
      this->v_z_valid = false;
      this->x = 0.0f;
      this->y = 0.0f;
      this->z = 0.0f;
      this->vx = 0.0f;
      this->vy = 0.0f;
      this->vz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->heading = 0.0f;
      this->delta_heading = 0.0f;
      this->heading_good_for_control = false;
      this->lat = 0.0;
      this->lon = 0.0;
      this->alt = 0.0f;
      this->eph = 0.0f;
      this->epv = 0.0f;
      this->terrain_alt = 0.0f;
      this->terrain_alt_valid = false;
      this->dead_reckoning = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _id_type =
    int32_t;
  _id_type id;
  using _mavtype_type =
    int32_t;
  _mavtype_type mavtype;
  using _autopilot_type =
    int32_t;
  _autopilot_type autopilot;
  using _base_mode_type =
    int32_t;
  _base_mode_type base_mode;
  using _custom_mode_type =
    int32_t;
  _custom_mode_type custom_mode;
  using _system_status_type =
    int32_t;
  _system_status_type system_status;
  using _connected_type =
    int32_t;
  _connected_type connected;
  using _is_armed_type =
    int8_t;
  _is_armed_type is_armed;
  using _bat_voltage_type =
    float;
  _bat_voltage_type bat_voltage;
  using _bat_remaining_type =
    float;
  _bat_remaining_type bat_remaining;
  using _q_type =
    std::array<float, 4>;
  _q_type q;
  using _gyro_rad_type =
    std::array<float, 3>;
  _gyro_rad_type gyro_rad;
  using _gyro_integral_dt_type =
    uint32_t;
  _gyro_integral_dt_type gyro_integral_dt;
  using _accelerometer_timestamp_relative_type =
    int32_t;
  _accelerometer_timestamp_relative_type accelerometer_timestamp_relative;
  using _accelerometer_m_s2_type =
    std::array<float, 3>;
  _accelerometer_m_s2_type accelerometer_m_s2;
  using _accelerometer_integral_dt_type =
    uint32_t;
  _accelerometer_integral_dt_type accelerometer_integral_dt;
  using _accelerometer_clipping_type =
    uint8_t;
  _accelerometer_clipping_type accelerometer_clipping;
  using _gyro_clipping_type =
    uint8_t;
  _gyro_clipping_type gyro_clipping;
  using _xy_valid_type =
    bool;
  _xy_valid_type xy_valid;
  using _z_valid_type =
    bool;
  _z_valid_type z_valid;
  using _v_xy_valid_type =
    bool;
  _v_xy_valid_type v_xy_valid;
  using _v_z_valid_type =
    bool;
  _v_z_valid_type v_z_valid;
  using _x_type =
    float;
  _x_type x;
  using _y_type =
    float;
  _y_type y;
  using _z_type =
    float;
  _z_type z;
  using _vx_type =
    float;
  _vx_type vx;
  using _vy_type =
    float;
  _vy_type vy;
  using _vz_type =
    float;
  _vz_type vz;
  using _ax_type =
    float;
  _ax_type ax;
  using _ay_type =
    float;
  _ay_type ay;
  using _az_type =
    float;
  _az_type az;
  using _heading_type =
    float;
  _heading_type heading;
  using _delta_heading_type =
    float;
  _delta_heading_type delta_heading;
  using _heading_good_for_control_type =
    bool;
  _heading_good_for_control_type heading_good_for_control;
  using _lat_type =
    double;
  _lat_type lat;
  using _lon_type =
    double;
  _lon_type lon;
  using _alt_type =
    float;
  _alt_type alt;
  using _eph_type =
    float;
  _eph_type eph;
  using _epv_type =
    float;
  _epv_type epv;
  using _terrain_alt_type =
    float;
  _terrain_alt_type terrain_alt;
  using _terrain_alt_valid_type =
    bool;
  _terrain_alt_valid_type terrain_alt_valid;
  using _dead_reckoning_type =
    bool;
  _dead_reckoning_type dead_reckoning;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__id(
    const int32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__mavtype(
    const int32_t & _arg)
  {
    this->mavtype = _arg;
    return *this;
  }
  Type & set__autopilot(
    const int32_t & _arg)
  {
    this->autopilot = _arg;
    return *this;
  }
  Type & set__base_mode(
    const int32_t & _arg)
  {
    this->base_mode = _arg;
    return *this;
  }
  Type & set__custom_mode(
    const int32_t & _arg)
  {
    this->custom_mode = _arg;
    return *this;
  }
  Type & set__system_status(
    const int32_t & _arg)
  {
    this->system_status = _arg;
    return *this;
  }
  Type & set__connected(
    const int32_t & _arg)
  {
    this->connected = _arg;
    return *this;
  }
  Type & set__is_armed(
    const int8_t & _arg)
  {
    this->is_armed = _arg;
    return *this;
  }
  Type & set__bat_voltage(
    const float & _arg)
  {
    this->bat_voltage = _arg;
    return *this;
  }
  Type & set__bat_remaining(
    const float & _arg)
  {
    this->bat_remaining = _arg;
    return *this;
  }
  Type & set__q(
    const std::array<float, 4> & _arg)
  {
    this->q = _arg;
    return *this;
  }
  Type & set__gyro_rad(
    const std::array<float, 3> & _arg)
  {
    this->gyro_rad = _arg;
    return *this;
  }
  Type & set__gyro_integral_dt(
    const uint32_t & _arg)
  {
    this->gyro_integral_dt = _arg;
    return *this;
  }
  Type & set__accelerometer_timestamp_relative(
    const int32_t & _arg)
  {
    this->accelerometer_timestamp_relative = _arg;
    return *this;
  }
  Type & set__accelerometer_m_s2(
    const std::array<float, 3> & _arg)
  {
    this->accelerometer_m_s2 = _arg;
    return *this;
  }
  Type & set__accelerometer_integral_dt(
    const uint32_t & _arg)
  {
    this->accelerometer_integral_dt = _arg;
    return *this;
  }
  Type & set__accelerometer_clipping(
    const uint8_t & _arg)
  {
    this->accelerometer_clipping = _arg;
    return *this;
  }
  Type & set__gyro_clipping(
    const uint8_t & _arg)
  {
    this->gyro_clipping = _arg;
    return *this;
  }
  Type & set__xy_valid(
    const bool & _arg)
  {
    this->xy_valid = _arg;
    return *this;
  }
  Type & set__z_valid(
    const bool & _arg)
  {
    this->z_valid = _arg;
    return *this;
  }
  Type & set__v_xy_valid(
    const bool & _arg)
  {
    this->v_xy_valid = _arg;
    return *this;
  }
  Type & set__v_z_valid(
    const bool & _arg)
  {
    this->v_z_valid = _arg;
    return *this;
  }
  Type & set__x(
    const float & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const float & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const float & _arg)
  {
    this->z = _arg;
    return *this;
  }
  Type & set__vx(
    const float & _arg)
  {
    this->vx = _arg;
    return *this;
  }
  Type & set__vy(
    const float & _arg)
  {
    this->vy = _arg;
    return *this;
  }
  Type & set__vz(
    const float & _arg)
  {
    this->vz = _arg;
    return *this;
  }
  Type & set__ax(
    const float & _arg)
  {
    this->ax = _arg;
    return *this;
  }
  Type & set__ay(
    const float & _arg)
  {
    this->ay = _arg;
    return *this;
  }
  Type & set__az(
    const float & _arg)
  {
    this->az = _arg;
    return *this;
  }
  Type & set__heading(
    const float & _arg)
  {
    this->heading = _arg;
    return *this;
  }
  Type & set__delta_heading(
    const float & _arg)
  {
    this->delta_heading = _arg;
    return *this;
  }
  Type & set__heading_good_for_control(
    const bool & _arg)
  {
    this->heading_good_for_control = _arg;
    return *this;
  }
  Type & set__lat(
    const double & _arg)
  {
    this->lat = _arg;
    return *this;
  }
  Type & set__lon(
    const double & _arg)
  {
    this->lon = _arg;
    return *this;
  }
  Type & set__alt(
    const float & _arg)
  {
    this->alt = _arg;
    return *this;
  }
  Type & set__eph(
    const float & _arg)
  {
    this->eph = _arg;
    return *this;
  }
  Type & set__epv(
    const float & _arg)
  {
    this->epv = _arg;
    return *this;
  }
  Type & set__terrain_alt(
    const float & _arg)
  {
    this->terrain_alt = _arg;
    return *this;
  }
  Type & set__terrain_alt_valid(
    const bool & _arg)
  {
    this->terrain_alt_valid = _arg;
    return *this;
  }
  Type & set__dead_reckoning(
    const bool & _arg)
  {
    this->dead_reckoning = _arg;
    return *this;
  }

  // constant declarations
  static constexpr int32_t RELATIVE_TIMESTAMP_INVALID =
    2147483647;
  static constexpr uint8_t CLIPPING_X =
    1u;
  static constexpr uint8_t CLIPPING_Y =
    2u;
  static constexpr uint8_t CLIPPING_Z =
    4u;

  // pointer types
  using RawPtr =
    drone_ros2_centralized_control::msg::UavState_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_ros2_centralized_control::msg::UavState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_ros2_centralized_control::msg::UavState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_ros2_centralized_control::msg::UavState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_ros2_centralized_control__msg__UavState
    std::shared_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_ros2_centralized_control__msg__UavState
    std::shared_ptr<drone_ros2_centralized_control::msg::UavState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UavState_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    if (this->mavtype != other.mavtype) {
      return false;
    }
    if (this->autopilot != other.autopilot) {
      return false;
    }
    if (this->base_mode != other.base_mode) {
      return false;
    }
    if (this->custom_mode != other.custom_mode) {
      return false;
    }
    if (this->system_status != other.system_status) {
      return false;
    }
    if (this->connected != other.connected) {
      return false;
    }
    if (this->is_armed != other.is_armed) {
      return false;
    }
    if (this->bat_voltage != other.bat_voltage) {
      return false;
    }
    if (this->bat_remaining != other.bat_remaining) {
      return false;
    }
    if (this->q != other.q) {
      return false;
    }
    if (this->gyro_rad != other.gyro_rad) {
      return false;
    }
    if (this->gyro_integral_dt != other.gyro_integral_dt) {
      return false;
    }
    if (this->accelerometer_timestamp_relative != other.accelerometer_timestamp_relative) {
      return false;
    }
    if (this->accelerometer_m_s2 != other.accelerometer_m_s2) {
      return false;
    }
    if (this->accelerometer_integral_dt != other.accelerometer_integral_dt) {
      return false;
    }
    if (this->accelerometer_clipping != other.accelerometer_clipping) {
      return false;
    }
    if (this->gyro_clipping != other.gyro_clipping) {
      return false;
    }
    if (this->xy_valid != other.xy_valid) {
      return false;
    }
    if (this->z_valid != other.z_valid) {
      return false;
    }
    if (this->v_xy_valid != other.v_xy_valid) {
      return false;
    }
    if (this->v_z_valid != other.v_z_valid) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    if (this->vx != other.vx) {
      return false;
    }
    if (this->vy != other.vy) {
      return false;
    }
    if (this->vz != other.vz) {
      return false;
    }
    if (this->ax != other.ax) {
      return false;
    }
    if (this->ay != other.ay) {
      return false;
    }
    if (this->az != other.az) {
      return false;
    }
    if (this->heading != other.heading) {
      return false;
    }
    if (this->delta_heading != other.delta_heading) {
      return false;
    }
    if (this->heading_good_for_control != other.heading_good_for_control) {
      return false;
    }
    if (this->lat != other.lat) {
      return false;
    }
    if (this->lon != other.lon) {
      return false;
    }
    if (this->alt != other.alt) {
      return false;
    }
    if (this->eph != other.eph) {
      return false;
    }
    if (this->epv != other.epv) {
      return false;
    }
    if (this->terrain_alt != other.terrain_alt) {
      return false;
    }
    if (this->terrain_alt_valid != other.terrain_alt_valid) {
      return false;
    }
    if (this->dead_reckoning != other.dead_reckoning) {
      return false;
    }
    return true;
  }
  bool operator!=(const UavState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UavState_

// alias to use template instance with default allocator
using UavState =
  drone_ros2_centralized_control::msg::UavState_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr int32_t UavState_<ContainerAllocator>::RELATIVE_TIMESTAMP_INVALID;
template<typename ContainerAllocator>
constexpr uint8_t UavState_<ContainerAllocator>::CLIPPING_X;
template<typename ContainerAllocator>
constexpr uint8_t UavState_<ContainerAllocator>::CLIPPING_Y;
template<typename ContainerAllocator>
constexpr uint8_t UavState_<ContainerAllocator>::CLIPPING_Z;

}  // namespace msg

}  // namespace drone_ros2_centralized_control

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__STRUCT_HPP_
