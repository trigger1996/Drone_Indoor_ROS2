// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from drone_ros2_centralized_control:msg/UavState.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "drone_ros2_centralized_control/msg/detail/uav_state__struct.h"
#include "drone_ros2_centralized_control/msg/detail/uav_state__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool drone_ros2_centralized_control__msg__uav_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[55];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("drone_ros2_centralized_control.msg._uav_state.UavState", full_classname_dest, 54) == 0);
  }
  drone_ros2_centralized_control__msg__UavState * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // timestamp
    PyObject * field = PyObject_GetAttrString(_pymsg, "timestamp");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->timestamp = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // id
    PyObject * field = PyObject_GetAttrString(_pymsg, "id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // mavtype
    PyObject * field = PyObject_GetAttrString(_pymsg, "mavtype");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->mavtype = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // autopilot
    PyObject * field = PyObject_GetAttrString(_pymsg, "autopilot");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->autopilot = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // base_mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "base_mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->base_mode = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // custom_mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "custom_mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->custom_mode = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // system_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "system_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->system_status = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // connected
    PyObject * field = PyObject_GetAttrString(_pymsg, "connected");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->connected = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // is_armed
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_armed");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->is_armed = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // bat_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "bat_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bat_voltage = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // bat_remaining
    PyObject * field = PyObject_GetAttrString(_pymsg, "bat_remaining");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bat_remaining = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // q
    PyObject * field = PyObject_GetAttrString(_pymsg, "q");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
      Py_ssize_t size = 4;
      float * dest = ros_message->q;
      for (Py_ssize_t i = 0; i < size; ++i) {
        float tmp = *(npy_float32 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(float));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // gyro_rad
    PyObject * field = PyObject_GetAttrString(_pymsg, "gyro_rad");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
      Py_ssize_t size = 3;
      float * dest = ros_message->gyro_rad;
      for (Py_ssize_t i = 0; i < size; ++i) {
        float tmp = *(npy_float32 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(float));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // gyro_integral_dt
    PyObject * field = PyObject_GetAttrString(_pymsg, "gyro_integral_dt");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->gyro_integral_dt = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // accelerometer_timestamp_relative
    PyObject * field = PyObject_GetAttrString(_pymsg, "accelerometer_timestamp_relative");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->accelerometer_timestamp_relative = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // accelerometer_m_s2
    PyObject * field = PyObject_GetAttrString(_pymsg, "accelerometer_m_s2");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
      Py_ssize_t size = 3;
      float * dest = ros_message->accelerometer_m_s2;
      for (Py_ssize_t i = 0; i < size; ++i) {
        float tmp = *(npy_float32 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(float));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // accelerometer_integral_dt
    PyObject * field = PyObject_GetAttrString(_pymsg, "accelerometer_integral_dt");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->accelerometer_integral_dt = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // accelerometer_clipping
    PyObject * field = PyObject_GetAttrString(_pymsg, "accelerometer_clipping");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->accelerometer_clipping = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // gyro_clipping
    PyObject * field = PyObject_GetAttrString(_pymsg, "gyro_clipping");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->gyro_clipping = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // xy_valid
    PyObject * field = PyObject_GetAttrString(_pymsg, "xy_valid");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->xy_valid = (Py_True == field);
    Py_DECREF(field);
  }
  {  // z_valid
    PyObject * field = PyObject_GetAttrString(_pymsg, "z_valid");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->z_valid = (Py_True == field);
    Py_DECREF(field);
  }
  {  // v_xy_valid
    PyObject * field = PyObject_GetAttrString(_pymsg, "v_xy_valid");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->v_xy_valid = (Py_True == field);
    Py_DECREF(field);
  }
  {  // v_z_valid
    PyObject * field = PyObject_GetAttrString(_pymsg, "v_z_valid");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->v_z_valid = (Py_True == field);
    Py_DECREF(field);
  }
  {  // x
    PyObject * field = PyObject_GetAttrString(_pymsg, "x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y
    PyObject * field = PyObject_GetAttrString(_pymsg, "y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // z
    PyObject * field = PyObject_GetAttrString(_pymsg, "z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vx
    PyObject * field = PyObject_GetAttrString(_pymsg, "vx");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vx = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vy
    PyObject * field = PyObject_GetAttrString(_pymsg, "vy");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vy = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vz
    PyObject * field = PyObject_GetAttrString(_pymsg, "vz");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vz = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ax
    PyObject * field = PyObject_GetAttrString(_pymsg, "ax");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ax = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ay
    PyObject * field = PyObject_GetAttrString(_pymsg, "ay");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ay = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // az
    PyObject * field = PyObject_GetAttrString(_pymsg, "az");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->az = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // heading
    PyObject * field = PyObject_GetAttrString(_pymsg, "heading");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->heading = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // delta_heading
    PyObject * field = PyObject_GetAttrString(_pymsg, "delta_heading");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->delta_heading = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // heading_good_for_control
    PyObject * field = PyObject_GetAttrString(_pymsg, "heading_good_for_control");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->heading_good_for_control = (Py_True == field);
    Py_DECREF(field);
  }
  {  // lat
    PyObject * field = PyObject_GetAttrString(_pymsg, "lat");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lat = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // lon
    PyObject * field = PyObject_GetAttrString(_pymsg, "lon");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lon = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // alt
    PyObject * field = PyObject_GetAttrString(_pymsg, "alt");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->alt = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // eph
    PyObject * field = PyObject_GetAttrString(_pymsg, "eph");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->eph = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // epv
    PyObject * field = PyObject_GetAttrString(_pymsg, "epv");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->epv = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // terrain_alt
    PyObject * field = PyObject_GetAttrString(_pymsg, "terrain_alt");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->terrain_alt = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // terrain_alt_valid
    PyObject * field = PyObject_GetAttrString(_pymsg, "terrain_alt_valid");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->terrain_alt_valid = (Py_True == field);
    Py_DECREF(field);
  }
  {  // dead_reckoning
    PyObject * field = PyObject_GetAttrString(_pymsg, "dead_reckoning");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->dead_reckoning = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * drone_ros2_centralized_control__msg__uav_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of UavState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("drone_ros2_centralized_control.msg._uav_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "UavState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  drone_ros2_centralized_control__msg__UavState * ros_message = (drone_ros2_centralized_control__msg__UavState *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // timestamp
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->timestamp);
    {
      int rc = PyObject_SetAttrString(_pymessage, "timestamp", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // mavtype
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->mavtype);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mavtype", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // autopilot
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->autopilot);
    {
      int rc = PyObject_SetAttrString(_pymessage, "autopilot", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // base_mode
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->base_mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "base_mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // custom_mode
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->custom_mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "custom_mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // system_status
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->system_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "system_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // connected
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->connected);
    {
      int rc = PyObject_SetAttrString(_pymessage, "connected", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_armed
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->is_armed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_armed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bat_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bat_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bat_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bat_remaining
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bat_remaining);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bat_remaining", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // q
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "q");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
    assert(sizeof(npy_float32) == sizeof(float));
    npy_float32 * dst = (npy_float32 *)PyArray_GETPTR1(seq_field, 0);
    float * src = &(ros_message->q[0]);
    memcpy(dst, src, 4 * sizeof(float));
    Py_DECREF(field);
  }
  {  // gyro_rad
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "gyro_rad");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
    assert(sizeof(npy_float32) == sizeof(float));
    npy_float32 * dst = (npy_float32 *)PyArray_GETPTR1(seq_field, 0);
    float * src = &(ros_message->gyro_rad[0]);
    memcpy(dst, src, 3 * sizeof(float));
    Py_DECREF(field);
  }
  {  // gyro_integral_dt
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->gyro_integral_dt);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gyro_integral_dt", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // accelerometer_timestamp_relative
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->accelerometer_timestamp_relative);
    {
      int rc = PyObject_SetAttrString(_pymessage, "accelerometer_timestamp_relative", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // accelerometer_m_s2
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "accelerometer_m_s2");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
    assert(sizeof(npy_float32) == sizeof(float));
    npy_float32 * dst = (npy_float32 *)PyArray_GETPTR1(seq_field, 0);
    float * src = &(ros_message->accelerometer_m_s2[0]);
    memcpy(dst, src, 3 * sizeof(float));
    Py_DECREF(field);
  }
  {  // accelerometer_integral_dt
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->accelerometer_integral_dt);
    {
      int rc = PyObject_SetAttrString(_pymessage, "accelerometer_integral_dt", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // accelerometer_clipping
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->accelerometer_clipping);
    {
      int rc = PyObject_SetAttrString(_pymessage, "accelerometer_clipping", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gyro_clipping
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->gyro_clipping);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gyro_clipping", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // xy_valid
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->xy_valid ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "xy_valid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // z_valid
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->z_valid ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "z_valid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // v_xy_valid
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->v_xy_valid ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "v_xy_valid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // v_z_valid
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->v_z_valid ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "v_z_valid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vx
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vx);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vx", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vy
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vy);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vy", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vz
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ax
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ax);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ax", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ay
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ay);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ay", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // az
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->az);
    {
      int rc = PyObject_SetAttrString(_pymessage, "az", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // heading
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->heading);
    {
      int rc = PyObject_SetAttrString(_pymessage, "heading", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // delta_heading
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->delta_heading);
    {
      int rc = PyObject_SetAttrString(_pymessage, "delta_heading", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // heading_good_for_control
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->heading_good_for_control ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "heading_good_for_control", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lat
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lat);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lat", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lon
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lon);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lon", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // alt
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->alt);
    {
      int rc = PyObject_SetAttrString(_pymessage, "alt", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // eph
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->eph);
    {
      int rc = PyObject_SetAttrString(_pymessage, "eph", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // epv
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->epv);
    {
      int rc = PyObject_SetAttrString(_pymessage, "epv", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // terrain_alt
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->terrain_alt);
    {
      int rc = PyObject_SetAttrString(_pymessage, "terrain_alt", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // terrain_alt_valid
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->terrain_alt_valid ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "terrain_alt_valid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // dead_reckoning
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->dead_reckoning ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "dead_reckoning", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
