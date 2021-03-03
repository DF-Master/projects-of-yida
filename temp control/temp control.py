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


# 定义默认变量
tempsetdefault = 30  # 默认温度设定值应当是一个最多为1位小数、最高位为百位的数字
waittimedefault = 1  # 默认温度测定等待时间，以秒为单位，0.5 s 以下的过快访问会导致不出结果？
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
    return hex(((crc & 0xff) << 8) + (crc >> 8))

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
def WriteLine(element1,element2,element3,csvfile = './temp control/datalog.csv'):
    with open(csvfile,"a",newline='') as csvfile_edit:
        csv.writer(csvfile_edit).writerow([element1, element2,element3])
        
        
        



# 产生UI界面


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        # 初始化
        super().__init__()
        self.setWindowTitle('温控仪 by yida --UI')
        self.setupUi(self) #UI文件在先前的import已有定义

        
        
        # 打开多线程，利用多线程读取实时测得的温度与实时的温度设置（在实验中，设定温度一般为常数，考虑到设定温度可能是渐变函数的存在，这里保留实时更新功能）
        self.threadtemprev = ThreadTempRev()
        self.threadtemprev.start()
        self.threadtempset = ThreadTempSet()
        self.threadtempset.start()

        # 信号与槽函数的连接
        ## 
        self.threadtemprev.sinOut.connect(self.TextTemprevChange)
        self.threadtempset.sinOut.connect(self.TextTempsetChange)
        ## 按钮与函数进行关联
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
        global startprogram
        startprogram = True
        # 获得所有数据的初始值

    def StopProgram(self):
        global startprogram
        startprogram = False

    def AdjustTempSet(self):
        waittime = 0
        global tempset
        tempset = int(float(self.texttempset.toPlainText()))
        print(tempset)
        SetTemp(tempset)
        waittime =1
        
# 利用多線程输出温度测定值和设定值
class ThreadTempRev(QThread):
    sinOut = pyqtSignal(str)
    #初始化
    def ___init__(self):
        super(Thread, self).__init__()

    def run(self):
        # 线程相关的代码
        global startprogram, temprev, waittime, waitinglist
        while True:
            if startprogram == True and waitinglist == 1:
                DetectTemp()
                self.sinOut.emit(str(temprev))
                waitinglist = 2 #下一步为读取设定温度值

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
                waitinglist = 1 #下一步为读取实时温度
                #将结果保存进csv
                WriteLine(str(temprev),str(datarev),str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%SS'))) #将结果保存入CSV的最后一行 #%Y-%m-%d  %H:%M:%S

            sleep(waittime)


# 主程序
if __name__ == "__main__":
    #初始化datalog.csv
    dataframe = pd.DataFrame({'TempRev':[],'TempSet':[],'TimeLog':[]})
        ##将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("temp control\datalog.csv",index=False,sep=',')
    #初始化串口
    initSerial()
    ser.open()
    seropen = True
    #产生UI
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())
