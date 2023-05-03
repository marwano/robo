#!/usr/bin/env python3
from subprocess import check_output

SSH_USER = 'robo'
SSH_HOST = 'robopi'
SSH_CLI_CMD = '~/pyenv/bin/python ~/bin/cli.py'

def call_ssh(user, host, remote_cmd):
    cmd = ['ssh', f'{user}@{host}', remote_cmd]
    check_output(cmd)

def remote_robot(robot_cmd):
    call_ssh(SSH_USER, SSH_HOST, SSH_CLI_CMD + ' ' + robot_cmd)

def main():
    commands = ['forward', 'backward', 'spin_right', 'spin_left']
    for command in commands:
        print('remote robot command:', command)
        remote_robot(command)

main()
