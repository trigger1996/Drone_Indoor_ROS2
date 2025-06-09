#!/usr/bin/env python3

import rclpy
from threading import Lock
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

from std_msgs.msg import Header, Float32MultiArray
from geometry_msgs.msg import Twist, PoseStamped, Quaternion
from nav_msgs.msg import Odometry
from px4_msgs.msg import TrajectorySetpoint, VehicleAttitude, VehicleLocalPosition, VehicleGlobalPosition, VehicleCommand, VehicleStatus, SensorCombined, VehicleAttitudeSetpoint, VehicleRatesSetpoint, OffboardControlMode

from drone_ros2_centralized_control.msg import UavCmd, UavState, AttitudeSetpoint2

import math

'''

HOW TO USE
    ros2 run your_pkg multi_uav_bridge.py --ros-args -p uav_ids:="[1,2,3]"


Arm / Disarm Command
    UavCmd -> /px4_1/fmu/in/vehicle_command 

Position / Velocity / Accerleration / Attitude Command

    Pos: PosStamped -> /px4_1/fmu/in/trajectory_setpoint        TrajectorySetpoint.msg
    Vel: Twist      -> /px4_1/fmu/in/trajectory_setpoint
    Acc: Float32    -> /px4_1/fmu/in/trajectory_setpoint
    Att:            -> /px4_1/fmu/in/vehicle_attitude_setpoint  VehicleAttitudeSetpoint.msg

UAVStates

        /px4_1/fmu/out/sensor_combined -> UAVState
        /px4_1/fmu/out/vehicle_status  -> 

/px4_1/fmu/in/obstacle_distance
/px4_1/fmu/in/offboard_control_mode
/px4_1/fmu/in/onboard_computer_status
/px4_1/fmu/in/sensor_optical_flow
/px4_1/fmu/in/telemetry_status
/px4_1/fmu/in/trajectory_setpoint
/px4_1/fmu/in/vehicle_attitude_setpoint
/px4_1/fmu/in/vehicle_command
/px4_1/fmu/in/vehicle_mocap_odometry
/px4_1/fmu/in/vehicle_rates_setpoint
/px4_1/fmu/in/vehicle_trajectory_bezier
/px4_1/fmu/in/vehicle_trajectory_waypoint
/px4_1/fmu/in/vehicle_visual_odometry
/px4_1/fmu/out/failsafe_flags
/px4_1/fmu/out/position_setpoint_triplet
/px4_1/fmu/out/sensor_combined
/px4_1/fmu/out/timesync_status
/px4_1/fmu/out/vehicle_attitude
/px4_1/fmu/out/vehicle_control_mode
/px4_1/fmu/out/vehicle_global_position
/px4_1/fmu/out/vehicle_gps_position
/px4_1/fmu/out/vehicle_local_position
/px4_1/fmu/out/vehicle_odometry
/px4_1/fmu/out/vehicle_status


'''

def euler_to_quaternion(roll, pitch, yaw):
    """欧拉角转四元数"""
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    q = Quaternion()
    q.w = cr * cp * cy + sr * sp * sy
    q.x = sr * cp * cy - cr * sp * sy
    q.y = cr * sp * cy + sr * cp * sy
    q.z = cr * cp * sy - sr * sp * cy
    return q

