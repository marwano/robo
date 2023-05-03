#!/usr/bin/env python3
from adafruit_crickit import crickit
import time
import os

DC_ADJUST_R = float(os.environ.get('ROBO_DC_ADJUST_R', '1'))
DC_ADJUST_L = float(os.environ.get('ROBO_DC_ADJUST_L', '1'))
ADJUST = dict(R=DC_ADJUST_R, L=DC_ADJUST_L)
MOTOR = dict(R=crickit.dc_motor_1, L=crickit.dc_motor_2)
THROTTLE_SPEED = {0: 0, 1: 0.5, 2: 0.7, 3: 0.9}

def set_throttle(name, speed):
    MOTOR[name].throttle = THROTTLE_SPEED[speed] * ADJUST[name]

def forward(duration=0.2, speed=3):
    set_throttle('R', speed)
    set_throttle('L', speed)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

print('move forward for 0.5 seconds')
forward(duration=0.5)

for speed in [1, 2, 3]:
    print('move forward at speed:', speed)
    forward(speed=speed)
