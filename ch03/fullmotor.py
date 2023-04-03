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

def forward(duration=0.2, speed=3):
    set_throttle('R', speed)
    set_throttle('L', speed)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

def backward(duration=0.2, speed=3):
    set_throttle('R', speed, factor=-1)
    set_throttle('L', speed, factor=-1)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

def right(duration=0.2, speed=3):
    set_throttle('R', speed, factor=0.5)
    set_throttle('L', speed)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

def left(duration=0.2, speed=3):
    set_throttle('R', speed)
    set_throttle('L', speed, factor=0.5)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

def spin_right(duration=0.2, speed=3):
    set_throttle('R', speed, factor=-1)
    set_throttle('L', speed, factor=1)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

def spin_left(duration=0.2, speed=3):
    set_throttle('R', speed, factor=1)
    set_throttle('L', speed, factor=-1)
    time.sleep(duration)
    set_throttle('R', 0)
    set_throttle('L', 0)

if __name__ == "__main__":
    left(1)
    spin_right(0.5)
    spin_left(0.5)
