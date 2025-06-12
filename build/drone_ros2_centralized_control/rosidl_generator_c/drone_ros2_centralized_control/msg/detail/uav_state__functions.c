// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice
#include "drone_ros2_centralized_control/msg/detail/uav_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
drone_ros2_centralized_control__msg__UavState__init(drone_ros2_centralized_control__msg__UavState * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    drone_ros2_centralized_control__msg__UavState__fini(msg);
    return false;
  }
  // timestamp
  // id
  // mavtype
  // autopilot
  // base_mode
  // custom_mode
  // system_status
  // connected
  // is_armed
  // bat_voltage
  // bat_remaining
  // q
  // gyro_rad
  // gyro_integral_dt
  // accelerometer_timestamp_relative
  // accelerometer_m_s2
  // accelerometer_integral_dt
  // accelerometer_clipping
  // gyro_clipping
  // xy_valid
  // z_valid
  // v_xy_valid
  // v_z_valid
  // x
  // y
  // z
  // vx
  // vy
  // vz
  // ax
  // ay
  // az
  // heading
  // delta_heading
  // heading_good_for_control
  // lat
  // lon
  // alt
  // eph
  // epv
  // terrain_alt
  // terrain_alt_valid
  // dead_reckoning
  return true;
}

void
drone_ros2_centralized_control__msg__UavState__fini(drone_ros2_centralized_control__msg__UavState * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // timestamp
  // id
  // mavtype
  // autopilot
  // base_mode
  // custom_mode
  // system_status
  // connected
  // is_armed
  // bat_voltage
  // bat_remaining
  // q
  // gyro_rad
  // gyro_integral_dt
  // accelerometer_timestamp_relative
  // accelerometer_m_s2
  // accelerometer_integral_dt
  // accelerometer_clipping
  // gyro_clipping
  // xy_valid
  // z_valid
  // v_xy_valid
  // v_z_valid
  // x
  // y
  // z
  // vx
  // vy
  // vz
  // ax
  // ay
  // az
  // heading
  // delta_heading
  // heading_good_for_control
  // lat
  // lon
  // alt
  // eph
  // epv
  // terrain_alt
  // terrain_alt_valid
  // dead_reckoning
}

