#!/usr/bin/env python3
import cv2
from face import detect_face
from statistics import mean
import time

def get_detect_timing(frame):
    start = time.perf_counter()
    center = detect_face(frame)
    return time.perf_counter() - start

def main():
    frame = cv2.imread('photo.jpg')
    center = detect_face(frame.copy())
    print('face center:', center)
    stats = [get_detect_timing(frame.copy()) for i in range(10)]
    print('avg fps:', 1 / mean(stats))

main()
