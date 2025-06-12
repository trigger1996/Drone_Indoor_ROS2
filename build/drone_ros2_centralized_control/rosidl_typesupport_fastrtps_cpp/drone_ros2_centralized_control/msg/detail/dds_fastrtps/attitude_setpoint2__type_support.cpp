// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from drone_ros2_centralized_control:msg/AttitudeSetpoint2.idl
// generated code does not contain a copyright notice
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__rosidl_typesupport_fastrtps_cpp.hpp"
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__struct.hpp"

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

namespace drone_ros2_centralized_control
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
cdr_serialize(
  const drone_ros2_centralized_control::msg::AttitudeSetpoint2 & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: timestamp
  cdr << ros_message.timestamp;
  // Member: mode
  cdr << ros_message.mode;
  // Member: roll_rate
  cdr << ros_message.roll_rate;
  // Member: pitch_rate
  cdr << ros_message.pitch_rate;
  // Member: yaw_rate
  cdr << ros_message.yaw_rate;
  // Member: roll_body
  cdr << ros_message.roll_body;
  // Member: pitch_body
  cdr << ros_message.pitch_body;
  // Member: yaw_body
  cdr << ros_message.yaw_body;
  // Member: yaw_sp_move_rate
  cdr << ros_message.yaw_sp_move_rate;
  // Member: q_d
  {
    cdr << ros_message.q_d;
  }
  // Member: thrust_body
  {
    cdr << ros_message.thrust_body;
  }
  // Member: reset_integral
  cdr << (ros_message.reset_integral ? true : false);
  // Member: fw_control_yaw_wheel
  cdr << (ros_message.fw_control_yaw_wheel ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  drone_ros2_centralized_control::msg::AttitudeSetpoint2 & ros_message)
{
  // Member: timestamp
  cdr >> ros_message.timestamp;

  // Member: mode
  cdr >> ros_message.mode;

  // Member: roll_rate
  cdr >> ros_message.roll_rate;

  // Member: pitch_rate
  cdr >> ros_message.pitch_rate;

  // Member: yaw_rate
  cdr >> ros_message.yaw_rate;

  // Member: roll_body
  cdr >> ros_message.roll_body;

  // Member: pitch_body
  cdr >> ros_message.pitch_body;

  // Member: yaw_body
  cdr >> ros_message.yaw_body;

  // Member: yaw_sp_move_rate
  cdr >> ros_message.yaw_sp_move_rate;

  // Member: q_d
  {
    cdr >> ros_message.q_d;
  }

  // Member: thrust_body
  {
    cdr >> ros_message.thrust_body;
  }

  // Member: reset_integral
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.reset_integral = tmp ? true : false;
  }

  // Member: fw_control_yaw_wheel
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.fw_control_yaw_wheel = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
get_serialized_size(
  const drone_ros2_centralized_control::msg::AttitudeSetpoint2 & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: timestamp
  {
    size_t item_size = sizeof(ros_message.timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mode
  {
    size_t item_size = sizeof(ros_message.mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: roll_rate
  {
    size_t item_size = sizeof(ros_message.roll_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: pitch_rate
  {
    size_t item_size = sizeof(ros_message.pitch_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: yaw_rate
  {
    size_t item_size = sizeof(ros_message.yaw_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: roll_body
  {
    size_t item_size = sizeof(ros_message.roll_body);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: pitch_body
  {
    size_t item_size = sizeof(ros_message.pitch_body);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: yaw_body
  {
    size_t item_size = sizeof(ros_message.yaw_body);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: yaw_sp_move_rate
  {
    size_t item_size = sizeof(ros_message.yaw_sp_move_rate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: q_d
  {
    size_t array_size = 4;
    size_t item_size = sizeof(ros_message.q_d[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: thrust_body
  {
    size_t array_size = 3;
    size_t item_size = sizeof(ros_message.thrust_body[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: reset_integral
  {
    size_t item_size = sizeof(ros_message.reset_integral);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: fw_control_yaw_wheel
  {
    size_t item_size = sizeof(ros_message.fw_control_yaw_wheel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_drone_ros2_centralized_control
max_serialized_size_AttitudeSetpoint2(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: timestamp
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: roll_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: pitch_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: yaw_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: roll_body
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: pitch_body
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: yaw_body
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: yaw_sp_move_rate
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: q_d
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: thrust_body
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: reset_integral
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: fw_control_yaw_wheel
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _AttitudeSetpoint2__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const drone_ros2_centralized_control::msg::AttitudeSetpoint2 *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _AttitudeSetpoint2__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<drone_ros2_centralized_control::msg::AttitudeSetpoint2 *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _AttitudeSetpoint2__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const drone_ros2_centralized_control::msg::AttitudeSetpoint2 *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _AttitudeSetpoint2__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_AttitudeSetpoint2(full_bounded, 0);
}

static message_type_support_callbacks_t _AttitudeSetpoint2__callbacks = {
  "drone_ros2_centralized_control::msg",
  "AttitudeSetpoint2",
  _AttitudeSetpoint2__cdr_serialize,
  _AttitudeSetpoint2__cdr_deserialize,
  _AttitudeSetpoint2__get_serialized_size,
  _AttitudeSetpoint2__max_serialized_size
};

static rosidl_message_type_support_t _AttitudeSetpoint2__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_AttitudeSetpoint2__callbacks,
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
get_message_type_support_handle<drone_ros2_centralized_control::msg::AttitudeSetpoint2>()
{
  return &drone_ros2_centralized_control::msg::typesupport_fastrtps_cpp::_AttitudeSetpoint2__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, drone_ros2_centralized_control, msg, AttitudeSetpoint2)() {
  return &drone_ros2_centralized_control::msg::typesupport_fastrtps_cpp::_AttitudeSetpoint2__handle;
}

#ifdef __cplusplus
}
#endif
