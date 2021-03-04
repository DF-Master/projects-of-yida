# 导入模块

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

# 定义默认变量
tempsetdefault = 30  # 默认温度设定值应当是一个最多为1位小数、最高位为百位的数字
waittimedefault = 3  # 默认温度测定等待时间，以秒为单位，0.5 s 以下的过快访问会导致不出结果？ 因为远程通讯需要时间，寄存器可能来不及反应，建议不要太快
comdefault = 'COM3'


# 定义环境变量
startprogram = False
uiini = True
temprev = 0
datarev = 0
tempset = 0
waitinglist = 1
waittime = waittimedefault
timelog = time.time()


# 根据字符串产生CRC代码并将其拼接为命令
# CRC 计算代码 https://www.jianshu.com/p/568ac2b3f442
def calc_crc(string):
    data = bytearray.fromhex(string)
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for i in range(8):
            if ((crc & 1) != 0):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return hex(((crc & 0xff) << 8) + (crc >> 8))[2:].zfill(4)

# 将字符串去掉特定字母并加和


def Str_Join(string, icon=' ', newicon=''):
    list = string.split(icon)
    newstring = newicon.join(list)
    return newstring

# 将这两个命令合二为一


def Add_CRC(stringnoCRC):
    stringnoCRC_join = Str_Join(stringnoCRC)
    crc = calc_crc(stringnoCRC)
    newstring = stringnoCRC + ' ' + crc[-4:-2] + ' ' + crc[-2:]
    return newstring

