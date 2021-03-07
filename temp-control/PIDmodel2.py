import matplotlib.pyplot as plt
import matplotlib.collections as mcol
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import csv
import serial
import binascii
import time
import sys
import numpy as np
import pandas as pd
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import temp_ui as ui
import datetime
from time import sleep
from tkinter import messagebox

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# class MyWindow(QWidget):
#     def __init__(self,parent=None):
#         super(MyWindow,self).__init__(parent)
#         self.setWindowTitle("弹出式对话框例子")
#         self.resize(400,200)
#         self.btn1=QPushButton(self)
#         self.btn1.setText("消息框")
#         self.btn1.clicked.connect(self.msg1)
#         layout=QVBoxLayout()

#         self.btn2=QPushButton(self)
#         self.btn2.setText("问答对话框")
#         self.btn2.clicked.connect(self.msg2)

#         self.btn3=QPushButton()
#         self.btn3.setText("警告对话框")
#         self.btn3.clicked.connect(self.msg3)

#         self.btn4=QPushButton()
#         self.btn4.setText("严重错误对话框")
#         self.btn4.clicked.connect(self.msg4)

#         self.btn5=QPushButton()
#         self.btn5.setText("关于对话框")
#         self.btn5.clicked.connect(self.msg5)

#         layout.addWidget(self.btn1)
#         layout.addWidget(self.btn2)
#         layout.addWidget(self.btn3)
#         layout.addWidget(self.btn4)
#         layout.addWidget(self.btn5)

#         self.setLayout(layout)


#     def msg1(self):
#         #使用infomation信息框
#         QMessageBox.information(self,"标题","消息正文",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
#     def msg2(self):
#          QMessageBox.question(self,"标题","问答消息正文",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
#     def msg3(self):
#         QMessageBox.warning(self,"标题","警告消息正文",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
#     def msg4(self):
#         QMessageBox.critical(self,"标题","严重错误消息正文",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
#     def msg5(self):
#         QMessageBox.about(self,"标题","关于消息正文")

# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     win=MyWindow()
#     win.show()
#     sys.exit(app.exec_())


# def WriteLine(element1, element2, element3, csvfile='./temp control/datalog.csv'):
#     with open(csvfile, "a", newline='') as csvfile_edit:
#         csv.writer(csvfile_edit).writerow([element1, element2, element3])


# # 信息框
# QMessageBox.information(self, '框名', '内容', 按钮s, 默认按钮)
# # 问答框
# QMessageBox.question(self, '框名', '内容', 按钮s, 默认按钮)
# # 警告框
# QMessageBox.warning(self, '框名', '内容', 按钮s, 默认按钮)
# # 危险框
# QMessageBox.critical(self, '框名', '内容', 按钮s, 默认按钮)
# # 关于框
# QMessageBox.about(self, '框名', '内容')


import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import os


class PID_Prama:
    def __init__(self):
        self.Kp = 0
        self.Ki = 0
        self.Kd = 0
        self.set_val = 0
        self.error_last = 0
        self.error_prev = 0
        self.error_sum = 0

# 增量计算公式：
# Pout=Kp*[e(t) - e(t-1)] + Ki*e(t) + Kd*[e(t) - 2*e(t-1) +e(t-2)]


def PID_Controller_Increa(pid, out_now):
    error = pid.set_val - out_now
    Res = pid.Kp*(error-pid.error_last) + pid.Ki*error + \
        pid.Kd*(error-2*pid.error_last+pid.error_prev)
    pid.error_prev = pid.error_last
    pid.error_last = error
    return Res


standard_out = 80
Time = 80


def Draw(kp=0.01, ki=0.1, kd=0.05):
    PID_val = PID_Prama()
    # PID参数
    PID_val.Kp = kp
    PID_val.Ki = ki
    PID_val.Kd = kd
    PID_val.set_val = standard_out  # 标准输出值
    # 增量型PID控制器输出值
    PID_Controller_Increa_Out = []
    Sys_In = []
    # 0时刻系统输入值
    Sys_In.append(4)
    # 系统响应函数
    def SystemFunc(x): return 5*x + np.random.normal(0, 0.5, 1)[0]

    Sys_Out = []
    # 0时刻系统输出值
    Sys_Out.append(SystemFunc(Sys_In[0]))

    for t_slice in range(Time):
        Diff = PID_Controller_Increa(PID_val, Sys_Out[t_slice])  # 系统误差
        PID_Controller_Increa_Out.append(Diff)  # 记录所有的系统误差
        # 计算增量之后的新的系统输入
        Sys_In.append(Sys_In[0]+np.sum(PID_Controller_Increa_Out))
        Sys_Out.append(SystemFunc(Sys_In[t_slice+1]))  # 计算下一时刻系统新的输出值

    standard = np.linspace(PID_val.set_val, PID_val.set_val, Time)
    return Sys_Out


plt.figure('PID_Controller_Increa')
plt.xlim(0, Time)
plt.ylim(0, 2*standard_out)
plt.plot(Draw(kp=0.01, ki=0.1, kd=0.05), label='kp=0.01, ki=0.1, kd=0.05')
plt.plot(Draw(kp=0.01, ki=0.1, kd=0.01), label='kp=0.01, ki=0.1, kd=0.01')
plt.plot(Draw(kp=0.01, ki=0.15, kd=0.05), label='kp=0.01, ki=0.15, kd=0.05')
plt.plot(Draw(kp=0.005, ki=0.1, kd=0.05), label='kp=0.005, ki=0.1, kd=0.05')
plt.xlabel('Time', fontsize=18)
plt.ylabel('Temp.', fontsize=18)

plt.legend(loc='upper left', shadow=True, fancybox=True)
plt.show()
