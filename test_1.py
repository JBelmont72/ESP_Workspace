from machine import Pin
import sys
print(sys.version)
if 'MicroPython v1.21.0' in sys.version:
    print('true')
else:
    print('False')
import os
print(os.__name__)
print(sys.platform)
if sys.platform == 'esp32' or sys.platform == 'rp2020':
    print(f'platform is {sys.platform}')
    controller = 'microcontroller'
else:
    controller = 'rp1'
print(controller)    