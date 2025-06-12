#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
import yaml
import time
from collections import OrderedDict

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from drone_ros2_centralized_control.msg import UavCmd, UavState  # 自定义消息类型
from transforms3d.euler import quat2euler

from utils2.vis import print_c, format_logger
from utils2.PID import PID_Position
from utils2.functions import saturation, dead_zone

import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

from functools import cmp_to_key
from subprocess import check_output
from MDP_Planner.Map.example_20250506_grid_single_agent import construct_single_agent_mdp, observation_func_0506, control_observable_dict
from MDP_Planner.Map.example_20250506_team_mdp import run_2_observations_seqs, observation_seq_2_inference, calculate_cost_from_runs    # TODO
from MDP_Planner.MDP_TG.mdp import Motion_MDP
from MDP_Planner.MDP_TG.dra import Dra
from MDP_Planner.MDP_TG.lp  import syn_full_plan_rex
from MDP_Planner.User.dra3 import product_mdp3
from MDP_Planner.User.lp3  import synthesize_full_plan_w_opacity3
from MDP_Planner.User.grid_utils import sort_team_numerical_states
from MDP_Planner.User.vis2 import print_c, print_colored_sequence, print_highlighted_sequences
from MDP_Planner.User.plot import plot_cost_hist, plot_cost_hists_multi


UAV_SPEED_X_DEAD_ZONE = 0.0
UAV_MAX_SPEED_X = 1.0
UAV_MAX_SPEED_Y = 1.0
UAV_MAX_SPEED_Z = 2.0


