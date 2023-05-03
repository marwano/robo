#!/usr/bin/env python3
import json
from http.client import HTTPConnection
from struct import Struct
from collections import namedtuple

DEVICE = '/dev/input/js0'
TYPE_AXIS = 2
AXIS = {0: 'left_x', 1: 'left_y', 3: 'right_x', 4: 'right_y'}
MOTOR_AXIS = dict(left_y='L', right_y='R')
MAX_VAL = 32767

Event = namedtuple('Event', 'time, value, type, number')

def call_api(conn, url, data):
    body = json.dumps(data).encode()
    conn.request('POST', url, body)
    with conn.getresponse() as resp:
        resp.read()

def call_robot(conn, func, **args):
    return call_api(conn, '/' + func, args)

def handle_event(event, data, conn):
    if event.type == TYPE_AXIS:
        name = AXIS.get(event.number)
        if name in ['left_y', 'right_y']:
            level = round((event.value / MAX_VAL) * 3)
            if data[name] != level:
                print('level change:', name, level)
                data[name] = level
                motor = MOTOR_AXIS[name]
                factor = 1 if level <= 0 else -1
                args = dict(name=motor, speed=abs(level), factor=factor)
                call_robot(conn, 'set_throttle', **args)

def main():
    conn = HTTPConnection('robopi:8888')
    data = dict(left_y=0, right_y=0)
    event_struct = Struct('I h B B')
    with open(DEVICE, 'rb') as js_device:
        while True:
            bytes = js_device.read(event_struct.size)
            event = Event(*event_struct.unpack(bytes))
            handle_event(event, data, conn)

main()
