#!/usr/bin/env python3
import cv2

BLUE = (255, 0, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX
decoder = cv2.QRCodeDetector()

def draw_box(frame, points, color, thickness):
    points = [(int(x), int(y)) for x, y in points]
    pt1, pt2, pt3, pt4 = points
    cv2.line(frame, pt1, pt2, color, thickness)
    cv2.line(frame, pt2, pt3, color, thickness)
    cv2.line(frame, pt3, pt4, color, thickness)
    cv2.line(frame, pt4, pt1, color, thickness)

def decode_qrcode(frame):
    data, matches, _ = decoder.detectAndDecode(frame)
    if data:
        cv2.putText(frame, f'data: {data}', (30, 30), FONT, 1, BLUE)
        draw_box(frame, matches[0], BLUE, thickness=3)
    return data

def main():
    frame = cv2.imread('hello.jpg')
    decoded_data = decode_qrcode(frame)
    print('decoded_data:', repr(decoded_data))
    cv2.imshow('preview', frame)
    cv2.waitKey()

main()
