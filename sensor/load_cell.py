#! /usr/bin/python2

import time
import sys

referenceUnit = 1

import RPi.GPIO as GPIO
from sensor.hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(6, 13)
hx.set_reading_format("MSB", "MSB")

# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92. 

hx.reset()
hx.tare()
print("Tare done! Add weight now...")

def baca_berat():
    try:
        hx.set_reference_unit(referenceUnit)
        val_A = hx.get_weight_A(5)

        print("A %.3f" %(val_A))

        hx.power_down()
        time.sleep(0.1)
        hx.power_up()
        time.sleep(0.1)
        
        return val_A

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        
if __name__ == '__main__':
    try:
        while True:
            baca_berat()
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
