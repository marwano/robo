#!/usr/bin/env python3
from os.path import dirname
from csv import DictReader
from emoji import emojize
from adafruit_crickit import crickit
import motor
import os
import time
import cv2

ITEMS_FILE = dirname(__file__) + '/items.csv'
IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robo_stream.jpg'
MAX_MOVES = 20
SERVO_ANGLES = dict(up=70, down=180)
decoder = cv2.QRCodeDetector()

def get_items():
    lines = [emojize(i) for i in open(ITEMS_FILE)]
    return list(DictReader(lines))

def decode_qr():
    img = cv2.imread(IMG_PATH)
    data, points, _ = decoder.detectAndDecode(img)
    return data

def goto(target, direction):
    motor_func = getattr(motor, direction)
    for i in range(MAX_MOVES):
        motor_func(speed=1, duration=0.1)
        data = decode_qr()
        if data == target:
            return True
        if data == 'end' and direction == 'forward':
            return False
    return False

def swing_arm():
    crickit.servo_2.angle = SERVO_ANGLES['up']
    time.sleep(0.5)
    crickit.servo_2.angle = SERVO_ANGLES['down']
    time.sleep(0.5)

def push_item(code):
    found = goto(code, 'forward')
    if found:
        motor.backward(speed=1, duration=0.3)
        swing_arm()
    goto('start', 'backward')

