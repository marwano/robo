#!/usr/bin/env python3
import cmd
import motor

class RobotShell(cmd.Cmd):
    intro = 'Welcome to the robot shell. Type help or ? to list commands.'
    prompt = '(robot) '

    def do_forward(self, line):
        motor.forward()

    def do_backward(self, line):
        motor.backward()

RobotShell().cmdloop()
