#!/usr/bin/env python3
import time
from adafruit_crickit import crickit

RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)
POLL_DELAY = 0.1

crickit.onboard_pixel.brightness = 0.01
while True:
    throttle = 1 if crickit.touch_1.value else 0
    color = RGB['red'] if crickit.touch_1.value else RGB['blue']
    crickit.onboard_pixel.fill(color)
    crickit.dc_motor_1.throttle = throttle
    time.sleep(POLL_DELAY)