bool
drone_ros2_centralized_control__msg__UavState__are_equal(const drone_ros2_centralized_control__msg__UavState * lhs, const drone_ros2_centralized_control__msg__UavState * rhs)
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
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // mavtype
  if (lhs->mavtype != rhs->mavtype) {
    return false;
  }
  // autopilot
  if (lhs->autopilot != rhs->autopilot) {
    return false;
  }
  // base_mode
  if (lhs->base_mode != rhs->base_mode) {
    return false;
  }
  // custom_mode
  if (lhs->custom_mode != rhs->custom_mode) {
    return false;
  }
  // system_status
  if (lhs->system_status != rhs->system_status) {
    return false;
  }
  // connected
  if (lhs->connected != rhs->connected) {
    return false;
  }
  // is_armed
  if (lhs->is_armed != rhs->is_armed) {
    return false;
  }
  // bat_voltage
  if (lhs->bat_voltage != rhs->bat_voltage) {
    return false;
  }
  // bat_remaining
  if (lhs->bat_remaining != rhs->bat_remaining) {
    return false;
  }
  // q
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->q[i] != rhs->q[i]) {
      return false;
    }
  }
  // gyro_rad
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->gyro_rad[i] != rhs->gyro_rad[i]) {
      return false;
    }
  }
  // gyro_integral_dt
  if (lhs->gyro_integral_dt != rhs->gyro_integral_dt) {
    return false;
  }
  // accelerometer_timestamp_relative
  if (lhs->accelerometer_timestamp_relative != rhs->accelerometer_timestamp_relative) {
    return false;
  }
  // accelerometer_m_s2
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->accelerometer_m_s2[i] != rhs->accelerometer_m_s2[i]) {
      return false;
    }
  }
  // accelerometer_integral_dt
  if (lhs->accelerometer_integral_dt != rhs->accelerometer_integral_dt) {
    return false;
  }
  // accelerometer_clipping
  if (lhs->accelerometer_clipping != rhs->accelerometer_clipping) {
    return false;
  }
  // gyro_clipping
  if (lhs->gyro_clipping != rhs->gyro_clipping) {
    return false;
  }
  // xy_valid
  if (lhs->xy_valid != rhs->xy_valid) {
    return false;
  }
  // z_valid
  if (lhs->z_valid != rhs->z_valid) {
    return false;
  }
  // v_xy_valid
  if (lhs->v_xy_valid != rhs->v_xy_valid) {
    return false;
  }
  // v_z_valid
  if (lhs->v_z_valid != rhs->v_z_valid) {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // z
  if (lhs->z != rhs->z) {
    return false;
  }
  // vx
  if (lhs->vx != rhs->vx) {
    return false;
  }
  // vy
  if (lhs->vy != rhs->vy) {
    return false;
  }
  // vz
  if (lhs->vz != rhs->vz) {
    return false;
  }
  // ax
  if (lhs->ax != rhs->ax) {
    return false;
  }
  // ay
  if (lhs->ay != rhs->ay) {
    return false;
  }
  // az
  if (lhs->az != rhs->az) {
    return false;
  }
  // heading
  if (lhs->heading != rhs->heading) {
    return false;
  }
  // delta_heading
  if (lhs->delta_heading != rhs->delta_heading) {
    return false;
  }
  // heading_good_for_control
  if (lhs->heading_good_for_control != rhs->heading_good_for_control) {
    return false;
  }
  // lat
  if (lhs->lat != rhs->lat) {
    return false;
  }
  // lon
  if (lhs->lon != rhs->lon) {
    return false;
  }
  // alt
  if (lhs->alt != rhs->alt) {
    return false;
  }
  // eph
  if (lhs->eph != rhs->eph) {
    return false;
  }
  // epv
  if (lhs->epv != rhs->epv) {
    return false;
  }
  // terrain_alt
  if (lhs->terrain_alt != rhs->terrain_alt) {
    return false;
  }
  // terrain_alt_valid
  if (lhs->terrain_alt_valid != rhs->terrain_alt_valid) {
    return false;
  }
  // dead_reckoning
  if (lhs->dead_reckoning != rhs->dead_reckoning) {
    return false;
  }
  return true;
}

bool
drone_ros2_centralized_control__msg__UavState__copy(
  const drone_ros2_centralized_control__msg__UavState * input,
  drone_ros2_centralized_control__msg__UavState * output)
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
  // timestamp
  output->timestamp = input->timestamp;
  // id
  output->id = input->id;
  // mavtype
  output->mavtype = input->mavtype;
  // autopilot
  output->autopilot = input->autopilot;
  // base_mode
  output->base_mode = input->base_mode;
  // custom_mode
  output->custom_mode = input->custom_mode;
  // system_status
  output->system_status = input->system_status;
  // connected
  output->connected = input->connected;
  // is_armed
  output->is_armed = input->is_armed;
  // bat_voltage
  output->bat_voltage = input->bat_voltage;
  // bat_remaining
  output->bat_remaining = input->bat_remaining;
  // q
  for (size_t i = 0; i < 4; ++i) {
    output->q[i] = input->q[i];
  }
  // gyro_rad
  for (size_t i = 0; i < 3; ++i) {
    output->gyro_rad[i] = input->gyro_rad[i];
  }
  // gyro_integral_dt
  output->gyro_integral_dt = input->gyro_integral_dt;
  // accelerometer_timestamp_relative
  output->accelerometer_timestamp_relative = input->accelerometer_timestamp_relative;
  // accelerometer_m_s2
  for (size_t i = 0; i < 3; ++i) {
    output->accelerometer_m_s2[i] = input->accelerometer_m_s2[i];
  }
  // accelerometer_integral_dt
  output->accelerometer_integral_dt = input->accelerometer_integral_dt;
  // accelerometer_clipping
  output->accelerometer_clipping = input->accelerometer_clipping;
  // gyro_clipping
  output->gyro_clipping = input->gyro_clipping;
  // xy_valid
  output->xy_valid = input->xy_valid;
  // z_valid
  output->z_valid = input->z_valid;
  // v_xy_valid
  output->v_xy_valid = input->v_xy_valid;
  // v_z_valid
  output->v_z_valid = input->v_z_valid;
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // z
  output->z = input->z;
  // vx
  output->vx = input->vx;
  // vy
  output->vy = input->vy;
  // vz
  output->vz = input->vz;
  // ax
  output->ax = input->ax;
  // ay
  output->ay = input->ay;
  // az
  output->az = input->az;
  // heading
  output->heading = input->heading;
  // delta_heading
  output->delta_heading = input->delta_heading;
  // heading_good_for_control
  output->heading_good_for_control = input->heading_good_for_control;
  // lat
  output->lat = input->lat;
  // lon
  output->lon = input->lon;
  // alt
  output->alt = input->alt;
  // eph
  output->eph = input->eph;
  // epv
  output->epv = input->epv;
  // terrain_alt
  output->terrain_alt = input->terrain_alt;
  // terrain_alt_valid
  output->terrain_alt_valid = input->terrain_alt_valid;
  // dead_reckoning
  output->dead_reckoning = input->dead_reckoning;
  return true;
}