class UavBridge:
    def __init__(self, node: Node, uav_id: int):
        self.node         = node
        self.uav_id       = uav_id
        self.component_id = 1
        self.ns = f"/px4_{uav_id}"
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.bridge_main_cntr = 0                                           # MUST BE DEFINED FIRST
        self.timer = self.node.create_timer(0.02, self.uav_bridge_main)     # TODO 50Hz adequate?

        # 发布器
        self.traj_pub     = node.create_publisher(TrajectorySetpoint,      f"{self.ns}/fmu/in/trajectory_setpoint",       qos)
        self.cmd_pub      = node.create_publisher(VehicleCommand,          f"{self.ns}/fmu/in/vehicle_command",           qos)
        self.offboard_pub = node.create_publisher(OffboardControlMode,     f"{self.ns}/fmu/in/offboard_control_mode",     qos)       # Critical
        self.attitude_pub = node.create_publisher(VehicleAttitudeSetpoint, f"{self.ns}/fmu/in/vehicle_attitude_setpoint", qos)
        self.att_rate_pub = node.create_publisher(VehicleRatesSetpoint,    f"{self.ns}/fmu/in/vehicle_rates_setpoint",    qos)     
        self.state_pub    = node.create_publisher(UavState,                f"{self.ns}/uav_state",                        qos)       # TODO, topic name
        self.odom_pub     = node.create_publisher(Odometry,                f"{self.ns}/odom",                             qos)

        # 订阅控制输入
        node.create_subscription(Twist,             f"{self.ns}/cmd_vel", self.twist_cb, qos)
        node.create_subscription(PoseStamped,       f"{self.ns}/cmd_pos", self.pose_cb, qos)
        node.create_subscription(Float32MultiArray, f"{self.ns}/cmd_acc", self.acc_cb, qos)
        node.create_subscription(AttitudeSetpoint2, f"{self.ns}/cmd_att", self.attitude_setpt_cb, qos)

        # 订阅状态
        node.create_subscription(VehicleAttitude,       f"{self.ns}/fmu/out/vehicle_attitude",        self.attitude_cb, qos)         # euler
        node.create_subscription(SensorCombined,        f"{self.ns}/fmu/out/sensor_combined",         self.sensor_cb, qos)           # imu data
        node.create_subscription(VehicleLocalPosition,  f"{self.ns}/fmu/out/vehicle_local_position",  self.local_pos_cb,  qos)       # xyz
        node.create_subscription(VehicleGlobalPosition, f"{self.ns}/fmu/out/vehicle_global_position", self.global_pos_cb, qos)       # lat / lon
        node.create_subscription(VehicleStatus,         f"{self.ns}/fmu/out/vehicle_status",          self.status_cb, qos)           # vehicle status

        self.latest_status = None
        self.latest_sensor = None

        self.lock = Lock()

        # for offboard heartbeat
        self.current_ctrl_mode = None                      # 'position', 'velocity', 'attitude', 'body_rate', 'acceleration'

        # Attitude
        self.q = [ 1.0, 0.0, 0.0, 0.0 ]                    # TODO xyzw? wxyz?
        self.delta_q_reset = [ 1.0, 0.0, 0.0, 0.0 ]
        self.quat_reset_counter = 0        

        # Local position
        self.xy_valid = False
        self.z_valid = False
        self.v_xy_valid = False
        self.v_z_valid = False

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.delta_xy = [0.0, 0.0]
        self.xy_reset_counter = 0

        self.delta_z = 0.0
        self.z_reset_counter = 0

        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0
        self.z_deriv = 0.0

        self.delta_vxy = [0.0, 0.0]
        self.vxy_reset_counter = 0

        self.delta_vz = 0.0
        self.vz_reset_counter = 0

        self.ax = 0.0
        self.ay = 0.0
        self.az = 0.0

        self.heading = 0.0
        self.delta_heading = 0.0
        self.heading_reset_counter = 0
        self.heading_good_for_control = False

        self.xy_global = False
        self.z_global = False
        self.ref_timestamp = 0
        self.ref_lat = 0.0
        self.ref_lon = 0.0
        self.ref_alt = 0.0

        self.dist_bottom = 0.0
        self.dist_bottom_valid = False
        self.dist_bottom_sensor_bitfield = 0

        self.eph = 0.0
        self.epv = 0.0
        self.evh = 0.0
        self.evv = 0.0

        self.dead_reckoning = False
        self.vxy_max = 0.0
        self.vz_max = 0.0
        self.hagl_min = 0.0
        self.hagl_max = 0.0
        
        # Global Position
        self.lat = 0.0
        self.lon = 0.0
        self.alt = 0.0
        self.alt_ellipsoid = 0.0
        self.delta_alt = 0.0
        self.lat_lon_reset_counter = 0
        self.alt_reset_counter = 0
        self.eph_global = 0.0
        self.epv_global = 0.0
        self.terrain_alt = 0.0
        self.terrain_alt_valid = False
        self.dead_reckoning_global = False        

    def twist_cb(self, msg: Twist):
        if self.current_ctrl_mode != 'velocity':
            self.current_ctrl_mode = 'velocity'
            self.node.get_logger().info(f"[Gazebo Relay][UAV_{self.uav_id}] Switched to velocity control ...")            

        traj = TrajectorySetpoint()
        traj.position = [math.nan, math.nan, math.nan]
        traj.velocity = [msg.linear.x, msg.linear.y, msg.linear.z]
        traj.acceleration = [math.nan, math.nan, math.nan]
        traj.yaw = msg.angular.z
        traj.timestamp = int(self.node.get_clock().now().nanoseconds / 1000)
        self.traj_pub.publish(traj)

        # self.node.get_logger().info(f"[Gazebo Bridge ][UAV {self.uav_id}] Trajectory Setpt sent: vx / vy / vz : {traj.velocity} ")

    def pose_cb(self, msg: PoseStamped):
        if self.current_ctrl_mode != 'position':
            self.current_ctrl_mode = 'position'
            self.node.get_logger().info(f"[Gazebo Relay][UAV_{self.uav_id}] Switched to position control ...")

        traj = TrajectorySetpoint()
        traj.position = [msg.pose.position.x, msg.pose.position.y, msg.pose.position.z]
        traj.velocity = [math.nan, math.nan, math.nan]
        traj.acceleration = [math.nan, math.nan, math.nan]
        traj.timestamp = int(self.node.get_clock().now().nanoseconds / 1000)
        self.traj_pub.publish(traj)

    def acc_cb(self, msg: Float32MultiArray):
        if self.current_ctrl_mode != 'acceleration':
            self.current_ctrl_mode = 'acceleration'
            self.node.get_logger().info(f"[Gazebo Relay][UAV_{self.uav_id}] Switched to accleration control ...")

        traj = TrajectorySetpoint()
        traj.position = [math.nan, math.nan, math.nan]       
        traj.velocity = [math.nan, math.nan, math.nan]
        traj.acceleration = [msg.data[0], msg.data[1], msg.data[2]]
        traj.timestamp = int(self.node.get_clock().now().nanoseconds / 1000)
        self.traj_pub.publish(traj)

    def attitude_setpt_cb(self, msg: AttitudeSetpoint2):
        # 0 rate control, 
        # 1 quaternion control, thrust[2] needed as negative
        # 2 roll / pitch / yaw control, thrust[2] needed as negative
        if msg.mode == 0:
            if self.current_ctrl_mode != 'body_rate':
                self.current_ctrl_mode = 'body_rate'
                self.node.get_logger().info(f"[Gazebo Relay][UAV_{self.uav_id}] Switched to body_rate control ...")

            rate       = VehicleRatesSetpoint()
            rate.roll  = msg.roll_rate
            rate.pitch = msg.pitch_rate
            rate.yaw   = msg.yaw_rate

            rate.timestamp = int(self.node.get_clock().now().nanoseconds / 1000)
            rate.thrust_body = [float(msg.thrust_body[0]), float(msg.thrust_body[1]), float(msg.thrust_body[2])]
            self.att_rate_pub.publish(rate)
        else:
            if self.current_ctrl_mode != 'attitude':
                self.current_ctrl_mode = 'attitude'
                self.node.get_logger().info(f"[Gazebo Relay][UAV_{self.uav_id}] Switched to attitude control ...")

            attitude = VehicleAttitudeSetpoint()

            if msg.mode == 1:
                attitude.q_d = [float(msg.q_d[0]), float(msg.q_d[1]), float(msg.q_d[2]), float(msg.q_d[3])]
            elif msg.mode == 2:
                attitude.roll_body  = msg.roll_body
                attitude.pitch_body = msg.pitch_body
                attitude.yaw_body   = msg.yaw_body

            attitude.timestamp = int(self.node.get_clock().now().nanoseconds / 1000)
            attitude.thrust_body = [float(msg.thrust_body[0]), float(msg.thrust_body[1]), float(msg.thrust_body[2])]
            self.attitude_pub.publish(attitude)

    def attitude_cb(self, msg : VehicleAttitude):
        with self.lock:
            self.q = list(msg.q)
            self.delta_q_reset = list(msg.delta_q_reset)
            self.quat_reset_counter = msg.quat_reset_counter

    def local_pos_cb(self, msg : VehicleLocalPosition):
        with self.lock:
            self.xy_valid = msg.xy_valid
            self.z_valid = msg.z_valid
            self.v_xy_valid = msg.v_xy_valid
            self.v_z_valid = msg.v_z_valid

            self.x = msg.x
            self.y = msg.y
            self.z = msg.z
            self.delta_xy = list(msg.delta_xy)
            self.xy_reset_counter = msg.xy_reset_counter

            self.delta_z = msg.delta_z
            self.z_reset_counter = msg.z_reset_counter

            self.vx = msg.vx
            self.vy = msg.vy
            self.vz = msg.vz
            self.z_deriv = msg.z_deriv

            self.delta_vxy = list(msg.delta_vxy)
            self.vxy_reset_counter = msg.vxy_reset_counter

            self.delta_vz = msg.delta_vz
            self.vz_reset_counter = msg.vz_reset_counter

            self.ax = msg.ax
            self.ay = msg.ay
            self.az = msg.az

            self.heading = msg.heading
            self.delta_heading = msg.delta_heading
            self.heading_reset_counter = msg.heading_reset_counter
            self.heading_good_for_control = msg.heading_good_for_control

            self.xy_global = msg.xy_global
            self.z_global = msg.z_global
            self.ref_timestamp = msg.ref_timestamp
            self.ref_lat = msg.ref_lat
            self.ref_lon = msg.ref_lon
            self.ref_alt = msg.ref_alt

            self.dist_bottom = msg.dist_bottom
            self.dist_bottom_valid = msg.dist_bottom_valid
            self.dist_bottom_sensor_bitfield = msg.dist_bottom_sensor_bitfield

            self.eph = msg.eph
            self.epv = msg.epv
            self.evh = msg.evh
            self.evv = msg.evv

            self.dead_reckoning = msg.dead_reckoning
            self.vxy_max = msg.vxy_max
            self.vz_max = msg.vz_max
            self.hagl_min = msg.hagl_min
            self.hagl_max = msg.hagl_max

    def global_pos_cb(self, msg : VehicleGlobalPosition):
        with self.lock:
            self.timestamp = msg.timestamp
            self.timestamp_sample = msg.timestamp_sample
            self.lat = msg.lat
            self.lon = msg.lon
            self.alt = msg.alt
            self.alt_ellipsoid = msg.alt_ellipsoid
            self.delta_alt = msg.delta_alt
            self.lat_lon_reset_counter = msg.lat_lon_reset_counter
            self.alt_reset_counter = msg.alt_reset_counter
            self.eph_global = msg.eph
            self.epv_global = msg.epv
            self.terrain_alt = msg.terrain_alt
            self.terrain_alt_valid = msg.terrain_alt_valid
            self.dead_reckoning_global = msg.dead_reckoning

    def sensor_cb(self, msg: SensorCombined):
        self.latest_sensor = msg
        # self.publish_state()

    def status_cb(self, msg: VehicleStatus):
        self.latest_status = msg
        # self.publish_state()

    def publish_state(self):
        with self.lock:
            msg = UavState()
            now = self.node.get_clock().now().to_msg()
            msg.header = Header()
            msg.header.stamp = now
            msg.header.frame_id = f"uav_{self.uav_id}"

            msg.timestamp = self.node.get_clock().now().nanoseconds // 1000
            msg.id = self.uav_id

            # PX4 Status
        if self.latest_status:
            msg.mavtype = self.latest_status.system_type  # MAV_TYPE_xxx
            msg.autopilot = 12  # MAV_AUTOPILOT_PX4，若你知道是 PX4
            msg.base_mode = 0   # 无合适字段来源，设为0或根据需要修改
            msg.custom_mode = self.latest_status.nav_state  # 也许更合理将 nav_state 作为模式标志
            msg.system_status = 0  # 无明确映射，可自定义规则或设为0
            
            msg.connected = 1  # 暂时设为始终连接，或根据心跳等机制更新
            msg.is_armed = 1 if self.latest_status.arming_state == self.latest_status.ARMING_STATE_ARMED else 0


            # 电池电量（从 sensor_cb 中更新 
            # No battery in Gazebo
            #
            # if self.latest_sensor:
            #     msg.bat_voltage = self.latest_sensor.battery_voltage
            #     msg.bat_remaining = self.latest_sensor.battery_remaining


            # SensorCombined data
            if self.latest_sensor:
                msg.gyro_rad = self.latest_sensor.gyro_rad
                msg.gyro_integral_dt = self.latest_sensor.gyro_integral_dt
                msg.accelerometer_m_s2 = self.latest_sensor.accelerometer_m_s2
                msg.accelerometer_integral_dt = self.latest_sensor.accelerometer_integral_dt
                msg.accelerometer_clipping = self.latest_sensor.accelerometer_clipping
                msg.gyro_clipping = self.latest_sensor.gyro_clipping
            else:
                msg.gyro_rad = [0.0, 0.0, 0.0]
                msg.gyro_integral_dt = 0
                msg.accelerometer_m_s2 = [0.0, 0.0, 0.0]
                msg.accelerometer_integral_dt = 0
                msg.accelerometer_clipping = 0
                msg.gyro_clipping = 0

            # Local Position
            msg.xy_valid = self.xy_valid
            msg.z_valid = self.z_valid
            msg.v_xy_valid = self.v_xy_valid
            msg.v_z_valid = self.v_z_valid

            msg.x = self.x
            msg.y = self.y
            msg.z = self.z
            msg.vx = self.vx
            msg.vy = self.vy
            msg.vz = self.vz
            msg.ax = self.ax
            msg.ay = self.ay
            msg.az = self.az

            msg.heading = self.heading
            msg.delta_heading = self.delta_heading
            msg.heading_good_for_control = self.heading_good_for_control

            # Global Position
            msg.lat = self.lat
            msg.lon = self.lon
            msg.alt = self.alt
            msg.eph = self.eph_global
            msg.epv = self.epv_global
            msg.terrain_alt = self.terrain_alt
            msg.terrain_alt_valid = self.terrain_alt_valid
            msg.dead_reckoning = self.dead_reckoning_global

            self.state_pub.publish(msg)

    def publish_odom(self):
        odom = Odometry()
        odom.header = Header()
        odom.header.stamp = self.node.get_clock().now().to_msg()
        odom.header.frame_id = 'odom'
        odom.child_frame_id = 'base_link'

        odom.pose.pose.position.x = float(self.x)
        odom.pose.pose.position.y = float(self.y)
        odom.pose.pose.position.z = float(self.z)       
        odom.pose.pose.orientation = Quaternion(x=float(self.q[0]), y=float(self.q[1]), z=float(self.q[2]), w=float(self.q[3]))     # TODO

        odom.twist.twist.linear.x = float(self.vx)
        odom.twist.twist.linear.y = float(self.vy)
        odom.twist.twist.linear.z = float(self.vz)
        if self.latest_sensor != None:
            odom.twist.twist.angular.x = float(self.latest_sensor.gyro_rad[0])                                                      # TODO
            odom.twist.twist.angular.y = float(self.latest_sensor.gyro_rad[1])
            odom.twist.twist.angular.z = float(self.latest_sensor.gyro_rad[2])

        self.odom_pub.publish(odom)

    def set_arm_disarm_from_overall_cmd(self, msg: UavCmd):
        """根据 UAVCmd 控制 arm/disarm"""
        if msg.id not in [-1, self.uav_id]:
            return

        # if msg.is_arm == 0:
        #     return

        if msg.is_arm == 1:
            self.arm()
        else:
            self.disarm()
        self.engage_offboard_mode()

    def publish_vehicle_command(self, command, **params) -> None:
        """Publish a vehicle command."""
        msg = VehicleCommand()
        msg.command = command
        msg.param1 = params.get("param1", 0.0)
        msg.param2 = params.get("param2", 0.0)
        msg.param3 = params.get("param3", 0.0)
        msg.param4 = params.get("param4", 0.0)
        msg.param5 = params.get("param5", 0.0)
        msg.param6 = params.get("param6", 0.0)
        msg.param7 = params.get("param7", 0.0)
        msg.target_system    = self.uav_id + 1      # self.system_id
        msg.target_component = self.component_id
        msg.source_system    = self.uav_id + 1      # self.system_id
        msg.source_component = self.component_id
        msg.from_external = True
        msg.timestamp = int(self.node.get_clock().now().nanoseconds / 1000)
        self.cmd_pub.publish(msg)

    def arm(self):
        """Send an arm command to the vehicle."""
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=1.0)
        self.node.get_logger().info('Arm command sent ...')

    def disarm(self):
        """Send a disarm command to the vehicle."""
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=0.0)
        self.node.get_logger().info('Disarm command sent ...')

    def engage_offboard_mode(self):
        """Switch to offboard mode."""
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_DO_SET_MODE, param1=1.0, param2=6.0)
        self.node.get_logger().info("Switching to offboard mode")

    def land(self):
        """Switch to land mode."""
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_NAV_LAND)
        self.node.get_logger().info("Switching to land mode")

    def publish_offboard_control_heartbeat_signal(self, control_type=None):
        if control_type == None:
            control_type = self.current_ctrl_mode

        msg = OffboardControlMode()
        msg.timestamp = int(self.node.get_clock().now().nanoseconds / 1000)

        # 默认全部设为 False
        msg.position = False
        msg.velocity = False
        msg.acceleration = False
        msg.attitude = False
        msg.body_rate = False

        # 设置你想要的控制模式
        if control_type == 'position':
            msg.position = True
        elif control_type == 'velocity':
            msg.velocity = True
        elif control_type == 'acceleration':
            msg.acceleration = True
        elif control_type == 'attitude':
            msg.attitude = True
        elif control_type == 'body_rate':
            msg.body_rate = True
        else:
            self.node.get_logger().warn(f"[UAV {self.uav_id}] Unknown control_type: {control_type}, using default 'velocity'")
            msg.velocity = True  # fallback 默认使用 velocity 控制

        self.offboard_pub.publish(msg)


    def uav_bridge_main(self):
        #
        # Main function
        self.publish_state()

        self.publish_odom()

        # Critical
        if self.bridge_main_cntr % 25 == 0:
            self.publish_offboard_control_heartbeat_signal()

        self.bridge_main_cntr += 1
        if self.bridge_main_cntr >= 100:
            self.bridge_main_cntr = 0


class MultiUavBridgeNode(Node):
    def __init__(self):
        super().__init__('multi_uav_bridge')
        self.declare_parameter('uav_ids', [1])
        uav_ids = self.get_parameter('uav_ids').get_parameter_value().integer_array_value

        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.bridges = []
        for uid in uav_ids:
            bridge = UavBridge(self, uid)
            self.bridges.append(bridge)

        self.create_subscription(UavCmd, '/uav_cmd', self.cmd_handler, qos)      # 无人机的解锁命令是一起收的
        self.get_logger().info(f"Started bridge for UAVs: {uav_ids}")

    def cmd_handler(self, msg: UavCmd):
        for b in self.bridges:
            b.set_arm_disarm_from_overall_cmd(msg)
            self.get_logger().info(f"[Gazebo Bridge] Received UAV command: id: {msg.id} / is_arm: {msg.is_arm}")

def main(args=None):
    rclpy.init(args=args)
    node = MultiUavBridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
