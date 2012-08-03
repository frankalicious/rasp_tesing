'''
PCF8574 connected to the I2C bus.
output0..3 connected to leds.
a0...a3 is connected to ground. address is 0x38
'''
from smbus import SMBus
import time
import random

def endless_sequence(bus):
    """
    
    Arguments:
    - `bus`:
    """
    forward = range(1<<4)
    backward = forward[::-1]
    while True:
        for sequence in [forward, backward]:
            for led in sequence:
                print led
                b.write_i2c_block_data(0x38,0,[led])
                time.sleep(0.1)
        time.sleep(0.5)

def endless_random(bus):
    """
    
    Arguments:
    - `bus`:
    """
    while True:
        led = random.randint(0,(1<<4)-1)
        b.write_i2c_block_data(0x38,0,[led])
        time.sleep(0.2)


b = SMBus(0)
# endless_sequence(b)
endless_random(b)
