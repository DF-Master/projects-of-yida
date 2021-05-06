import serial
import turtle

# default data set
comdefault = "\\.\\COM3"

# serial


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


def read_serial():
    global ser
    


    # ser.open()
    c = ser.read()
    # ser.close()
    print(c)
    if len(c) == 0:
        turtle.ontimer(read_serial, 500)
        return

    c = c.decode('utf-8')



    if c == 'u':
        tt1.forward(50)

    if c == 'd':
        tt1.backward(50)

    if c == 'l':
        tt1.left(45)

    if c == 'r':
        tt1.right(45)

    turtle.ontimer(read_serial, 10)


# # program
if __name__ == '__main__':
    global ser
    ser = serial.Serial()
    initSerial()

    ser.open()
    print('here')
    ser.close()

    wn = turtle.Screen()
    tt1 = turtle.Turtle()
    tt1.shape('turtle')
    tt1.speed('fast')
    
    ser.open()
    

    turtle.ontimer(read_serial, 1000)
    print('1')
    wn.mainloop()
