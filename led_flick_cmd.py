#!/usr/bin/env python3

import time
import subprocess
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Simple example of handling LED with Raspberry Pi3')
parser.add_argument('gpio_num', type=int, nargs=None, help='GPIO number')
parser.add_argument('-n', '--num_repetition', type=int, help='The number of repetition',
        default=3)
args = parser.parse_args()
gpio_num = args.gpio_num
num_repetition = args.num_repetition

# Define commands
configure_command = ('gpio -g mode %i out' % (gpio_num)).split()
off_command = ('gpio -g write %i 0' % (gpio_num)).split()
on_command = ('gpio -g write %i 1' % (gpio_num)).split()

# Configure the target GPIO as an output
subprocess.check_call(configure_command)

for i in range(num_repetition):
    time.sleep(3)
    print('LED on')
    subprocess.check_call(on_command)
    time.sleep(3)
    print('LED off')
    subprocess.check_call(off_command)