#
# --------------------------------------------------------------------------------------------------
class Case_20250506_single_agent:
    def __init__(self):
        pass


    def ltl_convert(self, task, is_display=True):
        #
        # https://www.ltl2dstar.de/docs/ltl2dstar.html#:~:text=ltl2dstar%20is%20designed%20to%20use%20an%20external%20tool%20to%20convert
        # LTL是有两个格式的, 一个ltl2dstar notation, 一个spin notation
        # 后者是常用的, 要从后者转到前者ltl2dstar才能用
        cmd_ltl_convert = 'ltlfilt -l -f \'%s\'' % (task, )
        ltl_converted = str(check_output(cmd_ltl_convert, shell=True))
        ltl_converted = ltl_converted[2 : len(ltl_converted) - 3]               # tested
        if is_display:
            print_c('converted ltl: ' + ltl_converted)

        return ltl_converted

    def obtain_all_aps_from_team_mdp(self, mdp:Motion_MDP, is_convert_to_str=True, is_remove_empty_ap=True):
        ap_list = []
        for state_t in mdp.nodes():
            state_attr_t = mdp.nodes()[state_t]
            label_t = state_attr_t['label']
            for ap_t in list(state_attr_t['label'])[0]:
                #
                # Added
                if is_convert_to_str and type(ap_t) == frozenset:
                    ap_t = list(ap_t)
                    if not ap_t.__len__():
                        ap_t = ''
                    else:
                        ap_t = ap_t[0]
                #
                ap_list.append(ap_t)

        ap_list = list(set(ap_list))
        if is_remove_empty_ap:
            if '' in ap_list:
                ap_list.remove('')
            if ' ' in ap_list:
                ap_list.remove(' ')

        ap_list = list(set(ap_list))
        ap_list.sort()
        return ap_list

    def print_best_all_plan(self, best_all_plan):
        # Added
        # for printing policies
        if best_all_plan.__len__() >= 4 and best_all_plan[3].__len__():
            print_c("optimal AP: %s" % (best_all_plan[3][0], ), color=47)
        print_c("state action: probabilities")
        print_c("Prefix", color=42)
        #
        state_in_prefix = [ state_t for state_t in best_all_plan[0][0] ]
        state_in_prefix.sort(key=cmp_to_key(sort_team_numerical_states))
        #for state_t in best_all_plan[0][0]:
        for state_t in state_in_prefix:
            print_c("%s, %s: %s" % (str(state_t), str(best_all_plan[0][0][state_t][0]), str(best_all_plan[0][0][state_t][1]), ), color=42)
        #
        print_c("Suffix", color=45)
        state_in_suffix = [ state_t for state_t in best_all_plan[1][0] ]
        state_in_suffix.sort(key=cmp_to_key(sort_team_numerical_states))
        #for state_t in best_all_plan[1][0]:
        for state_t in state_in_suffix:
            print_c("%s, %s: %s" % (str(state_t), str(best_all_plan[1][0][state_t][0]), str(best_all_plan[1][0][state_t][1]), ), color=45)

    def execute_example_4_product_mdp3(self, N, total_T, prod_dra, best_all_plan, state_seq, label_seq, opt_prop, ap_gamma, attr='opaque'):
        XX  = []
        LL  = []
        UU  = []
        MM  = []
        OXX = []
        cost_list_pi = []
        cost_list_gamma = []
        for n in range(0, N):
            X, OX, O, X_OPA, L, OL, U, M = prod_dra.execution_in_observer_graph(total_T)

            XX.append(X)
            LL.append(L)
            UU.append(U)
            MM.append(M)
            OXX.append(OX)

        print('[Product Dra] process all done')

        color_init = 32
        for i in range(0, XX.__len__()):
            X_U = []
            for j in range(0, XX[i].__len__()):
                X_U.append(XX[i][j])
                if j < XX[i].__len__() - 1:
                    X_U.append(UU[i][j])
            #
            Y = run_2_observations_seqs(X_U)
            X_INV, AP_INV = observation_seq_2_inference(Y)
            #
            cost_cycle = calculate_cost_from_runs(prod_dra, XX[i], LL[i], UU[i], opt_prop)
            cost_list_pi = cost_list_pi + cost_cycle
            #
            cost_cycle_p = calculate_cost_from_runs(prod_dra, XX[i], LL[i], UU[i], ap_gamma)
            cost_list_gamma = cost_list_gamma + cost_cycle_p
            #
            # print_c(X_U, color=color_init)
            # print_c(Y, color=color_init)
            # print_c(X_INV, color=color_init)
            # print_c(AP_INV, color=color_init)
            # print_c("[cost / achieved_index] " + str(cost_cycle), color=color_init)
            # color_init += 1
            #
            print_colored_sequence(X_U)
            print_colored_sequence(Y)
            print_colored_sequence(X_INV)
            print_colored_sequence(AP_INV)
            print_c("[cost / achieved_index] " + str(cost_cycle), color=color_init)
            #
            print_highlighted_sequences(X_U, Y, X_INV, AP_INV, marker1=opt_prop, marker2=ap_gamma, attr=attr)
        # fig = visualize_run_sequence(XX, LL, UU, MM, 'surv_result', is_visuaize=False)

        return cost_list_pi, cost_list_gamma

    def execute_example_in_origin_product_mdp(self, N, total_T, prod_dra, best_all_plan, state_seq, label_seq, opt_prop, ap_gamma, attr):
        XX = []
        LL = []
        UU = []
        MM = []
        PP = []
        for n in range(0, N):
            X, L, U, M, PX = prod_dra.execution(best_all_plan, total_T, state_seq, label_seq)

            XX.append(X)
            LL.append(L)
            UU.append(U)
            MM.append(M)
            PP.append(PX)

        print('[Product Dra] process all done')

        cost_list_pi = []
        cost_list_gamma = []
        color_init = 32
        for i in range(0, XX.__len__()):
            X_U = []
            for j in range(0, XX[i].__len__()):
                X_U.append(XX[i][j])
                if j < XX[i].__len__() - 1:
                    X_U.append(UU[i][j])
            #
            Y = run_2_observations_seqs(X_U)
            X_INV, AP_INV = observation_seq_2_inference(Y)
            #
            cost_cycle = calculate_cost_from_runs(prod_dra, XX[i], LL[i], UU[i], opt_prop)
            cost_list_pi = cost_list_pi + cost_cycle
            #
            cost_cycle_p = calculate_cost_from_runs(prod_dra, XX[i], LL[i], UU[i], ap_gamma)
            cost_list_gamma = cost_list_gamma + cost_cycle_p
            #
            # print_c(X_U, color=color_init)
            # print_c(Y, color=color_init)
            # print_c(X_INV, color=color_init)
            # print_c(AP_INV, color=color_init)
            # print_c("[cost / achieved_index] " + str(cost_cycle), color=color_init)
            # color_init += 1
            #
            print_colored_sequence(X_U)
            print_colored_sequence(Y)
            print_colored_sequence(X_INV)
            print_colored_sequence(AP_INV)
            print_c("[cost / achieved_index] " + str(cost_cycle), color=color_init)
            #
            print_highlighted_sequences(X_U, Y, X_INV, AP_INV, marker1=opt_prop, marker2=ap_gamma, attr=attr)
        # fig = visualize_run_sequence(XX, LL, UU, MM, 'surv_result', is_visuaize=False)

        return cost_list_pi, cost_list_gamma

    def optimal_synthesis(self):
        mdp, initial_node, initial_label, node_positions = construct_single_agent_mdp(is_visualize=True)
        ap_list                                          = self.obtain_all_aps_from_team_mdp(mdp)

        # ltl_formula = 'GF (gather -> drop)'
        ltl_formula = 'GF (gather -> (!gather U drop))'  # 'GF (gather -> X(!gather U drop))'
        opt_prop = 'gather'
        ltl_formula_converted = self.ltl_convert(ltl_formula)

        dra = Dra(ltl_formula_converted)

        t42 = time.time()

        # ------
        gamma = 0.5
        d = 100
        risk_threshold = 0.05  # default:  0.1
        differential_exp_cost = 15  # 1.590106
        is_run_opaque_synthesis = True
        if is_run_opaque_synthesis:
            best_all_plan, prod_dra_pi = synthesize_full_plan_w_opacity3(mdp, ltl_formula, opt_prop, ap_list,
                                                                        risk_threshold,
                                                                        differential_exp_cost,
                                                                        observation_func=observation_func_0506,
                                                                        ctrl_obs_dict=control_observable_dict)
        ap_gamma = best_all_plan[3][0]

        prod_dra = product_mdp3(mdp, dra)
        best_all_plan_p = syn_full_plan_rex(prod_dra, gamma, d)
        # best_all_plan_p = syn_full_plan_repeated(prod_dra, gamma, opt_prop)

        # print_best_all_plan(best_all_plan)
        #
        # # for visualization
        total_T = 150
        state_seq = [initial_node, ]
        label_seq = [initial_label, ]
        N = 5
        is_average = True
        #
        # #
        # # Opaque runs
        if is_run_opaque_synthesis:
            # try:
            # TODO
            if True:
                cost_list_pi, cost_list_gamma = self.execute_example_4_product_mdp3(N, total_T, prod_dra_pi, best_all_plan,
                                                                                    state_seq, label_seq, opt_prop, ap_gamma,
                                                                                    attr='Opaque')

                plot_cost_hist(cost_list_pi, bins=25, is_average=is_average,
                            title="Cost for Satisfaction of AP \pi in Opaque runs")
                plot_cost_hist(cost_list_gamma, bins=25, color='r', is_average=is_average,
                            title="Cost for Satisfaction of AP \gamma in Opaque runs")
                plot_cost_hists_multi(cost_list_pi, cost_list_gamma, bins=25, colors=['r', 'magenta'], labels=['\pi', '\gamma'], is_average=is_average,
                                    title="Cost for Satisfaction of APs in Opaque runs")

                # TODO
                # except:
                print_c("No best plan synthesized, try re-run this program", color=33)

        #
        print_c("\n\nFOR COMPARASION, NON_OPAQUE SYNTHESIS: \n", color=46)
        self.print_best_all_plan(best_all_plan_p)

        #
        # Non-opaque runs
        # try:
        state_seq = [initial_node, ]
        label_seq = [initial_label, ]
        if True:
            cost_list_pi_p, cost_list_gamma_p = self.execute_example_in_origin_product_mdp(N, total_T, prod_dra, best_all_plan_p,
                                                                                           state_seq, label_seq, opt_prop,
                                                                                           ap_gamma, attr='Opaque')
        # except:
        #     print_c("No best plan synthesized, try re-run this program", color=33)
        # is_average = True
        plot_cost_hist(cost_list_pi_p, bins=25, color='b', is_average=is_average,
                    title="Cost for Satisfaction of AP \pi in NON-Opaque runs")
        plot_cost_hist(cost_list_gamma_p, bins=25, color='cyan', is_average=is_average,
                    title="Cost for Satisfaction of AP \gamma in NON-Opaque runs")
        plot_cost_hists_multi(cost_list_pi_p, cost_list_gamma_p, bins=25, colors=['b', 'cyan'], labels=['\pi', '\gamma'], is_average=is_average,
                            title="Cost for Satisfaction of APs in Opaque runs")

        # TODO 对比实验
        # 我的问题是, 入侵者到底拿到的是什么数据
        # 进而, 如何通过实验现象来描述opacity

        # TODO
        # draw_action_principle()
        # draw_mdp_principle()

        #
        #
        plt.show()

