// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice
#include "drone_ros2_centralized_control/msg/detail/uav_state__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "drone_ros2_centralized_control/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "drone_ros2_centralized_control/msg/detail/uav_state__struct.h"
#include "drone_ros2_centralized_control/msg/detail/uav_state__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_drone_ros2_centralized_control
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_drone_ros2_centralized_control
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_drone_ros2_centralized_control
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _UavState__ros_msg_type = drone_ros2_centralized_control__msg__UavState;

static bool _UavState__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _UavState__ros_msg_type * ros_message = static_cast<const _UavState__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->header, cdr))
    {
      return false;
    }
  }

  // Field name: timestamp
  {
    cdr << ros_message->timestamp;
  }

  // Field name: id
  {
    cdr << ros_message->id;
  }

  // Field name: mavtype
  {
    cdr << ros_message->mavtype;
  }

  // Field name: autopilot
  {
    cdr << ros_message->autopilot;
  }

  // Field name: base_mode
  {
    cdr << ros_message->base_mode;
  }

  // Field name: custom_mode
  {
    cdr << ros_message->custom_mode;
  }

  // Field name: system_status
  {
    cdr << ros_message->system_status;
  }

  // Field name: connected
  {
    cdr << ros_message->connected;
  }

  // Field name: is_armed
  {
    cdr << ros_message->is_armed;
  }

  // Field name: bat_voltage
  {
    cdr << ros_message->bat_voltage;
  }

  // Field name: bat_remaining
  {
    cdr << ros_message->bat_remaining;
  }

  // Field name: q
  {
    size_t size = 4;
    auto array_ptr = ros_message->q;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: gyro_rad
  {
    size_t size = 3;
    auto array_ptr = ros_message->gyro_rad;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: gyro_integral_dt
  {
    cdr << ros_message->gyro_integral_dt;
  }

  // Field name: accelerometer_timestamp_relative
  {
    cdr << ros_message->accelerometer_timestamp_relative;
  }

  // Field name: accelerometer_m_s2
  {
    size_t size = 3;
    auto array_ptr = ros_message->accelerometer_m_s2;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: accelerometer_integral_dt
  {
    cdr << ros_message->accelerometer_integral_dt;
  }

  // Field name: accelerometer_clipping
  {
    cdr << ros_message->accelerometer_clipping;
  }

  // Field name: gyro_clipping
  {
    cdr << ros_message->gyro_clipping;
  }

  // Field name: xy_valid
  {
    cdr << (ros_message->xy_valid ? true : false);
  }

  // Field name: z_valid
  {
    cdr << (ros_message->z_valid ? true : false);
  }

  // Field name: v_xy_valid
  {
    cdr << (ros_message->v_xy_valid ? true : false);
  }

  // Field name: v_z_valid
  {
    cdr << (ros_message->v_z_valid ? true : false);
  }

  // Field name: x
  {
    cdr << ros_message->x;
  }

  // Field name: y
  {
    cdr << ros_message->y;
  }

  // Field name: z
  {
    cdr << ros_message->z;
  }

  // Field name: vx
  {
    cdr << ros_message->vx;
  }

  // Field name: vy
  {
    cdr << ros_message->vy;
  }

  // Field name: vz
  {
    cdr << ros_message->vz;
  }

  // Field name: ax
  {
    cdr << ros_message->ax;
  }

  // Field name: ay
  {
    cdr << ros_message->ay;
  }

  // Field name: az
  {
    cdr << ros_message->az;
  }

  // Field name: heading
  {
    cdr << ros_message->heading;
  }

  // Field name: delta_heading
  {
    cdr << ros_message->delta_heading;
  }

  // Field name: heading_good_for_control
  {
    cdr << (ros_message->heading_good_for_control ? true : false);
  }

  // Field name: lat
  {
    cdr << ros_message->lat;
  }

  // Field name: lon
  {
    cdr << ros_message->lon;
  }

  // Field name: alt
  {
    cdr << ros_message->alt;
  }

  // Field name: eph
  {
    cdr << ros_message->eph;
  }

  // Field name: epv
  {
    cdr << ros_message->epv;
  }

  // Field name: terrain_alt
  {
    cdr << ros_message->terrain_alt;
  }

  // Field name: terrain_alt_valid
  {
    cdr << (ros_message->terrain_alt_valid ? true : false);
  }

  // Field name: dead_reckoning
  {
    cdr << (ros_message->dead_reckoning ? true : false);
  }

  return true;
}

static bool _UavState__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _UavState__ros_msg_type * ros_message = static_cast<_UavState__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->header))
    {
      return false;
    }
  }

  // Field name: timestamp
  {
    cdr >> ros_message->timestamp;
  }

  // Field name: id
  {
    cdr >> ros_message->id;
  }

  // Field name: mavtype
  {
    cdr >> ros_message->mavtype;
  }

  // Field name: autopilot
  {
    cdr >> ros_message->autopilot;
  }

  // Field name: base_mode
  {
    cdr >> ros_message->base_mode;
  }

  // Field name: custom_mode
  {
    cdr >> ros_message->custom_mode;
  }

  // Field name: system_status
  {
    cdr >> ros_message->system_status;
  }

  // Field name: connected
  {
    cdr >> ros_message->connected;
  }

  // Field name: is_armed
  {
    cdr >> ros_message->is_armed;
  }

  // Field name: bat_voltage
  {
    cdr >> ros_message->bat_voltage;
  }

  // Field name: bat_remaining
  {
    cdr >> ros_message->bat_remaining;
  }

  // Field name: q
  {
    size_t size = 4;
    auto array_ptr = ros_message->q;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: gyro_rad
  {
    size_t size = 3;
    auto array_ptr = ros_message->gyro_rad;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: gyro_integral_dt
  {
    cdr >> ros_message->gyro_integral_dt;
  }

  // Field name: accelerometer_timestamp_relative
  {
    cdr >> ros_message->accelerometer_timestamp_relative;
  }

  // Field name: accelerometer_m_s2
  {
    size_t size = 3;
    auto array_ptr = ros_message->accelerometer_m_s2;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: accelerometer_integral_dt
  {
    cdr >> ros_message->accelerometer_integral_dt;
  }

  // Field name: accelerometer_clipping
  {
    cdr >> ros_message->accelerometer_clipping;
  }

  // Field name: gyro_clipping
  {
    cdr >> ros_message->gyro_clipping;
  }

  // Field name: xy_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->xy_valid = tmp ? true : false;
  }

  // Field name: z_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->z_valid = tmp ? true : false;
  }

  // Field name: v_xy_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->v_xy_valid = tmp ? true : false;
  }

  // Field name: v_z_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->v_z_valid = tmp ? true : false;
  }

  // Field name: x
  {
    cdr >> ros_message->x;
  }

  // Field name: y
  {
    cdr >> ros_message->y;
  }

  // Field name: z
  {
    cdr >> ros_message->z;
  }

  // Field name: vx
  {
    cdr >> ros_message->vx;
  }

  // Field name: vy
  {
    cdr >> ros_message->vy;
  }

  // Field name: vz
  {
    cdr >> ros_message->vz;
  }

  // Field name: ax
  {
    cdr >> ros_message->ax;
  }

  // Field name: ay
  {
    cdr >> ros_message->ay;
  }

  // Field name: az
  {
    cdr >> ros_message->az;
  }

  // Field name: heading
  {
    cdr >> ros_message->heading;
  }

  // Field name: delta_heading
  {
    cdr >> ros_message->delta_heading;
  }

  // Field name: heading_good_for_control
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->heading_good_for_control = tmp ? true : false;
  }

  // Field name: lat
  {
    cdr >> ros_message->lat;
  }

  // Field name: lon
  {
    cdr >> ros_message->lon;
  }

  // Field name: alt
  {
    cdr >> ros_message->alt;
  }

  // Field name: eph
  {
    cdr >> ros_message->eph;
  }

  // Field name: epv
  {
    cdr >> ros_message->epv;
  }

  // Field name: terrain_alt
  {
    cdr >> ros_message->terrain_alt;
  }

  // Field name: terrain_alt_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->terrain_alt_valid = tmp ? true : false;
  }

  // Field name: dead_reckoning
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->dead_reckoning = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_ros2_centralized_control
size_t get_serialized_size_drone_ros2_centralized_control__msg__UavState(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _UavState__ros_msg_type * ros_message = static_cast<const _UavState__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name timestamp
  {
    size_t item_size = sizeof(ros_message->timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name id
  {
    size_t item_size = sizeof(ros_message->id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name mavtype
  {
    size_t item_size = sizeof(ros_message->mavtype);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name autopilot
  {
    size_t item_size = sizeof(ros_message->autopilot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name base_mode
  {
    size_t item_size = sizeof(ros_message->base_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name custom_mode
  {
    size_t item_size = sizeof(ros_message->custom_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name system_status
  {
    size_t item_size = sizeof(ros_message->system_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name connected
  {
    size_t item_size = sizeof(ros_message->connected);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name is_armed
  {
    size_t item_size = sizeof(ros_message->is_armed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name bat_voltage
  {
    size_t item_size = sizeof(ros_message->bat_voltage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name bat_remaining
  {
    size_t item_size = sizeof(ros_message->bat_remaining);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name q
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->q;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gyro_rad
  {
    size_t array_size = 3;
    auto array_ptr = ros_message->gyro_rad;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gyro_integral_dt
  {
    size_t item_size = sizeof(ros_message->gyro_integral_dt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name accelerometer_timestamp_relative
  {
    size_t item_size = sizeof(ros_message->accelerometer_timestamp_relative);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name accelerometer_m_s2
  {
    size_t array_size = 3;
    auto array_ptr = ros_message->accelerometer_m_s2;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name accelerometer_integral_dt
  {
    size_t item_size = sizeof(ros_message->accelerometer_integral_dt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name accelerometer_clipping
  {
    size_t item_size = sizeof(ros_message->accelerometer_clipping);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gyro_clipping
  {
    size_t item_size = sizeof(ros_message->gyro_clipping);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name xy_valid
  {
    size_t item_size = sizeof(ros_message->xy_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name z_valid
  {
    size_t item_size = sizeof(ros_message->z_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name v_xy_valid
  {
    size_t item_size = sizeof(ros_message->v_xy_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name v_z_valid
  {
    size_t item_size = sizeof(ros_message->v_z_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name x
  {
    size_t item_size = sizeof(ros_message->x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y
  {
    size_t item_size = sizeof(ros_message->y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name z
  {
    size_t item_size = sizeof(ros_message->z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vx
  {
    size_t item_size = sizeof(ros_message->vx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vy
  {
    size_t item_size = sizeof(ros_message->vy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vz
  {
    size_t item_size = sizeof(ros_message->vz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ax
  {
    size_t item_size = sizeof(ros_message->ax);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ay
  {
    size_t item_size = sizeof(ros_message->ay);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name az
  {
    size_t item_size = sizeof(ros_message->az);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name heading
  {
    size_t item_size = sizeof(ros_message->heading);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name delta_heading
  {
    size_t item_size = sizeof(ros_message->delta_heading);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name heading_good_for_control
  {
    size_t item_size = sizeof(ros_message->heading_good_for_control);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lat
  {
    size_t item_size = sizeof(ros_message->lat);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lon
  {
    size_t item_size = sizeof(ros_message->lon);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name alt
  {
    size_t item_size = sizeof(ros_message->alt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name eph
  {
    size_t item_size = sizeof(ros_message->eph);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name epv
  {
    size_t item_size = sizeof(ros_message->epv);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name terrain_alt
  {
    size_t item_size = sizeof(ros_message->terrain_alt);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name terrain_alt_valid
  {
    size_t item_size = sizeof(ros_message->terrain_alt_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dead_reckoning
  {
    size_t item_size = sizeof(ros_message->dead_reckoning);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _UavState__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_drone_ros2_centralized_control__msg__UavState(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_ros2_centralized_control
size_t max_serialized_size_drone_ros2_centralized_control__msg__UavState(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: header
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__Header(
        full_bounded, current_alignment);
    }
  }
  // member: timestamp
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: mavtype
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: autopilot
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: base_mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: custom_mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: system_status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: connected
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: is_armed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: bat_voltage
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: bat_remaining
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: q
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: gyro_rad
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: gyro_integral_dt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: accelerometer_timestamp_relative
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: accelerometer_m_s2
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: accelerometer_integral_dt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: accelerometer_clipping
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: gyro_clipping
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: xy_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: z_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: v_xy_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: v_z_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: z
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vx
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ax
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ay
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: az
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: heading
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: delta_heading
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: heading_good_for_control
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: lat
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: lon
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: alt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: eph
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: epv
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: terrain_alt
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: terrain_alt_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: dead_reckoning
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _UavState__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_drone_ros2_centralized_control__msg__UavState(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_UavState = {
  "drone_ros2_centralized_control::msg",
  "UavState",
  _UavState__cdr_serialize,
  _UavState__cdr_deserialize,
  _UavState__get_serialized_size,
  _UavState__max_serialized_size
};

static rosidl_message_type_support_t _UavState__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_UavState,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, drone_ros2_centralized_control, msg, UavState)() {
  return &_UavState__type_support;
}

#if defined(__cplusplus)
}
#endif
