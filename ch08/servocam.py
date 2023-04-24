#!/usr/bin/env python3
from datetime import datetime
import cv2
from adafruit_crickit import crickit
from snapshot import save_photo, show_image, set_message
from pan import move_motor, init_motors

ESC_KEY = 27
ARROW_KEYS = {81: 'left', 82: 'up', 83: 'right', 84: 'down'}

def handle_key(key, frame, messages):
    if key == ord(' '):
        save_photo(frame)
        set_message(messages, 'saving photo...')
    elif key in ARROW_KEYS.keys():
        move_motor(ARROW_KEYS[key])
        set_message(messages, f'moving {ARROW_KEYS[key]}...')

def main():
    init_motors()
    cap = cv2.VideoCapture(0)
    assert cap.isOpened(), 'Cannot open camera'

    messages = []
    while (key := cv2.waitKey(1)) not in [ord('q'), ESC_KEY]:
        ret, frame = cap.read()
        assert ret, 'Cannot read frame from camera'
        handle_key(key, frame, messages)
        show_image(frame, messages)

    cap.release()

main()
