#!/usr/bin/env python3
from adafruit_crickit import crickit
import time
import os
from functools import partial

DC_ADJUST_R = float(os.environ.get('ROBO_DC_ADJUST_R', '1'))
DC_ADJUST_L = float(os.environ.get('ROBO_DC_ADJUST_L', '1'))
ADJUST = dict(R=DC_ADJUST_R, L=DC_ADJUST_L)
MOTOR = dict(R=crickit.dc_motor_1, L=crickit.dc_motor_2)
THROTTLE_SPEED = {0: 0, 1: 0.5, 2: 0.7, 3: 0.9}

def set_throttle(name, speed, factor=1):
    MOTOR[name].throttle = THROTTLE_SPEED[speed] * ADJUST[name] * factor

def movement(duration=0.2, speed=3, factor_r=1, factor_l=1):
    set_throttle('R', speed, factor_r)
    set_throttle('L', speed, factor_l)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

forward = partial(movement)
backward = partial(movement, factor_r=-1, factor_l=-1)
right = partial(movement, factor_r=0.5)
left = partial(movement, factor_l=0.5)
spin_right = partial(movement, factor_r=-1, factor_l=1)
spin_left = partial(movement, factor_r=1, factor_l=-1)
noop = lambda: None
