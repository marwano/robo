#!/usr/bin/env python3
import cv2

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

def main():
    frame = cv2.imread('photo.jpg')
    center = detect_face(frame)
    print('face center:', center)
    cv2.imshow('preview', frame)
    cv2.waitKey()

main()
