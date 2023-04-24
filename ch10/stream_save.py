#!/usr/bin/env python3
import os
import cv2

IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robo_stream.jpg'
TMP_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robo_stream_tmp.jpg'
FRAME_WIDTH = 320
FRAME_HEIGHT = 240

def save_frames(cap):
    counter = 0
    while True:
        counter += 1
        ret, frame = cap.read()
        assert ret, 'Cannot read frame from camera'
        frame = cv2.flip(frame, -1)
        cv2.imwrite(TMP_PATH, frame)
        os.replace(TMP_PATH, IMG_PATH)
        print('frames:', counter, end='\r', flush=True)

def init_camera():
    cap = cv2.VideoCapture(0)
    assert cap.isOpened(), 'Cannot open camera'
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    return cap

def main():
    cap = init_camera()
    try:
        save_frames(cap)
    finally:
        print('releasing video capture device...')
        cap.release()

main()
