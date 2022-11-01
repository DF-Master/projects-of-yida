import GPIO
import UVcontrol
import streamlit as st
import time


if __name__ == '__main__':
    # Initial
    # GPIO.Initial()
    # UVcontrol.Communication.Print_Used_Com()
    # channel_1=UVcontrol.Communication()
    # channel_1.Print_Name() 
    # channel_1.Check()


    # channel_1.Send_data(UVcontrol.Power_Switch(ini_inensity=10))
    # GPIO.Reset(3)
    # channel_1.Send_data(UVcontrol.Power_Switch(ini_inensity=0))

    st.title("UVControl-WebUI")
    st.caption('made by [Yida](https://github.com/DF-Master) --221101 update!',unsafe_allow_html=True)
    # comdefault = str(comset)
    output= st.empty()

    if st.button('Initial'):
        try:
            GPIO.Initial()
            output.markdown(' Initial Finished ')
        except:
            output.markdown(' Initial failed ')
    
    if st.button('Reset'):
        try:
            GPIO.Reset(3)
            output.markdown(' Reset Finished ')
        except:
            output.markdown(' Reset failed ')

    step_set = st.text_input('StepSet',value='1600')
    dir_set=st.text_input('StepSet(0/1)',value='0')

    if st.button('Forward'):
        try:
            GPIO.Forward(3,dir=int(dir_set),steps=int(step_set))
            output.markdown(' Forward Finished ')
        except:
            output.markdown(' Forward failed ')

    uv_intensity_set = st.text_input('UVIntensitySet(0-255)',value='0')

    if st.button('UVAdjust'):
        try:
            UVcontrol.Communication().Send_data(UVcontrol.Power_Switch(ini_inensity=int(uv_intensity_set)))
            output.markdown(' Forward Finished ')
        except:
            output.markdown(' Forward failed ')
    
    command_order= st.text_input('Command(dir,steps,uv,wait;)',value='1,800,100,1;0,800,0,1')


    if st.button('AutoRun'):
        try:
            n=0
            
            command_order_list=command_order.split(";")
            print(command_order_list)
            for i in command_order_list:
                print(i)
                order_list=i.split(",")
                GPIO.Forward(3,dir=int(order_list[0]),steps=int(order_list[1]))
                UVcontrol.Communication().Send_data(UVcontrol.Power_Switch(ini_inensity=int(order_list[2])))
                time.sleep(int(order_list[3]))
                n+=1
                print('Finish Round: ',n)
                
                output.markdown('Finish Round: '+str(n))
            output.markdown(' AutoRun Finished ')
        except:
            output.markdown(' AutoRun failed ')

    
    # if st.button('Close'):
    #     try:
    #         initSerial(comdefault)
    #         Close()
    #         ser.close()
    #         st.markdown('close')
    #     except:
    #         st.markdown('close failed')
        
    # if st.button('Search COM'):
    #     for i in ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10']:
            
    #         try:
    #             initSerial(i)
    #             Open()
    #             ser.close()
    #         except:
    #             st.markdown('not '+ i)
    #         else:
    #             st.markdown('Please set serial as '+ i)
    #             comdefault = i
                
    # if st.button('COM Now'):
    #     st.markdown(str(comdefault))

    
    # opentimelist = st.text_input('Open Time List',value='2,1')
    # closetimelist = st.text_input('Close Time List',value='2,1')
    # looptimelist = st.text_input('Loop Time List',value='1,1')
    
    # if st.button('Run Program'):
    #     try:
    #         initSerial(comdefault)
    #         Open()
    #         ser.close()
    #         initSerial(comdefault)
    #         Close()
    #         ser.close()
    #     except:
    #         st.markdown('open failed')
    #     else:
    #         st.markdown('test complete, run program')
    #         ol = opentimelist.split(',')
    #         cl = closetimelist.split(',')
    #         ll = looptimelist.split(',')
    #         for i in list(range(len(ol))):
    #             for j in list(range(int(ll[i]))):
    #                 initSerial(comdefault)
    #                 Open()
    #                 ser.close()
    #                 time.sleep(float(ol[i]))
    #                 initSerial(comdefault)
    #                 Close()
    #                 time.sleep(float(cl[i]))
    #                 ser.close()
    #                 st.markdown('Open '+ str(ol[i]) + '  Close ' + str(cl[i])+ '  Loop ' + str(j))
    #         st.markdown('Program finish')
    

