#!/usr/bin/env python3
from struct import Struct

DEVICE = '/dev/input/js0'

def main():
    event_struct = Struct('I h B B')
    with open(DEVICE, 'rb') as js_device:
        while True:
            bytes = js_device.read(event_struct.size)
            data = event_struct.unpack(bytes)
            time, value, type, number = data
            if type == 1:
                print(f'value:{value} number:{number}')

main()
