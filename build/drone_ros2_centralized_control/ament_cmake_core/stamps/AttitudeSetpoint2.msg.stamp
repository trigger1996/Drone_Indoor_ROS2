uint64 timestamp		# time since system start (microseconds)

int32   mode            # 0 rate control, 
                        # 1 quaternion control, thrust[2] needed as negative
                        # 2 roll / pitch / yaw control, thrust[2] needed as negative

# body angular rates in NED frame
float32 roll_rate		# [rad/s] roll rate setpoint
float32 pitch_rate		# [rad/s] pitch rate setpoint
float32 yaw_rate		# [rad/s] yaw rate setpoint

float32 roll_body		# body angle in NED frame (can be NaN for FW)
float32 pitch_body		# body angle in NED frame (can be NaN for FW)
float32 yaw_body		# body angle in NED frame (can be NaN for FW)

float32 yaw_sp_move_rate	# rad/s (commanded by user)

# For quaternion-based attitude control
float32[4] q_d			# Desired quaternion for quaternion control

# For clarification: For multicopters thrust_body[0] and thrust[1] are usually 0 and thrust[2] is the negative throttle demand.
# For fixed wings thrust_x is the throttle demand and thrust_y, thrust_z will usually be zero.
float32[3] thrust_body		# Normalized thrust command in body NED frame [-1,1]

bool reset_integral	# Reset roll/pitch/yaw integrals (navigation logic change)

bool fw_control_yaw_wheel	# control heading with steering wheel (used for auto takeoff on runway)

# TOPICS vehicle_attitude_setpoint mc_virtual_attitude_setpoint fw_virtual_attitude_setpoint
