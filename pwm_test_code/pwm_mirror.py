#testing interface between CRSF receiver and servo via pico as intemediary

from machine import Pin, PWM
import time

# setup pwm output for servo
pwm_out  = PWM(Pin(3))
pwm_out.freq(50)


input_pin  = Pin(2, Pin.IN)

while True:
    while input_pin.value() == 0:
      pass 
    start = time.time_ns()
    while input_pin.value() == 1:
        pass
    end = time.time_ns()
    duration = end - start  #read pulse width from receiver
    print(duration)
   
    pwm_out.duty_ns(duration) #write pulse width to servo
    