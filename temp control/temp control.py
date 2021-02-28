# 导入模块

import serial
import binascii,time

# 定义可设置的变量
tempsetdefault = 30 # 默认温度设定值应当是一个最多为1位小数、最高位为百位的数字
waittimedefault= 2 # 默认温度测定等待时间，以秒为单位，0.5 s 以下的过快访问会导致不出结果？ 

# 根据字符串产生CRC代码并将其拼接为命令
## CRC 计算代码 https://www.jianshu.com/p/568ac2b3f442
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

## 将字符串去掉特定字母并加和
def Str_Join(string, icon = ' ', newicon = ''):
    list = string.split(icon)
    newstring = newicon.join(list)
    return newstring

## 将这两个命令合二为一

def Add_CRC(stringnoCRC):
    stringnoCRC_join = Str_Join(stringnoCRC)
    crc = calc_crc(stringnoCRC)
    newstring = stringnoCRC + ' ' + crc[-4:-2] +' ' + crc[-2:]
    return newstring



# 定义输入部分

ser = serial.Serial()

## 串口初始化
def initSerial():
    global ser
    ser.baudrate = 9600
    #ser.port = '/dev/ttyUSB0'
    ser.port = 'COM3'
    #ser.timeout =0
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    
    
## 测温模块 https://sunmker.cn/serial_interface/
def DetectTemp(waittime= waittimedefault):
    global ser
    if seropen == True:
        # 产生查询温度测定值命令
        readtemt = '01 03 10 01 00 01 D1 0A'
        readtemt16bit=bytes.fromhex(readtemt)
        # print(readtemt16bit)
        
        # 串口发送数据
        result=ser.write(readtemt16bit)

        # 停止、等待数据，这一步非常关键。timeout压根没用
        # inwaiting: Get the number of bytes in the input buffer
        time.sleep(waittime)
        count=ser.inWaiting()
        
        # 数据的接收
        if count>0:
            data=ser.read(count)
            if data!=b'':
                # 将接受的16进制数据格式如b'h\x12\x90xV5\x12h\x91\n4737E\xc3\xab\x89hE\xe0\x16'
                #                      转换成b'6812907856351268910a3437333745c3ab896845e016'
                #                      通过[]去除前后的b'',得到我们真正想要的数据 
                print("receive",str(binascii.b2a_hex(data))[2:-1])
                temprev=int(str(str(binascii.b2a_hex(data))[2:-1][-8:-4:]),16)/10
                print(temprev)

## 设置温度模块 
def SetTemp(tempset = tempsetdefault):
    global ser
    if seropen == True:
        
        # 根据设定温度产生16进制命令
        tempset16bit = hex(tempset*10)[2:].zfill(4)
        tempsetordernoCRC = str('01 06 00 00 ' + tempset16bit[0:2] + ' ' + tempset16bit[-2:])
        tempsetorder= bytes.fromhex(Add_CRC(tempsetordernoCRC))
        
        # 串口发送数据 
        print(tempsetorder)
        ser.write(tempsetorder) # 向仪器输入温度设定命令

## 检测仪器数据模块
def DetectSet(hrnumer = '0000',waittime= waittimedefault):
    global serial
    if seropen == True:
        
        # 产生查询命令
        detectsetordernoCRC = str('01 03 '+ hrnumer[0:2] +' ' + hrnumer[-2:] + ' 00 01')
        detectsetorder =  bytes.fromhex(Add_CRC(detectsetordernoCRC))
        
        # 串口发送数据
        print(detectsetorder)
        ser.write(detectsetorder)
        
    # 停止、等待数据，这一步非常关键。timeout压根没用
        # inwaiting: Get the number of bytes in the input buffer
        time.sleep(waittime)
        count=ser.inWaiting()
        
        # 数据的接收
        if count>0:
            data=ser.read(count)
            if data!=b'':
                # 将接受的16进制数据格式如b'h\x12\x90xV5\x12h\x91\n4737E\xc3\xab\x89hE\xe0\x16'
                #                      转换成b'6812907856351268910a3437333745c3ab896845e016'
                #                      通过[]去除前后的b'',得到我们真正想要的数据 
                print("receive",str(binascii.b2a_hex(data))[2:-1])
                temprev=int(str(str(binascii.b2a_hex(data))[2:-1][-8:-4:]),16)/10
                print(temprev)

if __name__ == "__main__":
    initSerial()
    ser.open()
    while True:
        seropen=True
        DetectSet()
        DetectTemp()
