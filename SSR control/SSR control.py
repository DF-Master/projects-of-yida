import serial
import time
import streamlit as st
import csv



        
# 定义默认系统变量



seropen = False
openorder = 'A0 01 00 A1'
closeorder = 'A0 01 01 A2'
openorder16bit = bytes.fromhex(openorder)
closeorder16bit = bytes.fromhex(closeorder)
startprogram = False

# 定义可调变量
global comdefault
comdefault = 'COM3'
defaultopentime = float(0.5)  # 这是开机时的测试时间


#
# 打开串口
ser = serial.Serial()




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

# 定义开关函数
# def TryOpen(comset=comdefault):
#     try:    
#         global comdefault,breakloop
#         # initSerial(comset)
        
#         Open()
#         time.sleep(defaultopentime)
#         Close()  
#     except:
#         print('not ' + str(comset))
#     else:
#         seropen = True


#         comdefault = comset
#         print('serial open, serial name is '+ comdefault)
#         return True
def Open():
    global seropen
    if seropen == False:
        print('open fail')
    else:
        ser.write(openorder16bit)
        print('open')
        seropen=False


def Close():
    global seropen
    if seropen == False:
        print('open fail')
    else:
        ser.write(closeorder16bit)
        print('close')
        seropen=False
        

            
        
        
if __name__ == "__main__":
    # if TryOpen(comdefault)==True:
    #     print(comdefault)
    # else:
    #     for i in ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10']:
    #         TryOpen(i)
    #     print(comdefault)
    # print('COM set')

    
    st.title("UV网页控制UI")
    st.markdown('made by [Yida](https://github.com/DF-Master) --210402 update!',unsafe_allow_html=True)
    comset = st.text_input('COMSet',value='COM4')
    comdefault = str(comset)
    if st.button('Open'):
        try:
            initSerial(comdefault)
            Open()
            ser.close()
            st.markdown('open')
        except:
            st.markdown('open failed')
            
    if st.button('Close'):
        try:
            initSerial(comdefault)
            Close()
            ser.close()
            st.markdown('close')
        except:
            st.markdown('close failed')
        
    if st.button('Search COM'):
        for i in ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10']:
            
            try:
                initSerial(i)
                Open()
                ser.close()
            except:
                st.markdown('not '+ i)
            else:
                st.markdown('Please set serial as '+ i)
                comdefault = i
                
    if st.button('COM Now'):
        st.markdown(str(comdefault))

    
    opentimelist = st.text_input('Open Time List',value='2,1')
    closetimelist = st.text_input('Close Time List',value='2,1')
    looptimelist = st.text_input('Loop Time List',value='1,1')
    
    if st.button('Run Program'):
        try:
            initSerial(comdefault)
            Open()
            ser.close()
            initSerial(comdefault)
            Close()
            ser.close()
        except:
            st.markdown('open failed')
        else:
            st.markdown('test complete, run program')
            ol = opentimelist.split(',')
            cl = closetimelist.split(',')
            ll = looptimelist.split(',')
            for i in list(range(len(ol))):
                for j in list(range(int(ll[i]))):
                    initSerial(comdefault)
                    Open()
                    ser.close()
                    time.sleep(float(ol[i]))
                    initSerial(comdefault)
                    Close()
                    time.sleep(float(cl[i]))
                    ser.close()
                    st.markdown('Open '+ str(ol[i]) + '  Close ' + str(cl[i])+ '  Loop ' + str(j))
            st.markdown('Program finish')
    
