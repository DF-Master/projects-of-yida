from simple_pid import PID
import numpy as np
from matplotlib import pyplot as plt
import time

t1=time.time()

pid=PID(Kp=0.7,
    Ki=3,
    Kd=0,
    setpoint=22,
    sample_time=0.01,
    output_limits=(20, 25),
    auto_mode=True,
    proportional_on_measurement=False,
)

lst_systemin=[]
lst_systemout=[]
lst_x=[]
lst_y=[]

for i in range(100):
    system_input=np.random.randint(5,8)
    system_output=3*system_input+4+np.random.rand()
    lst_systemout.append(system_output)
    lst_y.append(system_output)

    lst=[]
    while system_output<20 or system_output>24:
        time.sleep(0.1)
        y=pid(system_output)
        system_output=y
        lst.append(y)   

    
t2=time.time()
print('Runtime:', (t2-t1))

plt.figure(figsize=(30,10))
plt.plot([24]*100,'--')
plt.plot([20]*100,'--')
plt.plot(lst_systemout,label='before PID')
plt.plot(lst_y, label='after PID')
plt.legend(fontsize=15)
plt.tick_params(labelsize=18)
plt.show()