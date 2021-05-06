import tkinter as tk
import serial

comdefault ='\\.\\COM3'
ser=serial.Serial()

def initSerial(comset=comdefault):

    global ser
    ser.baudrate = 9600
    #ser.port = '/dev/ttyUSB0'
    ser.port = comset
    #ser.timeout =0
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    ser.timeout = 1
    



window = tk.Tk()

bt1 = tk.Button(window, text = '1',command=lambda:bt_clicked('1'))
bt2 = tk.Button(window, text = '2',command=lambda:bt_clicked('2'))
bt3 = tk.Button(window, text = '3',command=lambda:bt_clicked('3'))
bt4 = tk.Button(window, text = '4',command=lambda:bt_clicked('4'))

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()

def bt_clicked(cmd):
    # ser.open()
    ser.write(cmd.encode())
    # ser.close()
    
initSerial('COM3')
ser.open()
window.mainloop()