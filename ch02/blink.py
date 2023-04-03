#!/usr/bin/env python3
import time
from adafruit_crickit import crickit

RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)

crickit.onboard_pixel.brightness = 0.01
while True:
    for name in RGB:
        print(name)
        crickit.onboard_pixel.fill(RGB[name])
        time.sleep(0.1)
