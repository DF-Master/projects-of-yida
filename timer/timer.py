import winsound
import time 


while True:
    time.sleep(5)    
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)
