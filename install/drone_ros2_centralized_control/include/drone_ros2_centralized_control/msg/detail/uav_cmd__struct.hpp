// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_ros2_centralized_control:msg/UavCmd.idl
// generated code does not contain a copyright notice

#ifndef DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__STRUCT_HPP_
#define DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__drone_ros2_centralized_control__msg__UavCmd __attribute__((deprecated))
#else
# define DEPRECATED__drone_ros2_centralized_control__msg__UavCmd __declspec(deprecated)
#endif

namespace drone_ros2_centralized_control
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct UavCmd_
{
  using Type = UavCmd_<ContainerAllocator>;

  explicit UavCmd_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->is_arm = 0l;
    }
  }

  explicit UavCmd_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->is_arm = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _id_type =
    int32_t;
  _id_type id;
  using _is_arm_type =
    int32_t;
  _is_arm_type is_arm;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__id(
    const int32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__is_arm(
    const int32_t & _arg)
  {
    this->is_arm = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_ros2_centralized_control__msg__UavCmd
    std::shared_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_ros2_centralized_control__msg__UavCmd
    std::shared_ptr<drone_ros2_centralized_control::msg::UavCmd_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UavCmd_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    if (this->is_arm != other.is_arm) {
      return false;
    }
    return true;
  }
  bool operator!=(const UavCmd_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UavCmd_

// alias to use template instance with default allocator
using UavCmd =
  drone_ros2_centralized_control::msg::UavCmd_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drone_ros2_centralized_control

#endif  // DRONE_ROS2_CENTRALIZED_CONTROL__MSG__DETAIL__UAV_CMD__STRUCT_HPP_
