import serial
import time

# default data set
comdefault = "\\.\\COM3"

# serial
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
    ser.open() 
    ser.timeout = 1


# program
if __name__ == '__main__':
    ser = serial.Serial()
    initSerial()
    print('here')
    
    while True:
        data = ser.read()
        if len(data) > 0:
            print('Got', data.decode())
        time.sleep(0.1)
        print('Sleep')
    
        print('请输入命令:')
        cmd = input()
        print('你发送了命令：',cmd,len(cmd))
        ser.write(str(cmd).encode())
    ser.close()
