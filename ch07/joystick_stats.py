#!/usr/bin/env python3
import sys
import time
from struct import Struct
from collections import namedtuple
from types import SimpleNamespace

DEVICE = '/dev/input/js0'
TYPE_AXIS = 2
AXIS = {0: 'left_x', 1: 'left_y', 3: 'right_x', 4: 'right_y'}
MAX_VAL = 32767

Event = namedtuple('Event', 'time, value, type, number')

def stop_counter(data):
    duration = time.perf_counter() - data.start
    event_rate = data.events / duration
    print('---------- STATS ----------')
    print(f'      time: {duration:0.3f}s')
    print(f'    events: {data.events}')
    print(f'event rate: {event_rate:0.1f}')
    sys.exit()

def update_counter(data):
    data.events += 1
    print('events:', data.events)
    if data.events == 1:
        data.start = time.perf_counter()
    if data.events == 100:
        stop_counter(data)

def handle_event(event, data):
    if event.type == TYPE_AXIS:
        name = AXIS.get(event.number)
        if name == 'right_y':
            update_counter(data)

def main():
    data = SimpleNamespace(events=0, start=None)
    event_struct = Struct('I h B B')
    with open(DEVICE, 'rb') as js_device:
        while True:
            bytes = js_device.read(event_struct.size)
            event = Event(*event_struct.unpack(bytes))
            handle_event(event, data)

main()
