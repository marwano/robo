#!/usr/bin/env python3
import string
import numpy as np
import cv2

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)

img = np.zeros(shape=(480, 640, 3), dtype=np.uint8)

cv2.circle(img, center=(200, 110), radius=100, color=RED)
cv2.line(img, pt1=(0, 0), pt2=(200, 110), color=GREEN)
cv2.rectangle(img, pt1=(50, 250), pt2=(350, 350), color=BLUE)

text = string.ascii_lowercase
font = cv2.FONT_HERSHEY_SIMPLEX
pos = (10, 380)
cv2.putText(img, text, org=pos, fontFace=font, fontScale=1, color=RED)

cv2.imshow('preview', img)
cv2.waitKey()
