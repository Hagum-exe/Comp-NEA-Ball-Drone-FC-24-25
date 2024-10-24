#reads one channel of PWM signal from CRSF receiver

from machine import Pin
import time

ch0  = Pin(0, Pin.IN)
ch1 = Pin(1, Pin.IN)
ch2 = Pin(2, Pin.IN)
ch3 = Pin(3, Pin.IN)
ch4 = Pin(4, Pin.IN)
ch5 = Pin(5, Pin.IN)

def read_pulse_width(channel):
    while channel.value()==0:
        pass
    start = time.time_ns()
    
    while channel.value() == 1:
        pass
    end = time.time_ns()
    return round((((end - start)-980000)/(2000000-980000))*100)


while True:
    ch0_value = read_pulse_width(ch0)
    ch1_value = read_pulse_width(ch1)
    ch2_value = read_pulse_width(ch2)
    ch3_value = read_pulse_width(ch3)
    ch4_value = read_pulse_width(ch4)
    ch5_value = read_pulse_width(ch5)
    print(f'ch0: {ch0_value}\tch1: {ch1_value}\tch2: {ch2_value}\tch3: {ch3_value}\tch4: {ch4_value}\tch5: {ch5_value}')
    time.sleep(0.2)
    
    