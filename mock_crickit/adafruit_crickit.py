#!/usr/bin/env python3
import os
from unittest.mock import Mock, PropertyMock
from functools import partial

DEBUG = bool(os.environ.get('ROBO_DEBUG'))
PROP_VALUES = {'touch_1.value': True}

def print_msg(msg):
    if DEBUG:
        print('MOCK_CRICKIT:', msg)

def prop_access(name, *args):
    action = 'set' if args else 'get'
    if action == 'set':
        PROP_VALUES[name] = args[0]
    val = PROP_VALUES.get(name)
    print_msg(f'{action} crickit.{name}: {val!r}')
    return val

def pixel_fill(val):
    print_msg(f'call crickit.onboard_pixel.fill({val!r})')

def add_property(name):
    parent, child = name.split('.')
    property_mock = PropertyMock(side_effect=partial(prop_access, name))
    setattr(type(getattr(crickit, parent)), child, property_mock)

crickit = Mock()
crickit.onboard_pixel.fill = Mock(side_effect=pixel_fill)
names = [
    'onboard_pixel.brightness', 'touch_1.value', 'dc_motor_1.throttle',
    'dc_motor_2.throttle', 'servo_1.angle', 'servo_2.angle',
    'servo_1.actuation_range', 'servo_2.actuation_range']
for name in names:
    add_property(name)

def demo():
    print('starting mock_crickit demo...')
    crickit.onboard_pixel.brightness = 0.01
    crickit.onboard_pixel.fill(0xFF0000)
    crickit.touch_1.value
    crickit.dc_motor_1.throttle = 1
    crickit.dc_motor_2.throttle = -1
    crickit.servo_1.angle = 70
    crickit.servo_1.angle
    crickit.servo_2.angle = 90
    crickit.servo_2.angle
    crickit.servo_1.actuation_range = 142
    crickit.servo_2.actuation_range = 180

if __name__ == "__main__":
    demo()
