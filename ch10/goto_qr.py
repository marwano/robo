#!/usr/bin/env python3
import os
import sys
import cv2
import motor

MAX_MOVES = 20
IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robo_stream.jpg'
decoder = cv2.QRCodeDetector()

def decode_qr():
    img = cv2.imread(IMG_PATH)
    data, points, _ = decoder.detectAndDecode(img)
    return data

def goto(target):
    for i in range(MAX_MOVES):
        motor.forward(speed=1, duration=0.1)
        data = decode_qr()
        print(f'searching {i + 1}/{MAX_MOVES}, data: {data}')
        if data == target:
            return True
    return False

def main():
    target = sys.argv[1]
    print('target:', repr(target))
    found = goto(target)
    print('found status:', found)

main()
