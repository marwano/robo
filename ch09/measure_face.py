#!/usr/bin/env python3
import cv2
from statistics import mean
import time

BLUE = (255, 0, 0)
CV2_DIR = cv2.__path__[0]
CLASSIFIER_PATH = f'{CV2_DIR}/data/haarcascade_frontalface_default.xml'
face_classifier = cv2.CascadeClassifier(CLASSIFIER_PATH)

def get_center(x, y, w, h):
    return int(x + (w / 2)), int(y + (h / 2))

def prep_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(gray)

def detect_face(frame):
    clean = prep_face(frame)
    faces = face_classifier.detectMultiScale(clean)
    if len(faces) > 0:
        x, y, w, h = faces[0]
        center = get_center(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), BLUE, 2)
        cv2.drawMarker(frame, center, BLUE)
        return center

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
