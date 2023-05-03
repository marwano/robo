#!/usr/bin/env python3
from struct import Struct
from collections import namedtuple

DEVICE = '/dev/input/js0'
TYPE_AXIS = 2
AXIS = {0: 'left_x', 1: 'left_y', 3: 'right_x', 4: 'right_y'}
MAX_VAL = 32767

Event = namedtuple('Event', 'time, value, type, number')

def handle_event(event):
    if event.type == TYPE_AXIS:
        name = AXIS.get(event.number)
        if name in ['left_y', 'right_y']:
            direction = 'backward' if event.value > 0 else 'forward'
            percent = round((abs(event.value) / MAX_VAL) * 100, 2)
            print(name, direction, percent)

def main():
    event_struct = Struct('I h B B')
    with open(DEVICE, 'rb') as js_device:
        while True:
            bytes = js_device.read(event_struct.size)
            event = Event(*event_struct.unpack(bytes))
            handle_event(event)

main()
