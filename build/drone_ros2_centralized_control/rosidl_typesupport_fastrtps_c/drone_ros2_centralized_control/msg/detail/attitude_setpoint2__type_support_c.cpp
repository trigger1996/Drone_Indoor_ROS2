// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from drone_ros2_centralized_control:msg/AttitudeSetpoint2.idl
// generated code does not contain a copyright notice
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "drone_ros2_centralized_control/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__struct.h"
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__functions.h"
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


// forward declare type support functions


using _AttitudeSetpoint2__ros_msg_type = drone_ros2_centralized_control__msg__AttitudeSetpoint2;

static bool _AttitudeSetpoint2__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AttitudeSetpoint2__ros_msg_type * ros_message = static_cast<const _AttitudeSetpoint2__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr << ros_message->timestamp;
  }

  // Field name: mode
  {
    cdr << ros_message->mode;
  }

  // Field name: roll_rate
  {
    cdr << ros_message->roll_rate;
  }

  // Field name: pitch_rate
  {
    cdr << ros_message->pitch_rate;
  }

  // Field name: yaw_rate
  {
    cdr << ros_message->yaw_rate;
  }

  // Field name: roll_body
  {
    cdr << ros_message->roll_body;
  }

  // Field name: pitch_body
  {
    cdr << ros_message->pitch_body;
  }

  // Field name: yaw_body
  {
    cdr << ros_message->yaw_body;
  }

  // Field name: yaw_sp_move_rate
  {
    cdr << ros_message->yaw_sp_move_rate;
  }

  // Field name: q_d
  {
    size_t size = 4;
    auto array_ptr = ros_message->q_d;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: thrust_body
  {
    size_t size = 3;
    auto array_ptr = ros_message->thrust_body;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: reset_integral
  {
    cdr << (ros_message->reset_integral ? true : false);
  }

  // Field name: fw_control_yaw_wheel
  {
    cdr << (ros_message->fw_control_yaw_wheel ? true : false);
  }

  return true;
}

static bool _AttitudeSetpoint2__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AttitudeSetpoint2__ros_msg_type * ros_message = static_cast<_AttitudeSetpoint2__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr >> ros_message->timestamp;
  }

  // Field name: mode
  {
    cdr >> ros_message->mode;
  }

  // Field name: roll_rate
  {
    cdr >> ros_message->roll_rate;
  }

  // Field name: pitch_rate
  {
    cdr >> ros_message->pitch_rate;
  }

  // Field name: yaw_rate
  {
    cdr >> ros_message->yaw_rate;
  }

  // Field name: roll_body
  {
    cdr >> ros_message->roll_body;
  }

  // Field name: pitch_body
  {
    cdr >> ros_message->pitch_body;
  }

  // Field name: yaw_body
  {
    cdr >> ros_message->yaw_body;
  }

  // Field name: yaw_sp_move_rate
  {
    cdr >> ros_message->yaw_sp_move_rate;
  }

  // Field name: q_d
  {
    size_t size = 4;
    auto array_ptr = ros_message->q_d;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: thrust_body
  {
    size_t size = 3;
    auto array_ptr = ros_message->thrust_body;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: reset_integral
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->reset_integral = tmp ? true : false;
  }

  // Field name: fw_control_yaw_wheel
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->fw_control_yaw_wheel = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_ros2_centralized_control
size_t get_serialized_size_drone_ros2_centralized_control__msg__AttitudeSetpoint2(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AttitudeSetpoint2__ros_msg_type * ros_message = static_cast<const _AttitudeSetpoint2__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name timestamp
  {
    size_t item_size = sizeof(ros_message->timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name mode
  {
    size_t item_size = sizeof(ros_message->mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name roll_rate
  {
    size_t item_size = sizeof(ros_message->roll_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pitch_rate
  {
    size_t item_size = sizeof(ros_message->pitch_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw_rate
  {
    size_t item_size = sizeof(ros_message->yaw_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name roll_body
  {
    size_t item_size = sizeof(ros_message->roll_body);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pitch_body
  {
    size_t item_size = sizeof(ros_message->pitch_body);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw_body
  {
    size_t item_size = sizeof(ros_message->yaw_body);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw_sp_move_rate
  {
    size_t item_size = sizeof(ros_message->yaw_sp_move_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name q_d
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->q_d;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name thrust_body
  {
    size_t array_size = 3;
    auto array_ptr = ros_message->thrust_body;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name reset_integral
  {
    size_t item_size = sizeof(ros_message->reset_integral);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fw_control_yaw_wheel
  {
    size_t item_size = sizeof(ros_message->fw_control_yaw_wheel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AttitudeSetpoint2__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_drone_ros2_centralized_control__msg__AttitudeSetpoint2(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_ros2_centralized_control
size_t max_serialized_size_drone_ros2_centralized_control__msg__AttitudeSetpoint2(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: timestamp
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: roll_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pitch_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: yaw_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: roll_body
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pitch_body
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: yaw_body
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: yaw_sp_move_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: q_d
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: thrust_body
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: reset_integral
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: fw_control_yaw_wheel
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _AttitudeSetpoint2__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_drone_ros2_centralized_control__msg__AttitudeSetpoint2(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_AttitudeSetpoint2 = {
  "drone_ros2_centralized_control::msg",
  "AttitudeSetpoint2",
  _AttitudeSetpoint2__cdr_serialize,
  _AttitudeSetpoint2__cdr_deserialize,
  _AttitudeSetpoint2__get_serialized_size,
  _AttitudeSetpoint2__max_serialized_size
};

static rosidl_message_type_support_t _AttitudeSetpoint2__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AttitudeSetpoint2,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, drone_ros2_centralized_control, msg, AttitudeSetpoint2)() {
  return &_AttitudeSetpoint2__type_support;
}

#if defined(__cplusplus)
}
#endif
