#!/usr/bin/env python3
from http.client import HTTPConnection
from statistics import mean, stdev
import time
import json

def call_api(conn, url, data):
    body = json.dumps(data).encode()
    conn.request('POST', url, body)
    with conn.getresponse() as resp:
        resp.read()

def call_robot(conn, name, **args):
    return call_api(conn, '/' + name, args)

def get_noop_timing(conn):
    start = time.perf_counter()
    call_robot(conn, 'noop')
    return (time.perf_counter() - start) * 1000

conn_initial = HTTPConnection('robopi:8888')
get_noop_timing(conn_initial)
conn = HTTPConnection('robopi:8888')
init = get_noop_timing(conn)
stats = [get_noop_timing(conn) for i in range(100)]
print(' init:', init)
print('  max:', max(stats))
print('  avg:', mean(stats))
print('  min:', min(stats))
print('stdev:', stdev(stats))