#
# --------------------------------------------------------------------------------------------------
class MultiDroneController(Node):

    def __init__(self):
        super().__init__('multi_drone_control')

        self.mdp_planner = Case_20250506_single_agent()

        self.declare_parameter('drone_id', 1)
        self.declare_parameter('map_file', '')
        ctrl_dt = 0.1

        drone_id = self.get_parameter('drone_id').get_parameter_value().integer_value
        self.drone_id = drone_id

        ns = f"/px4_{self.drone_id}"
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # PID 控制器
        self.pid_x = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_X, UAV_MAX_SPEED_X)
        self.pid_y = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_Y, UAV_MAX_SPEED_Y)
        self.pid_z = PID_Position(0, 1.0, 0., 0.0, ctrl_dt, -UAV_MAX_SPEED_Z, UAV_MAX_SPEED_Z)

        # UAV 状态变量
        self.uav_pose = Odometry()
        self.uav_state = UavState()
        self.is_uav_pose_updated = False
        self.is_uav_state_updated = False

        # 订阅与发布
        self.arm_disarm_pub = self.create_publisher(UavCmd, f"/cmd_arm_disarm_{drone_id}", qos)
        self.cmd_vel_pub = self.create_publisher(Twist, f"/cmd_vel_{drone_id}", qos)

        self.create_subscription(Odometry, f"/mavrouter/drone_pose_{drone_id}", self.uav_odom_callback, qos)
        self.create_subscription(UavState, f"/mavrouter/drone_state_{drone_id}", self.uav_state_callback, qos)

        # 加载航点
        map_file = self.get_parameter('map_file').value

        print(f"[UAV{drone_id}] Loading waypoints from {map_file}")
        with open(map_file, 'r') as f:
            self.waypoints = yaml.safe_load(f)['waypoint']

        self.sorted_waypoints = OrderedDict()
        for key in ['4', '1', '3', '5', '6', '2', '7', '8', '9', '10']:
            if key in self.waypoints:
                self.sorted_waypoints[key] = self.waypoints[key]

        # 控制流程变量
        self.create_timer(ctrl_dt, self.control_loop)
        self.start_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.ctrl_cntr = 0
        self.takeoff_duration = 10.0
        self.task_duration = 60.0
        self.target_altitude = 0.8
        self.current_waypoint_index = 0
        self.task_start_time = None
        self.task_flag = False
        self.finished_flag = False

        #
        # Critical
        self.mdp_planner.optimal_synthesis()

        # 自动解锁
        self.get_logger().info(format_logger(f"[UAV{drone_id}] Arming UAV...", color='green', styles='bold'))
        for _ in range(10):
            self.arm_disarm_pub.publish(self.set_arm_disarm_message(True))
            time.sleep(0.1)

    def uav_odom_callback(self, msg):
        self.uav_pose = msg
        self.is_uav_pose_updated = True

    def uav_state_callback(self, msg):
        self.uav_state = msg
        self.is_uav_state_updated = True

    def set_arm_disarm_message(self, arm, disarm=False):
        msg = UavCmd()
        msg.header.stamp = self.get_clock().now().to_msg()
        #msg.id = self.drone_id
        msg.id = -1
        msg.is_arm = 1 if arm else -1 if disarm else 0
        return msg

    def publish_velocity(self, vx, vy, vz):
        twist = Twist()
        twist.linear.x = float(vx)
        twist.linear.y = float(vy)
        twist.linear.z = float(vz)
        self.cmd_vel_pub.publish(twist)

    def calculate_velocity(self, x, y, z, x_tgt, y_tgt, z_tgt):
        self.pid_x.ref = x_tgt
        self.pid_y.ref = y_tgt
        self.pid_z.ref = z_tgt
        vx = saturation(self.pid_x.get_new_ctrl(x), UAV_MAX_SPEED_X, -UAV_MAX_SPEED_X)
        vy = saturation(self.pid_y.get_new_ctrl(y), UAV_MAX_SPEED_Y, -UAV_MAX_SPEED_Y)
        vz = saturation(self.pid_z.get_new_ctrl(z), UAV_MAX_SPEED_Z, -UAV_MAX_SPEED_Z)
        vx = dead_zone(vx, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)
        vy = dead_zone(vy, UAV_SPEED_X_DEAD_ZONE, UAV_SPEED_X_DEAD_ZONE)
        return vx, vy, vz

    def control_loop(self):
        if not self.is_uav_pose_updated:
            self.get_logger().info(format_logger(f"[UAV{self.drone_id}] pose NOT received...", color='yellow'))
            return

        if self.finished_flag:
            return

        now = self.get_clock().now().seconds_nanoseconds()[0] - self.start_time


        if now < self.takeoff_duration:
            # 起飞
            vx, vy, vz = self.calculate_velocity(0., 0., self.uav_pose.pose.pose.position.z, 0., 0., -self.target_altitude)
            self.publish_velocity(vx, vy, vz)
            if int(self.ctrl_cntr) % 10 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Taking off...", color='cyan'))

        elif now < self.takeoff_duration + self.task_duration:
            # 飞行任务
            if not self.task_flag:
                self.task_flag = True
                self.task_start_time = now
                self.waypt_start_time = now
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Mission started...", color='cyan'))

            keys = list(self.sorted_waypoints.keys())
            if self.current_waypoint_index >= len(keys):
                self.get_logger().info(f"[UAV{self.drone_id}] All waypoints reached.")
                return

            elapsed_time = now - self.waypt_start_time

            key = keys[self.current_waypoint_index]
            target = self.sorted_waypoints[key]
            duration = 10                           # TODO

            px = self.uav_pose.pose.pose.position.x
            py = self.uav_pose.pose.pose.position.y
            pz = self.uav_pose.pose.pose.position.z

            vx, vy, vz = self.calculate_velocity(px, py, pz, target[0], target[1], -self.target_altitude)
            self.publish_velocity(vx, vy, vz)

            err_x = target[0] - px
            err_y = target[1] - py
            err_z = self.target_altitude - pz
            dist = math.sqrt(err_x**2 + err_y**2)
            if dist < 0.25 or elapsed_time > duration:
                #
                if dist < 0.25:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Reached waypoint {key}", color='green',  styles='bold'))
                else:
                    self.get_logger().info(format_logger(f"[UAV{self.drone_id}] NOT Reach waypoint {key}, time exceeded", color='yellow', styles='bold'))
                #
                if self.current_waypoint_index < len(keys) - 1:
                    self.current_waypoint_index += 1
                self.waypt_start_time = now  # 重置航点计时

            if int(self.ctrl_cntr) % 20 == 0:
                self.get_logger().info(format_logger(f"[UAV{self.drone_id}] Tgt id:x/y/z: {key}: {target[0]} / {target[1]} / {self.target_altitude} | Fbk x/y/z: {px} / {py} / {pz} | Vel x/y/z: {vx} / {vy} / {vz}", color='blue', styles='italic'))

        elif now < self.task_duration + 5.0:
            # 降落
            err_z = 0.0 - self.uav_pose.pose.pose.position.z
            vx, vy, vz = 0.0, 0.0, saturation(self.pid_z.get_new_ctrl(err_z), UAV_MAX_SPEED_Z, -UAV_MAX_SPEED_Z)
            self.publish_velocity(vx, vy, vz)
            self.get_logger().info(f"[UAV{self.drone_id}] Landing...")

        else:
            # 上锁
            self.arm_disarm_pub.publish(self.set_arm_disarm_message(False, disarm=True))
            self.get_logger().info(f"[UAV{self.drone_id}] Disarmed.")
            self.finished_flag = True

        self.ctrl_cntr += 1

#
# --------------------------------------------------------------------------------------------------

def main(args=None):
    rclpy.init(args=args)
    node = MultiDroneController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
