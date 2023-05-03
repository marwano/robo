#!/usr/bin/env python3
from adafruit_crickit import crickit
import time
import os

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

def forward(duration=0.2, speed=3):
    movement(duration, speed)

def backward(duration=0.2, speed=3):
    movement(duration, speed, factor_r=-1, factor_l=-1)

def right(duration=0.2, speed=3):
    movement(duration, speed, factor_r=0.5)

def left(duration=0.2, speed=3):
    movement(duration, speed, factor_l=0.5)

def spin_right(duration=0.2, speed=3):
    movement(duration, speed, factor_r=-1, factor_l=1)

def spin_left(duration=0.2, speed=3):
    movement(duration, speed, factor_r=1, factor_l=-1)
