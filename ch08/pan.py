#!/usr/bin/env python3
from adafruit_crickit import crickit
import time

ANGLE_STEP = 2
PAN = dict(servo=crickit.servo_1, min=30, max=110, start=70, range=142)
TILT = dict(servo=crickit.servo_2, min=90, max=180, start=180, range=180)
MOVE = dict(left=(PAN, -1), right=(PAN, 1), up=(TILT, -1), down=(TILT, 1))

def move_motor(direction):
    motor, factor = MOVE[direction]
    new_angle = motor['servo'].angle + (ANGLE_STEP * factor)
    if motor['min'] <= new_angle <= motor['max']:
        motor['servo'].angle = new_angle

def init_motors():
    for motor in [PAN, TILT]:
        motor['servo'].actuation_range = motor['range']
        motor['servo'].angle = motor['start']

def main():
    init_motors()

    for i in range(20):
        print('moving left and up')
        move_motor('left')
        move_motor('up')
        time.sleep(0.1)

    for i in range(20):
        print('moving right and down')
        move_motor('right')
        move_motor('down')
        time.sleep(0.1)

if __name__ == "__main__":
    main()
