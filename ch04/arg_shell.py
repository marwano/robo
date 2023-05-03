#!/usr/bin/env python3
import cmd
import motor

class RobotShell(cmd.Cmd):
    intro = 'Welcome to the robot shell. Type help or ? to list commands.'
    prompt = '(robot) '

    def do_EOF(self, line):
        return True

    def do_forward(self, line):
        if line:
            duration = float(line)
            motor.forward(duration)
        else:
            motor.forward()

    def do_backward(self, line):
        if line:
            duration = float(line)
            motor.backward(duration)
        else:
            motor.backward()

RobotShell().cmdloop()
