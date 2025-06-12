// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drone_ros2_centralized_control:msg/AttitudeSetpoint2.idl
// generated code does not contain a copyright notice
#include "drone_ros2_centralized_control/msg/detail/attitude_setpoint2__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
drone_ros2_centralized_control__msg__AttitudeSetpoint2__init(drone_ros2_centralized_control__msg__AttitudeSetpoint2 * msg)
{
  if (!msg) {
    return false;
  }
  // timestamp
  // mode
  // roll_rate
  // pitch_rate
  // yaw_rate
  // roll_body
  // pitch_body
  // yaw_body
  // yaw_sp_move_rate
  // q_d
  // thrust_body
  // reset_integral
  // fw_control_yaw_wheel
  return true;
}

void
drone_ros2_centralized_control__msg__AttitudeSetpoint2__fini(drone_ros2_centralized_control__msg__AttitudeSetpoint2 * msg)
{
  if (!msg) {
    return;
  }
  // timestamp
  // mode
  // roll_rate
  // pitch_rate
  // yaw_rate
  // roll_body
  // pitch_body
  // yaw_body
  // yaw_sp_move_rate
  // q_d
  // thrust_body
  // reset_integral
  // fw_control_yaw_wheel
}

bool
drone_ros2_centralized_control__msg__AttitudeSetpoint2__are_equal(const drone_ros2_centralized_control__msg__AttitudeSetpoint2 * lhs, const drone_ros2_centralized_control__msg__AttitudeSetpoint2 * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  // roll_rate
  if (lhs->roll_rate != rhs->roll_rate) {
    return false;
  }
  // pitch_rate
  if (lhs->pitch_rate != rhs->pitch_rate) {
    return false;
  }
  // yaw_rate
  if (lhs->yaw_rate != rhs->yaw_rate) {
    return false;
  }
  // roll_body
  if (lhs->roll_body != rhs->roll_body) {
    return false;
  }
  // pitch_body
  if (lhs->pitch_body != rhs->pitch_body) {
    return false;
  }
  // yaw_body
  if (lhs->yaw_body != rhs->yaw_body) {
    return false;
  }
  // yaw_sp_move_rate
  if (lhs->yaw_sp_move_rate != rhs->yaw_sp_move_rate) {
    return false;
  }
  // q_d
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->q_d[i] != rhs->q_d[i]) {
      return false;
    }
  }
  // thrust_body
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->thrust_body[i] != rhs->thrust_body[i]) {
      return false;
    }
  }
  // reset_integral
  if (lhs->reset_integral != rhs->reset_integral) {
    return false;
  }
  // fw_control_yaw_wheel
  if (lhs->fw_control_yaw_wheel != rhs->fw_control_yaw_wheel) {
    return false;
  }
  return true;
}

bool
drone_ros2_centralized_control__msg__AttitudeSetpoint2__copy(
  const drone_ros2_centralized_control__msg__AttitudeSetpoint2 * input,
  drone_ros2_centralized_control__msg__AttitudeSetpoint2 * output)
{
  if (!input || !output) {
    return false;
  }
  // timestamp
  output->timestamp = input->timestamp;
  // mode
  output->mode = input->mode;
  // roll_rate
  output->roll_rate = input->roll_rate;
  // pitch_rate
  output->pitch_rate = input->pitch_rate;
  // yaw_rate
  output->yaw_rate = input->yaw_rate;
  // roll_body
  output->roll_body = input->roll_body;
  // pitch_body
  output->pitch_body = input->pitch_body;
  // yaw_body
  output->yaw_body = input->yaw_body;
  // yaw_sp_move_rate
  output->yaw_sp_move_rate = input->yaw_sp_move_rate;
  // q_d
  for (size_t i = 0; i < 4; ++i) {
    output->q_d[i] = input->q_d[i];
  }
  // thrust_body
  for (size_t i = 0; i < 3; ++i) {
    output->thrust_body[i] = input->thrust_body[i];
  }
  // reset_integral
  output->reset_integral = input->reset_integral;
  // fw_control_yaw_wheel
  output->fw_control_yaw_wheel = input->fw_control_yaw_wheel;
  return true;
}

drone_ros2_centralized_control__msg__AttitudeSetpoint2 *
drone_ros2_centralized_control__msg__AttitudeSetpoint2__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__AttitudeSetpoint2 * msg = (drone_ros2_centralized_control__msg__AttitudeSetpoint2 *)allocator.allocate(sizeof(drone_ros2_centralized_control__msg__AttitudeSetpoint2), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drone_ros2_centralized_control__msg__AttitudeSetpoint2));
  bool success = drone_ros2_centralized_control__msg__AttitudeSetpoint2__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drone_ros2_centralized_control__msg__AttitudeSetpoint2__destroy(drone_ros2_centralized_control__msg__AttitudeSetpoint2 * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drone_ros2_centralized_control__msg__AttitudeSetpoint2__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__init(drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__AttitudeSetpoint2 * data = NULL;

  if (size) {
    data = (drone_ros2_centralized_control__msg__AttitudeSetpoint2 *)allocator.zero_allocate(size, sizeof(drone_ros2_centralized_control__msg__AttitudeSetpoint2), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drone_ros2_centralized_control__msg__AttitudeSetpoint2__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drone_ros2_centralized_control__msg__AttitudeSetpoint2__fini(&data[i - 1]);
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
drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__fini(drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * array)
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
      drone_ros2_centralized_control__msg__AttitudeSetpoint2__fini(&array->data[i]);
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

drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence *
drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * array = (drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence *)allocator.allocate(sizeof(drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__destroy(drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__are_equal(const drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * lhs, const drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drone_ros2_centralized_control__msg__AttitudeSetpoint2__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence__copy(
  const drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * input,
  drone_ros2_centralized_control__msg__AttitudeSetpoint2__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drone_ros2_centralized_control__msg__AttitudeSetpoint2);
    drone_ros2_centralized_control__msg__AttitudeSetpoint2 * data =
      (drone_ros2_centralized_control__msg__AttitudeSetpoint2 *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drone_ros2_centralized_control__msg__AttitudeSetpoint2__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          drone_ros2_centralized_control__msg__AttitudeSetpoint2__fini(&data[i]);
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
    if (!drone_ros2_centralized_control__msg__AttitudeSetpoint2__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
