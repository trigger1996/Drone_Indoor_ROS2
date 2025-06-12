# generated from rosidl_generator_py/resource/_idl.py.em
# with input from drone_ros2_centralized_control:msg/UavState.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'q'
# Member 'gyro_rad'
# Member 'accelerometer_m_s2'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_UavState(type):
    """Metaclass of message 'UavState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'RELATIVE_TIMESTAMP_INVALID': 2147483647,
        'CLIPPING_X': 1,
        'CLIPPING_Y': 2,
        'CLIPPING_Z': 4,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('drone_ros2_centralized_control')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'drone_ros2_centralized_control.msg.UavState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__uav_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__uav_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__uav_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__uav_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__uav_state

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'RELATIVE_TIMESTAMP_INVALID': cls.__constants['RELATIVE_TIMESTAMP_INVALID'],
            'CLIPPING_X': cls.__constants['CLIPPING_X'],
            'CLIPPING_Y': cls.__constants['CLIPPING_Y'],
            'CLIPPING_Z': cls.__constants['CLIPPING_Z'],
        }

    @property
    def RELATIVE_TIMESTAMP_INVALID(self):
        """Message constant 'RELATIVE_TIMESTAMP_INVALID'."""
        return Metaclass_UavState.__constants['RELATIVE_TIMESTAMP_INVALID']

    @property
    def CLIPPING_X(self):
        """Message constant 'CLIPPING_X'."""
        return Metaclass_UavState.__constants['CLIPPING_X']

    @property
    def CLIPPING_Y(self):
        """Message constant 'CLIPPING_Y'."""
        return Metaclass_UavState.__constants['CLIPPING_Y']

    @property
    def CLIPPING_Z(self):
        """Message constant 'CLIPPING_Z'."""
        return Metaclass_UavState.__constants['CLIPPING_Z']


class UavState(metaclass=Metaclass_UavState):
    """
    Message class 'UavState'.

    Constants:
      RELATIVE_TIMESTAMP_INVALID
      CLIPPING_X
      CLIPPING_Y
      CLIPPING_Z
    """

    __slots__ = [
        '_header',
        '_timestamp',
        '_id',
        '_mavtype',
        '_autopilot',
        '_base_mode',
        '_custom_mode',
        '_system_status',
        '_connected',
        '_is_armed',
        '_bat_voltage',
        '_bat_remaining',
        '_q',
        '_gyro_rad',
        '_gyro_integral_dt',
        '_accelerometer_timestamp_relative',
        '_accelerometer_m_s2',
        '_accelerometer_integral_dt',
        '_accelerometer_clipping',
        '_gyro_clipping',
        '_xy_valid',
        '_z_valid',
        '_v_xy_valid',
        '_v_z_valid',
        '_x',
        '_y',
        '_z',
        '_vx',
        '_vy',
        '_vz',
        '_ax',
        '_ay',
        '_az',
        '_heading',
        '_delta_heading',
        '_heading_good_for_control',
        '_lat',
        '_lon',
        '_alt',
        '_eph',
        '_epv',
        '_terrain_alt',
        '_terrain_alt_valid',
        '_dead_reckoning',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'timestamp': 'uint64',
        'id': 'int32',
        'mavtype': 'int32',
        'autopilot': 'int32',
        'base_mode': 'int32',
        'custom_mode': 'int32',
        'system_status': 'int32',
        'connected': 'int32',
        'is_armed': 'int8',
        'bat_voltage': 'float',
        'bat_remaining': 'float',
        'q': 'float[4]',
        'gyro_rad': 'float[3]',
        'gyro_integral_dt': 'uint32',
        'accelerometer_timestamp_relative': 'int32',
        'accelerometer_m_s2': 'float[3]',
        'accelerometer_integral_dt': 'uint32',
        'accelerometer_clipping': 'uint8',
        'gyro_clipping': 'uint8',
        'xy_valid': 'boolean',
        'z_valid': 'boolean',
        'v_xy_valid': 'boolean',
        'v_z_valid': 'boolean',
        'x': 'float',
        'y': 'float',
        'z': 'float',
        'vx': 'float',
        'vy': 'float',
        'vz': 'float',
        'ax': 'float',
        'ay': 'float',
        'az': 'float',
        'heading': 'float',
        'delta_heading': 'float',
        'heading_good_for_control': 'boolean',
        'lat': 'double',
        'lon': 'double',
        'alt': 'float',
        'eph': 'float',
        'epv': 'float',
        'terrain_alt': 'float',
        'terrain_alt_valid': 'boolean',
        'dead_reckoning': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.timestamp = kwargs.get('timestamp', int())
        self.id = kwargs.get('id', int())
        self.mavtype = kwargs.get('mavtype', int())
        self.autopilot = kwargs.get('autopilot', int())
        self.base_mode = kwargs.get('base_mode', int())
        self.custom_mode = kwargs.get('custom_mode', int())
        self.system_status = kwargs.get('system_status', int())
        self.connected = kwargs.get('connected', int())
        self.is_armed = kwargs.get('is_armed', int())
        self.bat_voltage = kwargs.get('bat_voltage', float())
        self.bat_remaining = kwargs.get('bat_remaining', float())
        if 'q' not in kwargs:
            self.q = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.q = numpy.array(kwargs.get('q'), dtype=numpy.float32)
            assert self.q.shape == (4, )
        if 'gyro_rad' not in kwargs:
            self.gyro_rad = numpy.zeros(3, dtype=numpy.float32)
        else:
            self.gyro_rad = numpy.array(kwargs.get('gyro_rad'), dtype=numpy.float32)
            assert self.gyro_rad.shape == (3, )
        self.gyro_integral_dt = kwargs.get('gyro_integral_dt', int())
        self.accelerometer_timestamp_relative = kwargs.get('accelerometer_timestamp_relative', int())
        if 'accelerometer_m_s2' not in kwargs:
            self.accelerometer_m_s2 = numpy.zeros(3, dtype=numpy.float32)
        else:
            self.accelerometer_m_s2 = numpy.array(kwargs.get('accelerometer_m_s2'), dtype=numpy.float32)
            assert self.accelerometer_m_s2.shape == (3, )
        self.accelerometer_integral_dt = kwargs.get('accelerometer_integral_dt', int())
        self.accelerometer_clipping = kwargs.get('accelerometer_clipping', int())
        self.gyro_clipping = kwargs.get('gyro_clipping', int())
        self.xy_valid = kwargs.get('xy_valid', bool())
        self.z_valid = kwargs.get('z_valid', bool())
        self.v_xy_valid = kwargs.get('v_xy_valid', bool())
        self.v_z_valid = kwargs.get('v_z_valid', bool())
        self.x = kwargs.get('x', float())
        self.y = kwargs.get('y', float())
        self.z = kwargs.get('z', float())
        self.vx = kwargs.get('vx', float())
        self.vy = kwargs.get('vy', float())
        self.vz = kwargs.get('vz', float())
        self.ax = kwargs.get('ax', float())
        self.ay = kwargs.get('ay', float())
        self.az = kwargs.get('az', float())
        self.heading = kwargs.get('heading', float())
        self.delta_heading = kwargs.get('delta_heading', float())
        self.heading_good_for_control = kwargs.get('heading_good_for_control', bool())
        self.lat = kwargs.get('lat', float())
        self.lon = kwargs.get('lon', float())
        self.alt = kwargs.get('alt', float())
        self.eph = kwargs.get('eph', float())
        self.epv = kwargs.get('epv', float())
        self.terrain_alt = kwargs.get('terrain_alt', float())
        self.terrain_alt_valid = kwargs.get('terrain_alt_valid', bool())
        self.dead_reckoning = kwargs.get('dead_reckoning', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.id != other.id:
            return False
        if self.mavtype != other.mavtype:
            return False
        if self.autopilot != other.autopilot:
            return False
        if self.base_mode != other.base_mode:
            return False
        if self.custom_mode != other.custom_mode:
            return False
        if self.system_status != other.system_status:
            return False
        if self.connected != other.connected:
            return False
        if self.is_armed != other.is_armed:
            return False
        if self.bat_voltage != other.bat_voltage:
            return False
        if self.bat_remaining != other.bat_remaining:
            return False
        if all(self.q != other.q):
            return False
        if all(self.gyro_rad != other.gyro_rad):
            return False
        if self.gyro_integral_dt != other.gyro_integral_dt:
            return False
        if self.accelerometer_timestamp_relative != other.accelerometer_timestamp_relative:
            return False
        if all(self.accelerometer_m_s2 != other.accelerometer_m_s2):
            return False
        if self.accelerometer_integral_dt != other.accelerometer_integral_dt:
            return False
        if self.accelerometer_clipping != other.accelerometer_clipping:
            return False
        if self.gyro_clipping != other.gyro_clipping:
            return False
        if self.xy_valid != other.xy_valid:
            return False
        if self.z_valid != other.z_valid:
            return False
        if self.v_xy_valid != other.v_xy_valid:
            return False
        if self.v_z_valid != other.v_z_valid:
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.z != other.z:
            return False
        if self.vx != other.vx:
            return False
        if self.vy != other.vy:
            return False
        if self.vz != other.vz:
            return False
        if self.ax != other.ax:
            return False
        if self.ay != other.ay:
            return False
        if self.az != other.az:
            return False
        if self.heading != other.heading:
            return False
        if self.delta_heading != other.delta_heading:
            return False
        if self.heading_good_for_control != other.heading_good_for_control:
            return False
        if self.lat != other.lat:
            return False
        if self.lon != other.lon:
            return False
        if self.alt != other.alt:
            return False
        if self.eph != other.eph:
            return False
        if self.epv != other.epv:
            return False
        if self.terrain_alt != other.terrain_alt:
            return False
        if self.terrain_alt_valid != other.terrain_alt_valid:
            return False
        if self.dead_reckoning != other.dead_reckoning:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'timestamp' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'timestamp' field must be an unsigned integer in [0, 18446744073709551615]"
        self._timestamp = value

    @property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'id' field must be an integer in [-2147483648, 2147483647]"
        self._id = value

    @property
    def mavtype(self):
        """Message field 'mavtype'."""
        return self._mavtype

    @mavtype.setter
    def mavtype(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'mavtype' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'mavtype' field must be an integer in [-2147483648, 2147483647]"
        self._mavtype = value

    @property
    def autopilot(self):
        """Message field 'autopilot'."""
        return self._autopilot

    @autopilot.setter
    def autopilot(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'autopilot' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'autopilot' field must be an integer in [-2147483648, 2147483647]"
        self._autopilot = value

    @property
    def base_mode(self):
        """Message field 'base_mode'."""
        return self._base_mode

    @base_mode.setter
    def base_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'base_mode' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'base_mode' field must be an integer in [-2147483648, 2147483647]"
        self._base_mode = value

    @property
    def custom_mode(self):
        """Message field 'custom_mode'."""
        return self._custom_mode

    @custom_mode.setter
    def custom_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'custom_mode' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'custom_mode' field must be an integer in [-2147483648, 2147483647]"
        self._custom_mode = value

    @property
    def system_status(self):
        """Message field 'system_status'."""
        return self._system_status

    @system_status.setter
    def system_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'system_status' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'system_status' field must be an integer in [-2147483648, 2147483647]"
        self._system_status = value

    @property
    def connected(self):
        """Message field 'connected'."""
        return self._connected

    @connected.setter
    def connected(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'connected' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'connected' field must be an integer in [-2147483648, 2147483647]"
        self._connected = value

    @property
    def is_armed(self):
        """Message field 'is_armed'."""
        return self._is_armed

    @is_armed.setter
    def is_armed(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'is_armed' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'is_armed' field must be an integer in [-128, 127]"
        self._is_armed = value

    @property
    def bat_voltage(self):
        """Message field 'bat_voltage'."""
        return self._bat_voltage

    @bat_voltage.setter
    def bat_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'bat_voltage' field must be of type 'float'"
        self._bat_voltage = value

    @property
    def bat_remaining(self):
        """Message field 'bat_remaining'."""
        return self._bat_remaining

    @bat_remaining.setter
    def bat_remaining(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'bat_remaining' field must be of type 'float'"
        self._bat_remaining = value

    @property
    def q(self):
        """Message field 'q'."""
        return self._q

    @q.setter
    def q(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'q' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'q' numpy.ndarray() must have a size of 4"
            self._q = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 4 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'q' field must be a set or sequence with length 4 and each value of type 'float'"
        self._q = numpy.array(value, dtype=numpy.float32)

    @property
    def gyro_rad(self):
        """Message field 'gyro_rad'."""
        return self._gyro_rad

    @gyro_rad.setter
    def gyro_rad(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'gyro_rad' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 3, \
                "The 'gyro_rad' numpy.ndarray() must have a size of 3"
            self._gyro_rad = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'gyro_rad' field must be a set or sequence with length 3 and each value of type 'float'"
        self._gyro_rad = numpy.array(value, dtype=numpy.float32)

    @property
    def gyro_integral_dt(self):
        """Message field 'gyro_integral_dt'."""
        return self._gyro_integral_dt

    @gyro_integral_dt.setter
    def gyro_integral_dt(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'gyro_integral_dt' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'gyro_integral_dt' field must be an unsigned integer in [0, 4294967295]"
        self._gyro_integral_dt = value

    @property
    def accelerometer_timestamp_relative(self):
        """Message field 'accelerometer_timestamp_relative'."""
        return self._accelerometer_timestamp_relative

    @accelerometer_timestamp_relative.setter
    def accelerometer_timestamp_relative(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'accelerometer_timestamp_relative' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'accelerometer_timestamp_relative' field must be an integer in [-2147483648, 2147483647]"
        self._accelerometer_timestamp_relative = value

    @property
    def accelerometer_m_s2(self):
        """Message field 'accelerometer_m_s2'."""
        return self._accelerometer_m_s2

    @accelerometer_m_s2.setter
    def accelerometer_m_s2(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'accelerometer_m_s2' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 3, \
                "The 'accelerometer_m_s2' numpy.ndarray() must have a size of 3"
            self._accelerometer_m_s2 = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'accelerometer_m_s2' field must be a set or sequence with length 3 and each value of type 'float'"
        self._accelerometer_m_s2 = numpy.array(value, dtype=numpy.float32)

    @property
    def accelerometer_integral_dt(self):
        """Message field 'accelerometer_integral_dt'."""
        return self._accelerometer_integral_dt

    @accelerometer_integral_dt.setter
    def accelerometer_integral_dt(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'accelerometer_integral_dt' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'accelerometer_integral_dt' field must be an unsigned integer in [0, 4294967295]"
        self._accelerometer_integral_dt = value

    @property
    def accelerometer_clipping(self):
        """Message field 'accelerometer_clipping'."""
        return self._accelerometer_clipping

    @accelerometer_clipping.setter
    def accelerometer_clipping(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'accelerometer_clipping' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'accelerometer_clipping' field must be an unsigned integer in [0, 255]"
        self._accelerometer_clipping = value

    @property
    def gyro_clipping(self):
        """Message field 'gyro_clipping'."""
        return self._gyro_clipping

    @gyro_clipping.setter
    def gyro_clipping(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'gyro_clipping' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'gyro_clipping' field must be an unsigned integer in [0, 255]"
        self._gyro_clipping = value

    @property
    def xy_valid(self):
        """Message field 'xy_valid'."""
        return self._xy_valid

    @xy_valid.setter
    def xy_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'xy_valid' field must be of type 'bool'"
        self._xy_valid = value

    @property
    def z_valid(self):
        """Message field 'z_valid'."""
        return self._z_valid

    @z_valid.setter
    def z_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'z_valid' field must be of type 'bool'"
        self._z_valid = value

    @property
    def v_xy_valid(self):
        """Message field 'v_xy_valid'."""
        return self._v_xy_valid

    @v_xy_valid.setter
    def v_xy_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'v_xy_valid' field must be of type 'bool'"
        self._v_xy_valid = value

    @property
    def v_z_valid(self):
        """Message field 'v_z_valid'."""
        return self._v_z_valid

    @v_z_valid.setter
    def v_z_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'v_z_valid' field must be of type 'bool'"
        self._v_z_valid = value

    @property
    def x(self):
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x' field must be of type 'float'"
        self._x = value

    @property
    def y(self):
        """Message field 'y'."""
        return self._y

    @y.setter
    def y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y' field must be of type 'float'"
        self._y = value

    @property
    def z(self):
        """Message field 'z'."""
        return self._z

    @z.setter
    def z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'z' field must be of type 'float'"
        self._z = value

    @property
    def vx(self):
        """Message field 'vx'."""
        return self._vx

    @vx.setter
    def vx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vx' field must be of type 'float'"
        self._vx = value

    @property
    def vy(self):
        """Message field 'vy'."""
        return self._vy

    @vy.setter
    def vy(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vy' field must be of type 'float'"
        self._vy = value

    @property
    def vz(self):
        """Message field 'vz'."""
        return self._vz

    @vz.setter
    def vz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vz' field must be of type 'float'"
        self._vz = value

    @property
    def ax(self):
        """Message field 'ax'."""
        return self._ax

    @ax.setter
    def ax(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ax' field must be of type 'float'"
        self._ax = value

    @property
    def ay(self):
        """Message field 'ay'."""
        return self._ay

    @ay.setter
    def ay(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ay' field must be of type 'float'"
        self._ay = value

    @property
    def az(self):
        """Message field 'az'."""
        return self._az

    @az.setter
    def az(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'az' field must be of type 'float'"
        self._az = value

    @property
    def heading(self):
        """Message field 'heading'."""
        return self._heading

    @heading.setter
    def heading(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'heading' field must be of type 'float'"
        self._heading = value

    @property
    def delta_heading(self):
        """Message field 'delta_heading'."""
        return self._delta_heading

    @delta_heading.setter
    def delta_heading(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'delta_heading' field must be of type 'float'"
        self._delta_heading = value

    @property
    def heading_good_for_control(self):
        """Message field 'heading_good_for_control'."""
        return self._heading_good_for_control

    @heading_good_for_control.setter
    def heading_good_for_control(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'heading_good_for_control' field must be of type 'bool'"
        self._heading_good_for_control = value

    @property
    def lat(self):
        """Message field 'lat'."""
        return self._lat

    @lat.setter
    def lat(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lat' field must be of type 'float'"
        self._lat = value

    @property
    def lon(self):
        """Message field 'lon'."""
        return self._lon

    @lon.setter
    def lon(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lon' field must be of type 'float'"
        self._lon = value

    @property
    def alt(self):
        """Message field 'alt'."""
        return self._alt

    @alt.setter
    def alt(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alt' field must be of type 'float'"
        self._alt = value

    @property
    def eph(self):
        """Message field 'eph'."""
        return self._eph

    @eph.setter
    def eph(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'eph' field must be of type 'float'"
        self._eph = value

    @property
    def epv(self):
        """Message field 'epv'."""
        return self._epv

    @epv.setter
    def epv(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'epv' field must be of type 'float'"
        self._epv = value

    @property
    def terrain_alt(self):
        """Message field 'terrain_alt'."""
        return self._terrain_alt

    @terrain_alt.setter
    def terrain_alt(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'terrain_alt' field must be of type 'float'"
        self._terrain_alt = value

    @property
    def terrain_alt_valid(self):
        """Message field 'terrain_alt_valid'."""
        return self._terrain_alt_valid

    @terrain_alt_valid.setter
    def terrain_alt_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'terrain_alt_valid' field must be of type 'bool'"
        self._terrain_alt_valid = value

    @property
    def dead_reckoning(self):
        """Message field 'dead_reckoning'."""
        return self._dead_reckoning

    @dead_reckoning.setter
    def dead_reckoning(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'dead_reckoning' field must be of type 'bool'"
        self._dead_reckoning = value
