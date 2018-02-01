#!/usr/bin/env python3

import time
import argparse
import RPi.GPIO as GPIO

# Parse command line arguments
parser = argparse.ArgumentParser(description='Simple example of handling LED with Raspberry Pi3')
parser.add_argument('gpio_num', type=int, nargs=None, help='GPIO number')
parser.add_argument('-n', '--num_repetition', type=int, help='The number of repetition',
        default=3)
args = parser.parse_args()
gpio_num = args.gpio_num
num_repetition = args.num_repetition

try:
  # Configure the target GPIO as an output
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(gpio_num, GPIO.OUT)
  
  # Power on and off
  for i in range(num_repetition):
      time.sleep(3)
      print('LED on')
      GPIO.output(gpio_num, 1)
      time.sleep(3)
      print('LED off')
      GPIO.output(gpio_num, 0)
finally:  
  # Cleanup
  GPIO.cleanup()
