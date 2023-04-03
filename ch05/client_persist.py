#!/usr/bin/env python3
from http.client import HTTPConnection
import json

def call_api(conn, url, data):
    body = json.dumps(data).encode()
    conn.request('POST', url, body)
    with conn.getresponse() as resp:
        resp.read()

def call_robot(conn, name, **args):
    return call_api(conn, '/' + name, args)

conn = HTTPConnection('robopi:8888')
for speed in [1, 2, 3]:
    call_robot(conn, 'spin_right', speed=speed)
    call_robot(conn, 'spin_left', speed=speed)
