import serial
import time

ser = serial.Serial('COM8', timeout=1)
time.sleep(2)
a = 'B00000,B10001,B00000,B00000,B10001,B01110,B00000,'.encode()
ser.write(a)
print(a)
ser.close()





# time.sleep(1)
# comdefault = 'COM8'


# openorder = '00 01 00 A1'
# closeorder = 'A0 01 01 A2'
# closeorder16bit = bytes.fromhex(closeorder)
# print(closeorder16bit)


# def initSerial(comset=comdefault):

#     global ser, seropen
#     ser.baudrate = 9600
#     #ser.port = '/dev/ttyUSB0'
#     ser.port = comset
#     #ser.timeout =0
#     ser.stopbits = serial.STOPBITS_ONE
#     ser.bytesize = 8
#     ser.parity = serial.PARITY_NONE
#     ser.rtscts = 0


# if __name__ == '__main__':
#     # initSerial()

#     # ser.open()
#     # a = a2b_hex(closeorder16bit)
#     # ser.write(a)
#     # print(a)
#     # ser.close()
    
    
#     time.sleep(1)
    
    
#     # ser.open()
#     a = '123456789'.encode()
#     ser.write('   '.encode())
#     ser.write(a)
#     print(a)
#     ser.close()
#     time.sleep(1)
