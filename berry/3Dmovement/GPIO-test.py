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


def forward(channel, delay=0.01, steps=50):  #A-B-C-D-A通电方式
    GPIO.setup(channel, GPIO.OUT, initial=1)
    for i in range(0, steps):
        GPIO.output(channel, 1)
        time.sleep(delay)
        GPIO.output(channel, 0)
        time.sleep(delay)


if __name__ == '__main__':
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    #Initial
    GPIO.setup(2, GPIO.IN)
    # Run
    while True:
        if GPIO.input(2) == GPIO.LOW:
            GPIO.cleanup(3)
            GPIO.cleanup(4)
            time.sleep(0.5)
        else:
            GPIO.setup(4, GPIO.OUT, initial=1)
            forward(3)

    # time.sleep(0.2)
    # print(GPIO.input(26))

    # End and Clean
