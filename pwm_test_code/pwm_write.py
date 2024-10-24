#testing interface between pico and servo

from machine import Pin, PWM

#def map(percent):
#return 1000000+1000000*percent


# setup pwm output for servo
esc1  = PWM(Pin(3))
esc2 = PWM(Pin(5))
esc3 = PWM(Pin(7))
esc4 = PWM(Pin(9))

esc1.freq(50)
esc2.freq(50)
esc3.freq(50)
esc4.freq(50)

esc1.duty_ns(1000000)
esc2.duty_ns(1000000)
esc3.duty_ns(1000000)
esc4.duty_ns(1000000)

pwm_min = 1000000
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
    duty = calculate_duty_cycle(duty)
    esc1.duty_ns(duty)
    esc2.duty_ns(duty)
    esc3.duty_ns(duty)
    esc4.duty_ns(duty)
    