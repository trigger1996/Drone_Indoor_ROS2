#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math

class PID_Incremental:
    def __init__(self, ref, kp, ki, kd, min_u=None, max_u=None):
        self.ref = ref  # 参考值
        self.kp = kp  # 参数KP
        self.ki = ki  # 参数KI
        self.kd = kd  # 参数KD
        self.u_last = 0.  # 上一时刻的输出
        self.e_1 = 0.  # 上一时刻的误差
        self.e_2 = 0.  # 上上时刻的误差
        self.min_u = min_u
        self.max_u = max_u
        self.u = 0.
        self.delta_u = 0.
        pass
    
    def get_new_ctrl(self, fbk):
        e_k = self.ref - fbk
        term1 = self.kp * (e_k - self.e_1)
        term2 = self.ki * e_k
        term3 = self.kd * (e_k - 2*self.e_1 + self.e_2)
        self.delta_u = term1 + term2 + term3
        # 更新误差
        self.e_2 = self.e_1
        self.e_1 = e_k
        self.u = self.u_last + self.delta_u
        self.__pid_saturation()
        self.u_last = self.u
        return self.u
    
    def __pid_saturation(self):
        if not self.min_u is None:
            self.u = max(self.u, self.min_u)
        if not self.max_u is None:
            self.u = min(self.u, self.max_u)

class PID_Position:
    def __init__(self, ref, kp, ki, kd, min_u=None, max_u=None):
        self.ref = ref  # 参考值
        self.kp = kp  # 参数KP
        self.ki = ki  # 参数KI
        self.kd = kd  # 参数KD
        self.error_int = 0.  # 上一时刻的输出
        self.e_1 = 0.  # 上一时刻的误差
        self.e_2 = 0.  # 上上时刻的误差
        self.min_u = min_u
        self.max_u = max_u
        self.u = 0.
        self.delta_u = 0.
        pass
    
    def get_new_ctrl(self, fbk):
        e_k = self.ref - fbk
        self.error_int += e_k
        term1 = self.kp * e_k
        term2 = self.ki * self.error_int
        term3 = self.kd * (e_k - self.e_1)
        self.u = term1 + term2 + term3
        # 更新误差
        self.e_2 = self.e_1
        self.e_1 = e_k
        self.__pid_saturation()
        self.u_last = self.u
        return self.u
    
    def __pid_saturation(self):
        if not self.min_u is None:
            self.u = max(self.u, self.min_u)
        if not self.max_u is None:
            self.u = min(self.u, self.max_u)
            
            
if __name__ == "__main__":
    pidx = PID_Position(2, 1, 0.0001, 0.003, -0.3, 0.3)
    # system x_dot = u
    # desired x: 1
    # u=PID(x)
    x = 0
    xs = []
    iss = []
    for i in range(1000):
        u1 = pidx.get_new_ctrl(x)
        x = x + 0.01 * u1
        if i%10 == 0:
            xs.append(x)
            iss.append(0.01*i)
    # plot
    import matplotlib.pyplot as plt
    plt.plot(iss,xs)
    plt.show()
