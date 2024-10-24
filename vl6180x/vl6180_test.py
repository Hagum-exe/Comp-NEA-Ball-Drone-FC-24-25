import time
from machine import Pin, I2C
from vl6180 import Sensor
#from machine import Pin

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
#print(i2c.scan())

tof_sensor=Sensor(i2c)

while True:
    x = tof_sensor.range()
    print(x)
    time.sleep(0.1)
   
