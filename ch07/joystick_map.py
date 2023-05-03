#!/usr/bin/env python3
from struct import Struct
from collections import namedtuple

DEVICE = '/dev/input/js0'
TYPE_BUTTON = 1
TYPE_AXIS = 2
BUTTON = {0: 'cross', 1: 'circle', 2: 'triangle', 3: 'square'}
# BUTTON = {0: 'A', 1: 'B', 2: 'X', 3: 'Y'}
AXIS = {0: 'left_x', 1: 'left_y', 3: 'right_x', 4: 'right_y'}

Event = namedtuple('Event', 'time, value, type, number')

def handle_event(event):
    if event.type == TYPE_BUTTON:
        name = BUTTON.get(event.number)
        print('button -', name, event)
    if event.type == TYPE_AXIS:
        name = AXIS.get(event.number)
        print('axis -', name, event)

def main():
    event_struct = Struct('I h B B')
    with open(DEVICE, 'rb') as js_device:
        while True:
            bytes = js_device.read(event_struct.size)
            event = Event(*event_struct.unpack(bytes))
            handle_event(event)

main()
