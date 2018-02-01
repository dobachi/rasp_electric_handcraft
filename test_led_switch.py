#!/usr/bin/env python3
# coding: utf-8
  
import RPi.GPIO as GPIO
import time
  
gpioLed = (21, 20, 16, 12, 25, 24, 23)
gpioSwitch = 18
 
try:
    # Initialization
    print('Start initilization...')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpioLed, GPIO.OUT)
    GPIO.setup(gpioSwitch, GPIO.IN)
 
    print('Test LEDs...')
    for led in gpioLed:
        print('LED{0} on'.format(led))
        GPIO.output(led, 1)
        time.sleep(1)
        print('LED{0} off'.format(led))
        GPIO.output(led, 0)
 
    print('Test the switch...')
    for num in range(0, 3):
        print('Push or release the switch')
        time.sleep(3)
        print(GPIO.input(gpioSwitch))
 
finally:
    GPIO.cleanup()
