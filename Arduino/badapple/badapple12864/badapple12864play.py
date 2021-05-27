import serial
import csv
import time

ser=serial.Serial()


def init_serial():
    global ser
    ser.baudrate = 460800
    #ser.port = '/dev/ttyUSB0'
    ser.port = 'COM4'
    #ser.timeout =0
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    ser.timeout = 1
    
if __name__ == '__main__':
    init_serial()
    ser.open()
    
    
    with open("Arduino\\badapple\\badapplesend.csv","r", encoding='utf-8') as csvfile:
        
        for i in csvfile:
            if len(i)>100:
                ser.write(i.encode())
            else:
                ser.write(i.encode())
                time.sleep(0.02)
            
        
    ser.close()