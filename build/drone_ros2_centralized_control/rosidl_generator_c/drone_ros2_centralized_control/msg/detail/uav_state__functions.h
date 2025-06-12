// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__FUNCTIONS_H_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "drone_ros2_centralized_control/msg/rosidl_generator_c__visibility_control.h"

#include "drone_ros2_centralized_control/msg/detail/uav_state__struct.h"

/// Initialize msg/UavState message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * drone_ros2_centralized_control__msg__UavState
 * )) before or use
 * drone_ros2_centralized_control__msg__UavState__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
bool
drone_ros2_centralized_control__msg__UavState__init(drone_ros2_centralized_control__msg__UavState * msg);

/// Finalize msg/UavState message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
void
drone_ros2_centralized_control__msg__UavState__fini(drone_ros2_centralized_control__msg__UavState * msg);

/// Create msg/UavState message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * drone_ros2_centralized_control__msg__UavState__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
drone_ros2_centralized_control__msg__UavState *
drone_ros2_centralized_control__msg__UavState__create();

/// Destroy msg/UavState message.
/**
 * It calls
 * drone_ros2_centralized_control__msg__UavState__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
void
drone_ros2_centralized_control__msg__UavState__destroy(drone_ros2_centralized_control__msg__UavState * msg);

/// Check for msg/UavState message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
bool
drone_ros2_centralized_control__msg__UavState__are_equal(const drone_ros2_centralized_control__msg__UavState * lhs, const drone_ros2_centralized_control__msg__UavState * rhs);

/// Copy a msg/UavState message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
bool
drone_ros2_centralized_control__msg__UavState__copy(
  const drone_ros2_centralized_control__msg__UavState * input,
  drone_ros2_centralized_control__msg__UavState * output);

/// Initialize array of msg/UavState messages.
/**
 * It allocates the memory for the number of elements and calls
 * drone_ros2_centralized_control__msg__UavState__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
bool
drone_ros2_centralized_control__msg__UavState__Sequence__init(drone_ros2_centralized_control__msg__UavState__Sequence * array, size_t size);

/// Finalize array of msg/UavState messages.
/**
 * It calls
 * drone_ros2_centralized_control__msg__UavState__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
void
drone_ros2_centralized_control__msg__UavState__Sequence__fini(drone_ros2_centralized_control__msg__UavState__Sequence * array);

/// Create array of msg/UavState messages.
/**
 * It allocates the memory for the array and calls
 * drone_ros2_centralized_control__msg__UavState__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
drone_ros2_centralized_control__msg__UavState__Sequence *
drone_ros2_centralized_control__msg__UavState__Sequence__create(size_t size);

/// Destroy array of msg/UavState messages.
/**
 * It calls
 * drone_ros2_centralized_control__msg__UavState__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
void
drone_ros2_centralized_control__msg__UavState__Sequence__destroy(drone_ros2_centralized_control__msg__UavState__Sequence * array);

/// Check for msg/UavState message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
bool
drone_ros2_centralized_control__msg__UavState__Sequence__are_equal(const drone_ros2_centralized_control__msg__UavState__Sequence * lhs, const drone_ros2_centralized_control__msg__UavState__Sequence * rhs);

/// Copy an array of msg/UavState messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_ros2_centralized_control
bool
drone_ros2_centralized_control__msg__UavState__Sequence__copy(
  const drone_ros2_centralized_control__msg__UavState__Sequence * input,
  drone_ros2_centralized_control__msg__UavState__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_STATE__FUNCTIONS_H_
