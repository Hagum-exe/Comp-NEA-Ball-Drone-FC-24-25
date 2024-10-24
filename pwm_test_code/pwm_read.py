#reads one channel of PWM signal from CRSF receiver

from machine import Pin, PWM
import time

input_pin  = Pin(5, Pin.IN)
while True:
    while input_pin.value() == 0:
      pass
    start = time.time_ns()
    while input_pin.value() == 1:
        pass
    end = time.time_ns()
    duration = end - start
    print (str(duration))
    time.sleep(0.1)