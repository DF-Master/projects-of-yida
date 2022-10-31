from mimetypes import init
import RPi.GPIO as GPIO
import time


def Output_set(channel_list, status_list):
    if len(channel_list) == len(status_list):
        for i in range(len(channel_list)):
            GPIO.output(channel_list[i], status_list[i])
    else:
        print('Error:Channel Status not Equal')


def Channel_setup(channel_list, status_list):
    if len(channel_list) == len(status_list):
        for i in range(len(channel_list)):
            GPIO.setup(channel_list[i], status_list[i])
    else:
        print('Error:Channel Status not Equal')


def Transform_list(l):
    return list(map(list, zip(*l)))



def Forward(channel,dir=0,dir_channel=4,pc_channel=2,pc_close=1,en_channel=5,en_close=1,delay=0.001, steps=1600,check_step=100):  #A-B-C-D-A通电方式
    try:
        GPIO.setup(en_channel, GPIO.OUT, initial=1-en_close) # OPEN EN
        GPIO.setup(dir_channel, GPIO.OUT, initial=dir) # DIR:0-down 1-up

        for i in range(0, steps):
            if i % check_step == 0:
                if GPIO.input(pc_channel) == pc_close:
                    GPIO.output(channel, 1)
                    time.sleep(delay)
                    GPIO.output(channel, 0)
                    time.sleep(delay)
                else:
                    # Turn back 500 Step
                    GPIO.setup(dir_channel, GPIO.OUT, initial=1-GPIO.input(dir_channel))
                    for j in range(500):
                        GPIO.output(channel, 1)
                        time.sleep(delay)
                        GPIO.output(channel, 0)
                        time.sleep(delay)
                    print("### POS_LOCKED ACTIVATE ###")
                    GPIO.setup(dir_channel, GPIO.OUT, initial=1-GPIO.input(dir_channel))
                    break
            else:
                GPIO.output(channel, 1)
                time.sleep(delay)
                GPIO.output(channel, 0)
                time.sleep(delay)
        GPIO.setup(en_channel, GPIO.OUT, initial=en_close) # CLOSE EN

    except:
        print("### Move Failed ###")


def Reset(channel,dir=0,dir_channel=4,pc_channel=2,pc_close=1,en_channel=5,en_close=1,delay=0.001, steps=40000,check_step=100):
    Forward(channel,dir=0,dir_channel=4,pc_channel=2,pc_close=1,en_channel=5,en_close=1,delay=0.001, steps=40000,check_step=100)
    print("### ALREADY RESET ###")

def Initial():
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    #Initial
    GPIO.setup(2, GPIO.IN) # POS_LOCK: 0-connect 1-disconnect
    GPIO.setup(3, GPIO.OUT) # PUL
    GPIO.setup(5, GPIO.OUT, initial=1) # EN:0-connect 1-disconnect
    GPIO.setup(4, GPIO.OUT, initial=0) # DIR:0-down 1-up

if __name__ == '__main__':

    # Run
    Reset(3)

    GPIO.setup(5, GPIO.OUT, initial=1)


