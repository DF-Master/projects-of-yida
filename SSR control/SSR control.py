import serial
import time
import binascii
import streamlit as st
# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import UI210331_1 as ui


# 定义默认系统变量

seropen = False
openorder = 'A0 01 01 A2'
closeorder = 'A0 01 00 A1'
openorder16bit = bytes.fromhex(openorder)
closeorder16bit = bytes.fromhex(closeorder)
startprogram = False

# 定义可调变量

defaultopentime = float(2)  # 这是开机启动时的预热测试时间
opentimedefault = float(5)
stoptimedefault = float(5)
loopdefault = float(5)
comdefault = 'COM4'
waittimedefault = 5

# 打开串口
ser = serial.Serial()


def initSerial(comset = comdefault):
    global ser,seropen
    ser.baudrate = 9600
    #ser.port = '/dev/ttyUSB0'
    ser.port = comset
    #ser.timeout =0
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    seropen=True

# 定义开关函数
def TryOpen(comset):
    try:    
        global comdefault,breakloop
        initSerial(comset)
        ser.open()
        seropen = True

        Open()
        time.sleep(defaultopentime)
        Close()
        
        comdefault = comset
    except:
        print('not ' + str(comset))

def Open():
    for i in ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10']:
        TryOpen(i)
    print(comdefault)
    global seropen
    if seropen == False:
        print('open fail')
    else:
        ser.write(openorder16bit)


def Close():
    global seropen
    if seropen == False:
        print('open fail')
    else:
        ser.write(closeorder16bit)
        


# # 产生主界面
# class ThreadRunLoop(QThread):
#     sinOut = pyqtSignal(str)

#     def ___init__(self):
#         super(Thread, self).__init__()

#     def run(self):
#         # 线程相关的代码
#         global opentimedefault, closetimedefault, loopdefault, comdefault 
#         while True:
#             if startprogram == True and waitinglist == 2:
#                 DetectSet()
#                 self.sinOut.emit(str(datarev))
#                 waitinglist = 1  # 下一步为读取实时温度
#                 # 将结果保存进csv
#                 WriteLine(str(temprev), str(datarev), NowTime())  # 将结果保存入CSV的最后一行 

#             sleep(waittime)

# class Main(QMainWindow, ui.Ui_MainWindow):
#     def __init__(self):
#         # 初始化
#         super().__init__()
#         self.setWindowTitle('UV Controller --UI')
#         self.setupUi(self)  # UI文件在先前的import已有定义

#         # 打开多线程，利用多线程读取实时测得的温度与实时的温度设置（在实验中，设定温度一般为常数，考虑到设定温度可能是渐变函数的存在，这里保留实时更新功能）
#         # self.threadtemprev = ThreadTempRev()
#         # self.threadtemprev.start()
        

#         # 信号与槽函数的连接

#         # self.opentime.sinOut.connect(self.OpenTimeChange)
#         # self.closetime.sinOut.connect(self.CloseTimeChange)
#         # 按钮与函数进行关联

#         self.pbstop.clicked.connect(self.StopProgram)
#         self.pbquit.clicked.connect(self.EndProgram)
#         self.pbstart.clicked.connect(self.StartProgram)

#     def EndProgram(self):
#         sys.exit(app.exec_())

#     def StartProgram(self):
#         startprogram = True

#     def StopProgram(self):
#         startprogram = False

#     def OpenTimeChange(self, str):
#         if str.isdigit():
#             global opentimedefault
#             opentimedefault = float(str)
`-+`
#     def CloseTimeChange(self, str):
#         if str.isdigit():
#             global closetimedefault
#             closetimedefault = float(str)


if __name__ == "__main__":
    # for i in ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10']:
    #     TryOpen(i)
    # print(comdefault)
    st.title("UV网页控制UI")
    st.markdown('made by [Yida](https://github.com/DF-Master) --210402 update!',unsafe_allow_html=True)
    if st.button('Open'):
        Open()
        time.sleep(2)
    if st.button('Close'):
        Close()


        

    # 产生UI
    # # app = QtWidgets.QApplication(sys.argv)
    # # window = Main()
    # window.show()

    # sys.exit(app.exec_())
