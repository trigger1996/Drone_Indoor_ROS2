std_msgs/Header header

uint64 timestamp			# time since system start (microseconds)


int32 id
int32 mavtype
int32 autopilot
int32 base_mode
int32 custom_mode
int32 system_status
int32 connected
int8  is_armed      # Added

float32 bat_voltage
float32 bat_remaining

#
# From Vehicle Attitude
#       This is similar to the mavlink message ATTITUDE_QUATERNION, but for onboard use
#
float32[4] q                    # Quaternion rotation from the FRD body frame to the NED earth frame

# From SensorCombined
# Sensor readings in SI-unit form.
# These fields are scaled and offset-compensated where possible and do not
# change with board revisions and sensor updates.
#
int32 RELATIVE_TIMESTAMP_INVALID = 2147483647   # (0x7fffffff) If one of the relative timestamps is set to this value, it means the associated sensor values are invalid

# gyro timstamp is equal to the timestamp of the message
float32[3] gyro_rad                     # average angular rate measured in the FRD body frame XYZ-axis in rad/s over the last gyro sampling period
uint32 gyro_integral_dt                 # gyro measurement sampling period in microseconds

int32 accelerometer_timestamp_relative  # timestamp + accelerometer_timestamp_relative = Accelerometer timestamp
float32[3] accelerometer_m_s2           # average value acceleration measured in the FRD body frame XYZ-axis in m/s^2 over the last accelerometer sampling period
uint32 accelerometer_integral_dt        # accelerometer measurement sampling period in microseconds

uint8 CLIPPING_X = 1
uint8 CLIPPING_Y = 2
uint8 CLIPPING_Z = 4

uint8 accelerometer_clipping    # bitfield indicating if there was any accelerometer clipping (per axis) during the integration time frame
uint8 gyro_clipping             # bitfield indicating if there was any gyro clipping (per axis) during the integration time frame



#
# From EKF2 NED Frame
#       Fused local position in NED.
#       The coordinate system origin is the vehicle position at the time when the EKF2-module was started.


bool xy_valid				# true if x and y are valid
bool z_valid				# true if z is valid
bool v_xy_valid				# true if vx and vy are valid
bool v_z_valid				# true if vz is valid

# Position in local NED frame
float32 x				# North position in NED earth-fixed frame, (metres)
float32 y				# East position in NED earth-fixed frame, (metres)
float32 z				# Down position (negative altitude) in NED earth-fixed frame, (metres)

# Velocity in NED frame
float32 vx 				# North velocity in NED earth-fixed frame, (metres/sec)
float32 vy				# East velocity in NED earth-fixed frame, (metres/sec)
float32 vz				# Down velocity in NED earth-fixed frame, (metres/sec)

# Acceleration in NED frame
float32 ax        # North velocity derivative in NED earth-fixed frame, (metres/sec^2)
float32 ay        # East velocity derivative in NED earth-fixed frame, (metres/sec^2)
float32 az        # Down velocity derivative in NED earth-fixed frame, (metres/sec^2)

float32 heading				# Euler yaw angle transforming the tangent plane relative to NED earth-fixed frame, -PI..+PI,  (radians)
float32 delta_heading
bool heading_good_for_control


#
# From VehicleGlobalPosition
#       Fused global position in WGS84.
#       This struct contains global position estimation. It is not the raw GPS
#       measurement (@see vehicle_gps_position). This topic is usually published by the position
#       estimator, which will take more sources of information into account than just GPS,
#       e.g. control inputs of the vehicle in a Kalman-filter implementation.
#

float64 lat			# Latitude, (degrees)
float64 lon			# Longitude, (degrees)
float32 alt			# Altitude AMSL, (meters)

float32 eph			# Standard deviation of horizontal position error, (metres)
float32 epv			# Standard deviation of vertical position error, (metres)

float32 terrain_alt		# Terrain altitude WGS84, (metres)
bool terrain_alt_valid		# Terrain altitude estimate is valid

bool dead_reckoning		# True if this position is estimated through dead-reckoning
