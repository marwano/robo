#!/usr/bin/env python3
from adafruit_crickit import crickit
import time

MOTOR_R = crickit.dc_motor_1
MOTOR_L = crickit.dc_motor_2

def set_throttle(motor, value):
    motor.throttle = value

def forward():
    set_throttle(MOTOR_R, 0.9)
    set_throttle(MOTOR_L, 0.9)
    time.sleep(0.2)
    set_throttle(MOTOR_R, 0)
    set_throttle(MOTOR_L, 0)

forward()
