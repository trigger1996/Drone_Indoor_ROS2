// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from drone_ros2_centralized_control:msg/AttitudeSetpoint2.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__rosidl_typesupport_introspection_c.h"
#include "drone_ros2_centralized_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__functions.h"
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  drone_ros2_centralized_control__msg__AttitudeSetpoint2__init(message_memory);
}

void AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_fini_function(void * message_memory)
{
  drone_ros2_centralized_control__msg__AttitudeSetpoint2__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_member_array[13] = {
  {
    "timestamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, timestamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "roll_rate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, roll_rate),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pitch_rate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, pitch_rate),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yaw_rate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, yaw_rate),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "roll_body",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, roll_body),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pitch_body",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, pitch_body),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yaw_body",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, yaw_body),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yaw_sp_move_rate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, yaw_sp_move_rate),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "q_d",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, q_d),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "thrust_body",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, thrust_body),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "reset_integral",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, reset_integral),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "fw_control_yaw_wheel",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__AttitudeSetpoint2, fw_control_yaw_wheel),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_members = {
  "drone_ros2_centralized_control__msg",  // message namespace
  "AttitudeSetpoint2",  // message name
  13,  // number of fields
  sizeof(drone_ros2_centralized_control__msg__AttitudeSetpoint2),
  AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_member_array,  // message members
  AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_init_function,  // function to initialize message memory (memory has to be allocated)
  AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_type_support_handle = {
  0,
  &AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_drone_ros2_centralized_control
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drone_ros2_centralized_control, msg, AttitudeSetpoint2)() {
  if (!AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_type_support_handle.typesupport_identifier) {
    AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &AttitudeSetpoint2__rosidl_typesupport_introspection_c__AttitudeSetpoint2_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
