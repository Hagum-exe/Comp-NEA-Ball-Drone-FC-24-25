from machine import Pin, I2C
from time import sleep

MSG_SIZE = 15   #set message size

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=100000)     #initiate I2C pin
addr = i2c.scan()[0]    #scan for I2C connections and use the first connection found

i2c.writeto(addr, 'Hi from Pi') #write message via I2C
sleep(0.1)

while True:
    a = i2c.readfrom(addr, MSG_SIZE)    #read message via I2C
    print(a)
    sleep(0.1)

