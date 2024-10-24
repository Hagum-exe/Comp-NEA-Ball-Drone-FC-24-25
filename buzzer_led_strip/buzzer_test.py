import machine
import time

buzzer = machine.Pin(28, machine.Pin.OUT)

while True:
    buzzer.high()
    time.sleep_ms(300)
    buzzer.low()
    time.sleep_ms(300)
    
    
    