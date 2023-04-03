#!/usr/bin/env python3
import cmd
import motor

def get_kwargs(line):
    kwargs = dict()
    items = line.split()
    if len(items) > 0:
        kwargs['duration'] = float(items[0])
    if len(items) > 1:
        kwargs['speed'] = int(items[1])
    return kwargs

class RobotShell(cmd.Cmd):
    intro = 'Welcome to the robot shell. Type help or ? to list commands.'
    prompt = '(robot) '

    def do_EOF(self, line):
        return True

    def precmd(self, line):
        print('executing', repr(line))
        return line

    def do_forward(self, line):
        motor.forward(**get_kwargs(line))

    def do_backward(self, line):
        motor.backward(**get_kwargs(line))

    def do_right(self, line):
        motor.right(**get_kwargs(line))

    def do_left(self, line):
        motor.left(**get_kwargs(line))

    def do_spin_right(self, line):
        motor.spin_right(**get_kwargs(line))

    def do_spin_left(self, line):
        motor.spin_left(**get_kwargs(line))

RobotShell().cmdloop()
