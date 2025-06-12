// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drone_ros2_centralized_control:msg/UavCmd.idl
// generated code does not contain a copyright notice
#include "drone_ros2_centralized_control/msg/detail/uav_cmd__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
drone_ros2_centralized_control__msg__UavCmd__init(drone_ros2_centralized_control__msg__UavCmd * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    drone_ros2_centralized_control__msg__UavCmd__fini(msg);
    return false;
  }
  // id
  // is_arm
  return true;
}

void
drone_ros2_centralized_control__msg__UavCmd__fini(drone_ros2_centralized_control__msg__UavCmd * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // id
  // is_arm
}

bool
drone_ros2_centralized_control__msg__UavCmd__are_equal(const drone_ros2_centralized_control__msg__UavCmd * lhs, const drone_ros2_centralized_control__msg__UavCmd * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // is_arm
  if (lhs->is_arm != rhs->is_arm) {
    return false;
  }
  return true;
}

bool
drone_ros2_centralized_control__msg__UavCmd__copy(
  const drone_ros2_centralized_control__msg__UavCmd * input,
  drone_ros2_centralized_control__msg__UavCmd * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // id
  output->id = input->id;
  // is_arm
  output->is_arm = input->is_arm;
  return true;
}

drone_ros2_centralized_control__msg__UavCmd *
drone_ros2_centralized_control__msg__UavCmd__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__UavCmd * msg = (drone_ros2_centralized_control__msg__UavCmd *)allocator.allocate(sizeof(drone_ros2_centralized_control__msg__UavCmd), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drone_ros2_centralized_control__msg__UavCmd));
  bool success = drone_ros2_centralized_control__msg__UavCmd__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drone_ros2_centralized_control__msg__UavCmd__destroy(drone_ros2_centralized_control__msg__UavCmd * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drone_ros2_centralized_control__msg__UavCmd__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drone_ros2_centralized_control__msg__UavCmd__Sequence__init(drone_ros2_centralized_control__msg__UavCmd__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__UavCmd * data = NULL;

  if (size) {
    data = (drone_ros2_centralized_control__msg__UavCmd *)allocator.zero_allocate(size, sizeof(drone_ros2_centralized_control__msg__UavCmd), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drone_ros2_centralized_control__msg__UavCmd__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drone_ros2_centralized_control__msg__UavCmd__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
drone_ros2_centralized_control__msg__UavCmd__Sequence__fini(drone_ros2_centralized_control__msg__UavCmd__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      drone_ros2_centralized_control__msg__UavCmd__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

drone_ros2_centralized_control__msg__UavCmd__Sequence *
drone_ros2_centralized_control__msg__UavCmd__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__UavCmd__Sequence * array = (drone_ros2_centralized_control__msg__UavCmd__Sequence *)allocator.allocate(sizeof(drone_ros2_centralized_control__msg__UavCmd__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drone_ros2_centralized_control__msg__UavCmd__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drone_ros2_centralized_control__msg__UavCmd__Sequence__destroy(drone_ros2_centralized_control__msg__UavCmd__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drone_ros2_centralized_control__msg__UavCmd__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drone_ros2_centralized_control__msg__UavCmd__Sequence__are_equal(const drone_ros2_centralized_control__msg__UavCmd__Sequence * lhs, const drone_ros2_centralized_control__msg__UavCmd__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drone_ros2_centralized_control__msg__UavCmd__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drone_ros2_centralized_control__msg__UavCmd__Sequence__copy(
  const drone_ros2_centralized_control__msg__UavCmd__Sequence * input,
  drone_ros2_centralized_control__msg__UavCmd__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drone_ros2_centralized_control__msg__UavCmd);
    drone_ros2_centralized_control__msg__UavCmd * data =
      (drone_ros2_centralized_control__msg__UavCmd *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drone_ros2_centralized_control__msg__UavCmd__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          drone_ros2_centralized_control__msg__UavCmd__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!drone_ros2_centralized_control__msg__UavCmd__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
