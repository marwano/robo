#!/usr/bin/env python3
from urllib.request import urlopen
import json

ROBO_URL = 'http://robopi:8888/'

def call_api(url, data):
    data = json.dumps(data).encode()
    urlopen(url, data).read()

def call_robot(name, **args):
    call_api(ROBO_URL + name, args)

call_robot('forward')
call_robot('backward')
call_robot('forward', duration=0.5, speed=1)
call_robot('backward', duration=0.5, speed=1)
call_robot('spin_right')
call_robot('spin_left')
