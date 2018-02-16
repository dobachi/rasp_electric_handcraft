#!/usr/bin/env python3
# coding: utf-8
  
import RPi.GPIO as GPIO
import time
  
basicPat = {
    "on":    (1, 1, 1, 1),
    "off":   (0, 0, 0, 0),
    "blink": (0, 1, 0, 1)
}
 
gpioLed = {
    "fine":  21,
    "cloud": 20,
    "rain":  16,
    "snow":  12
}
 
# Initialization
GPIO.setmode(GPIO.BCM)
gpioPins = list(gpioLed.values())
print(gpioPins)
GPIO.setup(gpioPins, GPIO.OUT)
 
try:
    # Define Sunny partly cloudy pattern
    ledPat = {}
    ledPat.update({"fine": basicPat["on"] + basicPat["on"] + basicPat["off"]})
    ledPat.update({"cloud": basicPat["blink"] + basicPat["blink"] + basicPat["off"]})
    ledPat.update({"rain":  basicPat["off"] + basicPat["off"] + basicPat["off"]})
    ledPat.update({"snow":  basicPat["off"] + basicPat["off"] + basicPat["off"]})
 
    for repeat in range(0, 3):
        for num in range(0, len(ledPat["fine"])):
            for weather, gpioPinNumber in gpioLed.items():
                GPIO.output(gpioPinNumber, ledPat[weather][num])
 
            time.sleep(0.25)
 
finally:
    GPIO.cleanup()
