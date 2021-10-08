import streamlit as st
from streamlit.file_util import streamlit_write
import RPi.GPIO as GPIO
import time
import os
from PIL import Image
from threading import Timer



# ===================================================================================================
# 底层硬件
# ===================================================================================================


# RGB相关
#RGB三色灯引脚定义
LED_R = 22
LED_G = 27
LED_B = 24

#设置RGB三色灯为BCM编码方式
GPIO.setmode(GPIO.BCM)

#RGB三色灯设置为输出模式
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
#---


# 电机相关
#小车电机引脚定义
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#忽略警告信息
GPIO.setwarnings(False)



#舵机引脚定义
ServoPin = 23
GPIO.setup(ServoPin, GPIO.OUT)



# ===================================================================================================
# Def
# ===================================================================================================

#RGB相关
def Show_Seven_Colors():
    #循环显示7种不同的颜色
    try:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(0.5)
    except:
        print("except")
    #使用try except语句，当CTRL+C结束进程时会触发异常后
    #会执行gpio.cleanup()语句清除GPIO管脚的状态
    GPIO.cleanup()

def Close_LED():
    #循环显示7种不同的颜色
    try:
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
    except:
        print("except")
    #使用try except语句，当CTRL+C结束进程时会触发异常后
    #会执行gpio.cleanup()语句清除GPIO管脚的状态

def Open_LED():
    #循环显示7种不同的颜色
    try:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)

    except:
        print("except")
    #使用try except语句，当CTRL+C结束进程时会触发异常后
    #会执行gpio.cleanup()语句清除GPIO管脚的状态

def blink():
    try:
        Close_LED()
        time.sleep(0.1)
        Open_LED()
    except:
        print("except")
# 舵机相关

def corlor_light(pos):
    
    if pos > 150:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
    elif pos > 125:
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
    elif pos >100:
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 75:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
    elif pos > 50:
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 25:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 0:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
    else :
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)

#舵机来回转动
def servo_control_color():
    for pos in range(181):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)
        corlor_light(pos)
        time.sleep(0.009) 
    for pos in reversed(range(181)):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)
        corlor_light(pos)
        time.sleep(0.009)

#电机相关
#电机引脚初始化操作
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #设置pwm引脚和频率为2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

#小车前进	
def run(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车后退
def back(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车左转	
def left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车右转
def right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车原地左转
def spin_left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车原地右转
def spin_right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

#小车停止	
def brake():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)

#图像相关
def show_new_photo():
    nfn = os.popen("ls -tr /root/logicphotos/ | grep jpg | tail -n 1")
    new_file_name = nfn.read().strip()
    image = Image.open('/root/logicphotos/'+new_file_name)
    st.image(image, caption='最新捕获的图像'+ " " + new_file_name)

def auto_show_new_photo():
    show_new_photo()
    print('here')
    Timer(5,auto_show_new_photo).start()
    
def show_new_ai_photo():
    nfn = os.popen('ssh root@badapple.online "ls -tr /root/yidanetdisk/file_after_ai/ | grep jpg | tail -n 1"')
    new_file_name = nfn.read().strip()
    os.system("scp root@badapple.online:/root/yidanetdisk/file_after_ai/"+new_file_name+"  /root/logicphotos/ai_photos/")
    image_ai = Image.open('/root/logicphotos/ai_photos/'+new_file_name)
    st.image(image_ai, caption='最新识别的图像'+ " " + new_file_name)


# ===================================================================================================
# 正文部分
# ===================================================================================================


st.title('Car Controller')
st.write('--Made by Yida')
st.write('--20210610 updated')
st.write('=========================================')
st.write(' ')


# LED control
st.write('## LED')

column_1, column_2,column_3 = st.beta_columns(3)
seven_colors = column_1.button('七色灯闪烁')
close_led = column_2.button('关灯')
open_led = column_3.button('开灯')


if seven_colors:
    Show_Seven_Colors()
if close_led:
    Close_LED()
if open_led:
    Open_LED()

# 舵机
st.write('## 舵机')

column_fullleft, column_medium,column_fullright = st.beta_columns(3)



fullleft =column_fullleft.button('左满舵')
medium = column_medium.button('正前方')
fullright = column_fullright.button('右满舵')




    
if medium:
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
    pwm_servo.ChangeDutyCycle(2.5 + 10 * 90/180)
    time.sleep(0.3)
    pwm_servo.stop()
    
if fullleft:
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
    pwm_servo.ChangeDutyCycle(12)
    time.sleep(0.3)
    pwm_servo.stop()
    
if fullright:
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
    pwm_servo.ChangeDutyCycle(3)
    time.sleep(0.3)
    pwm_servo.stop()

angle = st.slider("角度细调",3.0,12.0,7.5,0.25)

column_angle,column_shake = st.beta_columns(2)
shake = column_shake.button('彩色摆头')
change_angle = column_angle.button('调整角度')

if shake:
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
    pwm_servo.ChangeDutyCycle(2.5 + 10 * 90/180)
    servo_control_color()
    pwm_servo.stop()

if change_angle:
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
    pwm_servo.ChangeDutyCycle(15.0-angle)
    time.sleep(0.3)
    pwm_servo.stop()

# Direction
st.write('## 方向')
# GPIO.cleanup()


column_cycleleft, column_advance,column_cycleright = st.beta_columns(3)
column_left, column_brake,column_right = st.beta_columns(3)
column_continue_on, column_back,column_continue_back = st.beta_columns(3)

cycleleft = column_cycleleft.button('原地左转')
advance = column_advance.button('↑')
cycleright = column_cycleright.button('原地右转')
left= column_left.button('←')
brake = column_brake.button('刷新')
right = column_right.button('→')
continue_on = column_continue_on.button('持续前进')
back = column_back.button('↓')
continue_back = column_continue_back.button("持续后退")


if advance:
    motor_init()
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(0.5)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.stop()
    pwm_ENB.stop()
    # GPIO.cleanup() 


if left:

    motor_init()
    # left(0.5)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(0.5)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.stop()
    pwm_ENB.stop()
    # GPIO.cleanup() 


if right:

    motor_init()
    # right(0.5)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(0.5)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.stop()
    pwm_ENB.stop()
    # GPIO.cleanup() 


if back:

    motor_init()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(0.5)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.stop()
    pwm_ENB.stop()
    # GPIO.cleanup() 

if cycleleft:
    motor_init()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(0.5)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.stop()
    pwm_ENB.stop()
    # GPIO.cleanup() 
    
if cycleright:
    motor_init()
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(0.5)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.stop()
    pwm_ENB.stop()
    # GPIO.cleanup() 
    
if continue_on:

    motor_init()

    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

        # time.sleep(0.2)
        # pwm_ENA.stop()
        # pwm_ENB.stop()
    wait_until_inifinity =True
    
    
if continue_back:
    motor_init()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)

if brake:
    # show_new_photo()
    # show_new_ai_photo()
    blink()

# 图片采集

st.write('## 图像采集')

column_auto_collect, column_collect_one,column_stop = st.beta_columns(3)
collect_auto = column_auto_collect.button("持续照片采集")
collect_one_photo = column_collect_one.button("单张照片采集")
collect_end = column_stop.button("停止采集")

if collect_auto:
    os.system("nohup bash /root/berry/auto_photo_collect.sh  &")

if collect_one_photo:
    os.system("bash /root/berry/collect_one_photo.sh")
    show_new_photo()
    show_new_ai_photo()
    blink()

    
if collect_end:
    os.system("ps aux | grep auto_photo_collect | awk '{print $2}'| xargs kill -9")

# show_new_photo()
# show_new_ai_photo()