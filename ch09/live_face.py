#!/usr/bin/env python3
import cv2
from face import detect_face

ESC_KEY = 27

def main():
    cap = cv2.VideoCapture(0)
    assert cap.isOpened(), 'Cannot open camera'
    while cv2.waitKey(1) not in [ord('q'), ESC_KEY]:
        ret, frame = cap.read()
        assert ret, 'Cannot read frame from camera'
        detect_face(frame)
        cv2.imshow('preview', frame)
    cap.release()

main()
