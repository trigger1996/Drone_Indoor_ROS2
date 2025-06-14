// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from drone_ros2_centralized_control:msg/UavCmd.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "drone_ros2_centralized_control/msg/detail/uav_cmd__rosidl_typesupport_introspection_c.h"
#include "drone_ros2_centralized_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "drone_ros2_centralized_control/msg/detail/uav_cmd__functions.h"
#include "drone_ros2_centralized_control/msg/detail/uav_cmd__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void UavCmd__rosidl_typesupport_introspection_c__UavCmd_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  drone_ros2_centralized_control__msg__UavCmd__init(message_memory);
}

void UavCmd__rosidl_typesupport_introspection_c__UavCmd_fini_function(void * message_memory)
{
  drone_ros2_centralized_control__msg__UavCmd__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__UavCmd, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__UavCmd, id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "is_arm",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_ros2_centralized_control__msg__UavCmd, is_arm),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_members = {
  "drone_ros2_centralized_control__msg",  // message namespace
  "UavCmd",  // message name
  3,  // number of fields
  sizeof(drone_ros2_centralized_control__msg__UavCmd),
  UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_member_array,  // message members
  UavCmd__rosidl_typesupport_introspection_c__UavCmd_init_function,  // function to initialize message memory (memory has to be allocated)
  UavCmd__rosidl_typesupport_introspection_c__UavCmd_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_type_support_handle = {
  0,
  &UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_drone_ros2_centralized_control
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drone_ros2_centralized_control, msg, UavCmd)() {
  UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_type_support_handle.typesupport_identifier) {
    UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &UavCmd__rosidl_typesupport_introspection_c__UavCmd_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
