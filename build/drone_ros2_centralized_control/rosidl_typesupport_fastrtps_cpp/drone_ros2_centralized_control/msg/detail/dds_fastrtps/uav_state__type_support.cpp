// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice
#include "drone_ros2_centralized_control/msg/detail/uav_state__rosidl_typesupport_fastrtps_cpp.hpp"
#include "drone_ros2_centralized_control/msg/detail/uav_state__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::Header &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::Header &);
size_t get_serialized_size(
  const std_msgs::msg::Header &,
  size_t current_alignment);
size_t
max_serialized_size_Header(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs


namespace drone_ros2_centralized_control
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
cdr_serialize(
  const drone_ros2_centralized_control::msg::UavState & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.header,
    cdr);
  // Member: timestamp
  cdr << ros_message.timestamp;
  // Member: id
  cdr << ros_message.id;
  // Member: mavtype
  cdr << ros_message.mavtype;
  // Member: autopilot
  cdr << ros_message.autopilot;
  // Member: base_mode
  cdr << ros_message.base_mode;
  // Member: custom_mode
  cdr << ros_message.custom_mode;
  // Member: system_status
  cdr << ros_message.system_status;
  // Member: connected
  cdr << ros_message.connected;
  // Member: is_armed
  cdr << ros_message.is_armed;
  // Member: bat_voltage
  cdr << ros_message.bat_voltage;
  // Member: bat_remaining
  cdr << ros_message.bat_remaining;
  // Member: q
  {
    cdr << ros_message.q;
  }
  // Member: gyro_rad
  {
    cdr << ros_message.gyro_rad;
  }
  // Member: gyro_integral_dt
  cdr << ros_message.gyro_integral_dt;
  // Member: accelerometer_timestamp_relative
  cdr << ros_message.accelerometer_timestamp_relative;
  // Member: accelerometer_m_s2
  {
    cdr << ros_message.accelerometer_m_s2;
  }
  // Member: accelerometer_integral_dt
  cdr << ros_message.accelerometer_integral_dt;
  // Member: accelerometer_clipping
  cdr << ros_message.accelerometer_clipping;
  // Member: gyro_clipping
  cdr << ros_message.gyro_clipping;
  // Member: xy_valid
  cdr << (ros_message.xy_valid ? true : false);
  // Member: z_valid
  cdr << (ros_message.z_valid ? true : false);
  // Member: v_xy_valid
  cdr << (ros_message.v_xy_valid ? true : false);
  // Member: v_z_valid
  cdr << (ros_message.v_z_valid ? true : false);
  // Member: x
  cdr << ros_message.x;
  // Member: y
  cdr << ros_message.y;
  // Member: z
  cdr << ros_message.z;
  // Member: vx
  cdr << ros_message.vx;
  // Member: vy
  cdr << ros_message.vy;
  // Member: vz
  cdr << ros_message.vz;
  // Member: ax
  cdr << ros_message.ax;
  // Member: ay
  cdr << ros_message.ay;
  // Member: az
  cdr << ros_message.az;
  // Member: heading
  cdr << ros_message.heading;
  // Member: delta_heading
  cdr << ros_message.delta_heading;
  // Member: heading_good_for_control
  cdr << (ros_message.heading_good_for_control ? true : false);
  // Member: lat
  cdr << ros_message.lat;
  // Member: lon
  cdr << ros_message.lon;
  // Member: alt
  cdr << ros_message.alt;
  // Member: eph
  cdr << ros_message.eph;
  // Member: epv
  cdr << ros_message.epv;
  // Member: terrain_alt
  cdr << ros_message.terrain_alt;
  // Member: terrain_alt_valid
  cdr << (ros_message.terrain_alt_valid ? true : false);
  // Member: dead_reckoning
  cdr << (ros_message.dead_reckoning ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  drone_ros2_centralized_control::msg::UavState & ros_message)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.header);

  // Member: timestamp
  cdr >> ros_message.timestamp;

  // Member: id
  cdr >> ros_message.id;

  // Member: mavtype
  cdr >> ros_message.mavtype;

  // Member: autopilot
  cdr >> ros_message.autopilot;

  // Member: base_mode
  cdr >> ros_message.base_mode;

  // Member: custom_mode
  cdr >> ros_message.custom_mode;

  // Member: system_status
  cdr >> ros_message.system_status;

  // Member: connected
  cdr >> ros_message.connected;

  // Member: is_armed
  cdr >> ros_message.is_armed;

  // Member: bat_voltage
  cdr >> ros_message.bat_voltage;

  // Member: bat_remaining
  cdr >> ros_message.bat_remaining;

  // Member: q
  {
    cdr >> ros_message.q;
  }

  // Member: gyro_rad
  {
    cdr >> ros_message.gyro_rad;
  }

  // Member: gyro_integral_dt
  cdr >> ros_message.gyro_integral_dt;

  // Member: accelerometer_timestamp_relative
  cdr >> ros_message.accelerometer_timestamp_relative;

  // Member: accelerometer_m_s2
  {
    cdr >> ros_message.accelerometer_m_s2;
  }

  // Member: accelerometer_integral_dt
  cdr >> ros_message.accelerometer_integral_dt;

  // Member: accelerometer_clipping
  cdr >> ros_message.accelerometer_clipping;

  // Member: gyro_clipping
  cdr >> ros_message.gyro_clipping;

  // Member: xy_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.xy_valid = tmp ? true : false;
  }

  // Member: z_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.z_valid = tmp ? true : false;
  }

  // Member: v_xy_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.v_xy_valid = tmp ? true : false;
  }

  // Member: v_z_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.v_z_valid = tmp ? true : false;
  }

  // Member: x
  cdr >> ros_message.x;

  // Member: y
  cdr >> ros_message.y;

  // Member: z
  cdr >> ros_message.z;

  // Member: vx
  cdr >> ros_message.vx;

  // Member: vy
  cdr >> ros_message.vy;

  // Member: vz
  cdr >> ros_message.vz;

  // Member: ax
  cdr >> ros_message.ax;

  // Member: ay
  cdr >> ros_message.ay;

  // Member: az
  cdr >> ros_message.az;

  // Member: heading
  cdr >> ros_message.heading;

  // Member: delta_heading
  cdr >> ros_message.delta_heading;

  // Member: heading_good_for_control
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.heading_good_for_control = tmp ? true : false;
  }

  // Member: lat
  cdr >> ros_message.lat;

  // Member: lon
  cdr >> ros_message.lon;

  // Member: alt
  cdr >> ros_message.alt;

  // Member: eph
  cdr >> ros_message.eph;

  // Member: epv
  cdr >> ros_message.epv;

  // Member: terrain_alt
  cdr >> ros_message.terrain_alt;

  // Member: terrain_alt_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.terrain_alt_valid = tmp ? true : false;
  }

  // Member: dead_reckoning
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.dead_reckoning = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
get_serialized_size(
  const drone_ros2_centralized_control::msg::UavState & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: header

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.header, current_alignment);
  // Member: timestamp
  {
    size_t item_size = sizeof(ros_message.timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: id
  {
    size_t item_size = sizeof(ros_message.id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mavtype
  {
    size_t item_size = sizeof(ros_message.mavtype);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: autopilot
  {
    size_t item_size = sizeof(ros_message.autopilot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: base_mode
  {
    size_t item_size = sizeof(ros_message.base_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: custom_mode
  {
    size_t item_size = sizeof(ros_message.custom_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: system_status
  {
    size_t item_size = sizeof(ros_message.system_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: connected
  {
    size_t item_size = sizeof(ros_message.connected);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: is_armed
  {
    size_t item_size = sizeof(ros_message.is_armed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bat_voltage
  {
    size_t item_size = sizeof(ros_message.bat_voltage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bat_remaining
  {
    size_t item_size = sizeof(ros_message.bat_remaining);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: q
  {
    size_t array_size = 4;
    size_t item_size = sizeof(ros_message.q[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: gyro_rad
  {
    size_t array_size = 3;
    size_t item_size = sizeof(ros_message.gyro_rad[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: gyro_integral_dt
  {
    size_t item_size = sizeof(ros_message.gyro_integral_dt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: accelerometer_timestamp_relative
  {
    size_t item_size = sizeof(ros_message.accelerometer_timestamp_relative);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: accelerometer_m_s2
  {
    size_t array_size = 3;
    size_t item_size = sizeof(ros_message.accelerometer_m_s2[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: accelerometer_integral_dt
  {
    size_t item_size = sizeof(ros_message.accelerometer_integral_dt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: accelerometer_clipping
  {
    size_t item_size = sizeof(ros_message.accelerometer_clipping);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: gyro_clipping
  {
    size_t item_size = sizeof(ros_message.gyro_clipping);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: xy_valid
  {
    size_t item_size = sizeof(ros_message.xy_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: z_valid
  {
    size_t item_size = sizeof(ros_message.z_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: v_xy_valid
  {
    size_t item_size = sizeof(ros_message.v_xy_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: v_z_valid
  {
    size_t item_size = sizeof(ros_message.v_z_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: x
  {
    size_t item_size = sizeof(ros_message.x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y
  {
    size_t item_size = sizeof(ros_message.y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: z
  {
    size_t item_size = sizeof(ros_message.z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: vx
  {
    size_t item_size = sizeof(ros_message.vx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: vy
  {
    size_t item_size = sizeof(ros_message.vy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: vz
  {
    size_t item_size = sizeof(ros_message.vz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ax
  {
    size_t item_size = sizeof(ros_message.ax);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ay
  {
    size_t item_size = sizeof(ros_message.ay);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: az
  {
    size_t item_size = sizeof(ros_message.az);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: heading
  {
    size_t item_size = sizeof(ros_message.heading);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: delta_heading
  {
    size_t item_size = sizeof(ros_message.delta_heading);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: heading_good_for_control
  {
    size_t item_size = sizeof(ros_message.heading_good_for_control);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lat
  {
    size_t item_size = sizeof(ros_message.lat);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lon
  {
    size_t item_size = sizeof(ros_message.lon);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: alt
  {
    size_t item_size = sizeof(ros_message.alt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: eph
  {
    size_t item_size = sizeof(ros_message.eph);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: epv
  {
    size_t item_size = sizeof(ros_message.epv);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: terrain_alt
  {
    size_t item_size = sizeof(ros_message.terrain_alt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: terrain_alt_valid
  {
    size_t item_size = sizeof(ros_message.terrain_alt_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: dead_reckoning
  {
    size_t item_size = sizeof(ros_message.dead_reckoning);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
max_serialized_size_UavState(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: header
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_Header(
        full_bounded, current_alignment);
    }
  }

  // Member: timestamp
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: mavtype
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: autopilot
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: base_mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: custom_mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: system_status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: connected
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: is_armed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: bat_voltage
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: bat_remaining
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: q
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: gyro_rad
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: gyro_integral_dt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: accelerometer_timestamp_relative
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: accelerometer_m_s2
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: accelerometer_integral_dt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: accelerometer_clipping
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: gyro_clipping
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: xy_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: z_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: v_xy_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: v_z_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: z
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: vx
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: vy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: vz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: ax
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: ay
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: az
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: heading
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: delta_heading
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: heading_good_for_control
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: lat
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: lon
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: alt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: eph
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: epv
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: terrain_alt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: terrain_alt_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: dead_reckoning
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _UavState__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const drone_ros2_centralized_control::msg::UavState *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _UavState__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<drone_ros2_centralized_control::msg::UavState *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _UavState__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const drone_ros2_centralized_control::msg::UavState *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _UavState__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_UavState(full_bounded, 0);
}

static message_type_support_callbacks_t _UavState__callbacks = {
  "drone_ros2_centralized_control::msg",
  "UavState",
  _UavState__cdr_serialize,
  _UavState__cdr_deserialize,
  _UavState__get_serialized_size,
  _UavState__max_serialized_size
};

static rosidl_message_type_support_t _UavState__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_UavState__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace drone_ros2_centralized_control

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_drone_ros2_centralized_control
const rosidl_message_type_support_t *
get_message_type_support_handle<drone_ros2_centralized_control::msg::UavState>()
{
  return &drone_ros2_centralized_control::msg::typesupport_fastrtps_cpp::_UavState__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, drone_ros2_centralized_control, msg, UavState)() {
  return &drone_ros2_centralized_control::msg::typesupport_fastrtps_cpp::_UavState__handle;
}

#ifdef __cplusplus
}
#endif
