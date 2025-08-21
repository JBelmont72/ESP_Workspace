''' use the same sketch for RPi and ESP32 and RP2040'''

import sys
from time import sleep
print(sys.version)
if 'MicroPython v1.21.0' in sys.version:
    # from machine import Pin
    # here is where to place imports for Pico and ESP32
    print('true')
    usingPico=True
else:
# here is where to place imports for RPI
    import RPi.GPIO as GPIO
    print('False')
    usingPico=False
usingRPI = not  usingPico
####
import os
print(os.__name__)
print(sys.platform)
if sys.platform == 'esp32' or sys.platform == 'rp2020':
    print(f'platform is {sys.platform}')
    controller = 'microcontroller'
else:
    controller = 'rp1'
print(controller) 
#####
print(f'usingRPI: {usingRPI}') 
print(f'using RP2030 or ESP32: {usingPico}') 
# if usingPico:
#     myPin = 21
#     LED=Pin(myPin,Pin.OUT)
#     try:
        
#         while usingPico == True:
#             LED.value(0)
#             print('led on')
#             sleep(0.5)
#             LED.value(not LED.value)
#             print('led off')
#             sleep(0.5)
#         else:
#             print('not pico or esp32')
#             sleep(1)
#     except KeyboardInterrupt:
#         print('exit')
#         sys.exit()
    
    
def setup():
    if usingRPI:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red.GPIO.OUT)
    if usingPico:
        from machine import Pin
        
    
def turnLedOn():
    if usingRPI:
        GPIO.output(red,True)
        sleep(1)
    if usingPico:
        LED.value(1)
        print('led on')
        sleep(0.5)
        
def turnLedOff():
    if usingRPI:
        GPIO.output(red,False)
        sleep(1)
    if usingPico:
        LED.value(0)
        print('led off')
        sleep(0.5)
def cleanUp() :
    if usingRPI:
        GPIO.cleanup()
    if usingPico:
        try:
            pass
        except KeyboardInterrupt:
            print('exit')
            sys.exit()
    
setup()
red=20

blink_num=int(input('Howm many blinks do you wnat?'))
for i in range(0,blink_num):
    turnLedOn()
    turnLedOff()
cleanUp()