#输出当前时间
def NowTime():
    return(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S'))) #%Y-%m-%d  %H:%M:%S


# 定义输入部分
ser = serial.Serial()

# 串口初始化


def initSerial():
    global ser
    ser.baudrate = 9600
    #ser.port = '/dev/ttyUSB0'
    ser.port = comdefault
    #ser.timeout =0
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0


# 测温模块 https://sunmker.cn/serial_interface/
def DetectTemp(waittime=waittimedefault):  # 返回的值是temprev
    global ser, temprev
    if seropen == True:
        # 产生查询温度测定值命令
        readtemt = '01 03 10 01 00 01 D1 0A'
        readtemt16bit = bytes.fromhex(readtemt)
        # print(readtemt16bit)

        # 串口发送数据
        result = ser.write(readtemt16bit)

        # 停止、等待数据，这一步非常关键。timeout压根没用
        # inwaiting: Get the number of bytes in the input buffer
        time.sleep(waittime)
        count = ser.inWaiting()

        # 数据的接收
        if count > 0:
            data = ser.read(count)
            if data != b'':
                # 将接受的16进制数据格式如b'h\x12\x90xV5\x12h\x91\n4737E\xc3\xab\x89hE\xe0\x16'
                #                      转换成b'6812907856351268910a3437333745c3ab896845e016'
                #                      通过[]去除前后的b'',得到我们真正想要的数据
                print("receive", str(binascii.b2a_hex(data))[2:-1])
                temprev = int(
                    str(str(binascii.b2a_hex(data))[2:-1][-8:-4:]), 16)/10
                print(temprev)

# 设置温度模块


def SetTemp(tempset=tempsetdefault):
    global ser
    if seropen == True:

        # 根据设定温度产生16进制命令
        tempset16bit = hex(tempset*10)[2:].zfill(4)
        tempsetordernoCRC = str(
            '01 06 00 00 ' + tempset16bit[0:2] + ' ' + tempset16bit[-2:])
        tempsetorder = bytes.fromhex(Add_CRC(tempsetordernoCRC))

        # 串口发送数据
        print(tempsetorder)
        ser.write(tempsetorder)  # 向仪器输入温度设定命令

# 设置数据模块


def SetData(hrnumber, dataset):
    global ser
    if seropen == True:
        # 根据设定温度产生16进制命令
        dataset16bit = hex(dataset)[2:].zfill(4)
        datasetordernoCRC = str(
            '01 06 ' + hrnumber[0:2] + ' ' + hrnumber[2:] + ' ' + dataset16bit[0:2] + ' ' + dataset16bit[-2:])
        datasetorder = bytes.fromhex(Add_CRC(datasetordernoCRC))

        # 串口发送数据
        print(Add_CRC(datasetordernoCRC))
        print(datasetorder)
        ser.write(datasetorder)  #


# 检测仪器数据模块


def DetectSet(hrnumer='0000', waittime=waittimedefault):  # 返回值是datarev
    global serial, datarev
    if seropen == True:

        # 产生查询命令
        detectsetordernoCRC = str(
            '01 03 ' + hrnumer[0:2] + ' ' + hrnumer[-2:] + ' 00 01')
        detectsetorder = bytes.fromhex(Add_CRC(detectsetordernoCRC))

        # 串口发送数据
        print(detectsetorder)
        ser.write(detectsetorder)

    # 停止、等待数据，这一步非常关键。timeout压根没用
        # inwaiting: Get the number of bytes in the input buffer
        time.sleep(waittime)
        count = ser.inWaiting()

        # 数据的接收
        if count > 0:
            data = ser.read(count)
            if data != b'':
                # 将接受的16进制数据格式如b'h\x12\x90xV5\x12h\x91\n4737E\xc3\xab\x89hE\xe0\x16'
                #                      转换成b'6812907856351268910a3437333745c3ab896845e016'
                #                      通过[]去除前后的b'',得到我们真正想要的数据
                print("receive", str(binascii.b2a_hex(data))[2:-1])
                datarev = int(
                    str(str(binascii.b2a_hex(data))[2:-1][-8:-4:]), 16)/10
                print(datarev)


# 向datalog.csv文件写入一行数据
def WriteLine(element1, element2, element3, csvfile='./temp-control/datalog.csv'):
    with open(csvfile, "a", newline='') as csvfile_edit:
        csv.writer(csvfile_edit).writerow([element1, element2, element3])


# 产生UI界面


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        # 初始化
        super().__init__()
        self.setWindowTitle('温控仪 by yida --UI')
        self.setupUi(self)  # UI文件在先前的import已有定义
        

        # 打开多线程，利用多线程读取实时测得的温度与实时的温度设置（在实验中，设定温度一般为常数，考虑到设定温度可能是渐变函数的存在，这里保留实时更新功能）
        self.threadtemprev = ThreadTempRev()
        self.threadtemprev.start()
        self.threadtempset = ThreadTempSet()
        self.threadtempset.start()

        # 信号与槽函数的连接
        ##
        self.threadtemprev.sinOut.connect(self.TextTemprevChange)
        self.threadtempset.sinOut.connect(self.TextTempsetChange)
        # 按钮与函数进行关联
        self.pbstart.clicked.connect(self.StartProgram)
        self.pbstop.clicked.connect(self.StopProgram)
        self.pbadjust.clicked.connect(self.AdjustTempSet)
        

    # 文本框显示观测值
    def TextTemprevChange(self, str):
        self.texttemprev.setText(str)

    def TextTempsetChange(self, str):
        self.texttempset.setText(str)

    # 按钮的关联函数
    def StartProgram(self):
        global startprogram, datarev, temprev, waittime
        print("开始初始化")
        QMessageBox.information(self,'提示','开始初始化，请耐心等待。')
        startprogram = False #杀后台    
        #初始化仪表盘 --显示检测数据
        DetectTemp()
        sleep(waittime) # 防止寄存器故障
        self.texttemprev.setText(str(temprev))
        DetectSet()
        sleep(waittime)  # 防止寄存器故障
        self.texttempset.setText(str(datarev))
        DetectSet(hrnumer='0004')  # KP的仪器地址（参考说明书）是0004
        sleep(waittime)  # 防止寄存器故障
        kp=str(datarev*10) 
        self.KP.setText(kp)  # DetectSet步骤中除以了10
        DetectSet(hrnumer='0005')  # KD的仪器地址（参考说明书）是0005
        ki = str(datarev*10) 
        sleep(waittime)  # 防止寄存器故障
        self.KI.setText(ki)
        DetectSet(hrnumer='0006')  # KD的仪器地址（参考说明书）是0006
        sleep(waittime)
        kd = str(datarev*10)
        self.KD.setText(kd)
        #将配置参数写入statuslog.csv中
        WriteLine('KP',str(kp),NowTime(),csvfile="./temp-control/statuslog.csv")
        WriteLine('KI',str(ki),NowTime(),csvfile="./temp-control/statuslog.csv")
        WriteLine('KD',str(kd),NowTime(),csvfile="./temp-control/statuslog.csv")
        QMessageBox.information(self,'提示','初始化完成。')

        startprogram = True
        # 获得所有数据的初始值

    def StopProgram(self):
        global startprogram
        startprogram = False
        QMessageBox.information(self,'提示','已停止程序。')

    def AdjustTempSet(self):
        global waittimedefault
        waittime = waittimedefault
        tempset = int(float(self.texttempset.toPlainText()))
        kpset = int(float(self.KP.toPlainText()))
        kiset = int(float(self.KI.toPlainText()))
        kdset = int(float(self.KD.toPlainText()))
        print(tempset)
        SetTemp(tempset)
        sleep(waittime)
        SetData('0004', kpset)
        sleep(waittime)
        SetData('0005', kiset)
        sleep(waittime)
        SetData('0006', kdset)
        waittime = 1
        print("adjust finish")
        QMessageBox.information(self,'提示','调整完成')



# 引入一些消息框 抄的 https://blog.csdn.net/lb0737/article/details/84318847
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *





# 利用多線程输出温度测定值和设定值


class ThreadTempRev(QThread):
    sinOut = pyqtSignal(str)
    # 初始化

    def ___init__(self):
        super(Thread, self).__init__()

    def run(self):
        # 线程相关的代码
        global startprogram, temprev, waittime, waitinglist
        while True:
            if startprogram == True and waitinglist == 1:
                DetectTemp()
                self.sinOut.emit(str(temprev))
                waitinglist = 2  # 下一步为读取设定温度值

            sleep(waittime)


class ThreadTempSet(QThread):
    sinOut = pyqtSignal(str)

    def ___init__(self):
        super(Thread, self).__init__()

    def run(self):
        # 线程相关的代码
        global startprogram, temprev, datarev, waittime, waitinglist
        while True:
            if startprogram == True and waitinglist == 2:
                DetectSet()
                self.sinOut.emit(str(datarev))
                waitinglist = 1  # 下一步为读取实时温度
                # 将结果保存进csv
                WriteLine(str(temprev), str(datarev), NowTime())  # 将结果保存入CSV的最后一行 

            sleep(waittime)


# 主程序
if __name__ == "__main__":
    # 初始化datalog.csv,statuslog.csv
    dataframe = pd.DataFrame({'TempRev': [], 'TempSet': [], 'TimeLog': []})
    ## 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("temp-control\datalog.csv", index=False, sep=',')
    ##同理
    dataframe = pd.DataFrame({'Name': [], 'Data': [], 'TimeLog': []})
    dataframe.to_csv("temp-control\statuslog.csv", index=False, sep=',')
    ## 为后者增加第一行数据以防出错
    WriteLine('KP','0',NowTime(),csvfile="./temp-control/statuslog.csv")
    WriteLine('KI','0',NowTime(),csvfile="./temp-control/statuslog.csv")
    WriteLine('KD','0',NowTime(),csvfile="./temp-control/statuslog.csv")


    # 初始化串口
    initSerial()
    ser.open()
    seropen = True
    # 产生UI
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    
    

    sys.exit(app.exec_())
    

 
