from machine import Pin, PWM
import time

class readPWM(PWM, Pin):
    def __init__(self, channel_num):
        self.channel = Pin(channel_num, Pin.IN) #initialise pwm read channel
        
    def read_pulse_width(self):
        while self.channel.value()==0:
            pass
        start = time.time_ns()  #taking low pulse width time stamp
        
        while self.channel.value() == 1:
            pass
        end = time.time_ns()    #taking high pulse width time stamp
        
        return round((((end - start)-980000)/(2000000-980000))) #calculating pulse width as decimal
    
    

class writePWM(PWM, Pin):
    def __init__(self, pin_num, freq):
        self.pin = PWM(Pin(pin_num))
        self.pin.freq(freq)
        
    def write_pulse_width(self, deci_val):
        pulse_width = round(deci_val*(2000000-980000)+980000)
        self.pin.duty_ns(pulse_width)
        

    