#testing interface between pico and esc
from machine import Pin, PWM

# setup pwm output for esc
esc1  = PWM(Pin(3))


esc1.freq(50)   #specify frequency of esc pwm


esc1.duty_ns(1000000)   #start with 0.00 throttle input


pwm_min = 1000000   #specify range of PWM pulse width
pwm_max = 2000000

def calculate_duty_cycle(throttle:float, dead_zone:float = 0.03) -> int:   
    """Determines the appropriate PWM duty cycle, in nanoseconds, to use for an ESC controlling a BLDC motor"""

    ### SETTINGS (that aren't parameters) ###
    duty_ceiling:int = pwm_max # the maximum duty cycle (max throttle, 100%) is 2 ms, or 10% duty (0.10)
    duty_floor:int = pwm_min # the minimum duty cycle (min throttle, 0%) is 1 ms, or 5% duty (0.05). HOWEVER, I've observed some "twitching" at exactly 5% duty cycle. It is off, but occasionally clips above, triggering the motor temporarily. To prevent this, i'm bringing the minimum down to slightly below 5%
    ################

    # calcualte the filtered percentage (consider dead zone)
    range:float = 1.0 - dead_zone - dead_zone
    percentage:float = min(max((throttle - dead_zone) / range, 0.0), 1.0)
    
    dutyns = duty_floor + ((duty_ceiling - duty_floor) * percentage)

    # clamp within the range
    dutyns = max(duty_floor, min(dutyns, duty_ceiling))

    return int(dutyns)

while True:
    duty = float(input('Enter duty: '))
    esc1.duty_ns(duty)
    