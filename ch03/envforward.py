#!/usr/bin/env python3
from adafruit_crickit import crickit
import time
import os

DC_ADJUST_R = float(os.environ.get('ROBO_DC_ADJUST_R', '1'))
DC_ADJUST_L = float(os.environ.get('ROBO_DC_ADJUST_L', '1'))
ADJUST = dict(R=DC_ADJUST_R, L=DC_ADJUST_L)
MOTOR = dict(R=crickit.dc_motor_1, L=crickit.dc_motor_2)

def set_throttle(name, value):
    MOTOR[name].throttle = value * ADJUST[name]

def forward():
    set_throttle('R', 0.9)
    set_throttle('L', 0.9)
    time.sleep(0.2)
    set_throttle('R', 0)
    set_throttle('L', 0)

forward()
