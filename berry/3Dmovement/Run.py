import GPIO
import UVcontrol

if __name__ == '__main__':
    # Initial
    GPIO.Initial()
    UVcontrol.Communication.Print_Used_Com()
    channel_1=UVcontrol.Communication()
    channel_1.Print_Name() 
    channel_1.Check()


    channel_1.Send_data(UVcontrol.Power_Switch(ini_inensity=10))
    GPIO.Reset(3)
    channel_1.Send_data(UVcontrol.Power_Switch(ini_inensity=0))
    # GPIO.Forward(3,dir=1,steps=80)