#!/usr/bin/env python3
from argparse import ArgumentParser
import motor

def parse_args():
    parser = ArgumentParser(description='robot cli')
    parser.add_argument('name', help='name of movement')
    parser.add_argument('--duration', type=float, help='movement duration')
    parser.add_argument('--speed', type=int, help='movement speed')
    return vars(parser.parse_args())

def main():
    args = parse_args()
    name = args.pop('name')
    func = getattr(motor, name)
    kwargs = {k: v for k, v in args.items() if v}
    print(f'calling {name} with kwargs {kwargs}')
    func(**kwargs)

main()