drone_ros2_centralized_control__msg__UavState *
drone_ros2_centralized_control__msg__UavState__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__UavState * msg = (drone_ros2_centralized_control__msg__UavState *)allocator.allocate(sizeof(drone_ros2_centralized_control__msg__UavState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drone_ros2_centralized_control__msg__UavState));
  bool success = drone_ros2_centralized_control__msg__UavState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drone_ros2_centralized_control__msg__UavState__destroy(drone_ros2_centralized_control__msg__UavState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drone_ros2_centralized_control__msg__UavState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drone_ros2_centralized_control__msg__UavState__Sequence__init(drone_ros2_centralized_control__msg__UavState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__UavState * data = NULL;

  if (size) {
    data = (drone_ros2_centralized_control__msg__UavState *)allocator.zero_allocate(size, sizeof(drone_ros2_centralized_control__msg__UavState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drone_ros2_centralized_control__msg__UavState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drone_ros2_centralized_control__msg__UavState__fini(&data[i - 1]);
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
drone_ros2_centralized_control__msg__UavState__Sequence__fini(drone_ros2_centralized_control__msg__UavState__Sequence * array)
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
      drone_ros2_centralized_control__msg__UavState__fini(&array->data[i]);
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

drone_ros2_centralized_control__msg__UavState__Sequence *
drone_ros2_centralized_control__msg__UavState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_ros2_centralized_control__msg__UavState__Sequence * array = (drone_ros2_centralized_control__msg__UavState__Sequence *)allocator.allocate(sizeof(drone_ros2_centralized_control__msg__UavState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drone_ros2_centralized_control__msg__UavState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drone_ros2_centralized_control__msg__UavState__Sequence__destroy(drone_ros2_centralized_control__msg__UavState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drone_ros2_centralized_control__msg__UavState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drone_ros2_centralized_control__msg__UavState__Sequence__are_equal(const drone_ros2_centralized_control__msg__UavState__Sequence * lhs, const drone_ros2_centralized_control__msg__UavState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drone_ros2_centralized_control__msg__UavState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drone_ros2_centralized_control__msg__UavState__Sequence__copy(
  const drone_ros2_centralized_control__msg__UavState__Sequence * input,
  drone_ros2_centralized_control__msg__UavState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drone_ros2_centralized_control__msg__UavState);
    drone_ros2_centralized_control__msg__UavState * data =
      (drone_ros2_centralized_control__msg__UavState *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drone_ros2_centralized_control__msg__UavState__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          drone_ros2_centralized_control__msg__UavState__fini(&data[i]);
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
    if (!drone_ros2_centralized_control__msg__UavState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
