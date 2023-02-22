import GPIO
import UVcontrol
import streamlit as st
import time
import PumpControl

if __name__ == '__main__':


    st.title("3D-UV-Pump-Control-WebUI")
    st.caption('made by [Yida](https://github.com/DF-Master) --221101 update!',unsafe_allow_html=True)
    # comdefault = str(comset)
    output= st.empty()

    st.header("3D Movement")

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

    st.header("UV Control")

    uv_intensity_set = st.text_input('UVIntensitySet(0-255)',value='0')

    uv_com=st.text_input('UV_inputCOM',value='/dev/ttyUSB0')

    if st.button('UVAdjust'):
        try:
            UVcontrol.Communication(com=uv_com).Send_data(UVcontrol.Power_Switch(ini_inensity=int(uv_intensity_set)))
            output.markdown(' UVAdjust Finished ')
        except:
            output.markdown(' UVAdjust failed ')
    
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
                UVcontrol.Communication(com=uv_com).Send_data(UVcontrol.Power_Switch(ini_inensity=int(order_list[2])))
                time.sleep(float(order_list[3]))
                n+=1
                print('Finish Round: ',n)
                
                output.markdown('Finish Round: '+str(n))
            output.markdown(' AutoRun Finished ')
        except:
            output.markdown(' AutoRun failed ')

    st.header("Pump Control")

    pump_set_status= st.empty()

    pump_intensity_set = st.text_input('PumpIntensitySet(0-255)uL/min',value='10')

    pump_com=st.text_input('Pump_inputCOM',value='/dev/ttyUSB0')

    if st.button('Read Pump Set'):
        try:
            pump_channel=PumpControl.Communication(com=pump_com)
            pump_channel.Send_data(b'\xE9\x01\x03\x43\x52\x54\x47')
            pump_set_status.markdown(list(pump_channel.Read_Size(13)))
            output.markdown(' Read Pump Set Finished ')
        except:
            output.markdown(' Read Pump Set failed ')

    if st.button('Pump Intensity Set(1mL,uL/min)'):
        try:
            pump_channel=PumpControl.Communication(com=pump_com)
            pump_channel.Send_data(b'\xE9\x01\x0A\x43\x57\x54\x01\x01\x00\x07'+ bytes(chr(int(pump_intensity_set)),encoding='ascii')+b'\x00\x08'+bytes(chr(68^int(pump_intensity_set)),encoding="ascii"))
            # pump_channel.Send_data( b'\xe9\x01\nCWT\x01\x01\x00\x07\x64\x00\x08\x20')
            
            pump_set_status.markdown(list(pump_channel.Read_Size(5)))
            output.markdown(' Read Pump Set Finished ')
        except:
            output.markdown(' Read Pump Set failed ')
    if st.button('Pump On'):
        try:
            pump_channel=PumpControl.Communication(com=pump_com)
            pump_channel.Send_data(b'\xE9\x01\x04\x43\x57\x58\x01\x48') 
            pump_set_status.markdown(list(pump_channel.Read_Size(5)))  
            output.markdown(' Pump On Finished ')
        except:
            output.markdown(' Pump On failed ')


    if st.button('Pump Terminate'):
        try:
            pump_channel=PumpControl.Communication(com=pump_com)
            pump_channel.Send_data(b'\xE9\x01\x04\x43\x57\x58\x00\x49') 
            pump_set_status.markdown(list(pump_channel.Read_Size(5)))
            output.markdown(' Pump On Finished ')
        except:
            output.markdown(' Pump On failed ')

    
    if st.button('Pump Stop'):
        try:
            pump_channel=PumpControl.Communication(com=pump_com)
            pump_channel.Send_data(b'\xE9\x01\x04\x43\x57\x58\x02\x4B') 
            pump_set_status.markdown(list(pump_channel.Read_Size(5)))
            output.markdown(' Pump On Finished ')
        except:
            output.markdown(' Pump On failed ')
    
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
    

