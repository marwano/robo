#!/usr/bin/env python3
import pygame

FRAME_RATE = 60
WINDOW_SIZE = [100, 100]

def handle_event(event):
    if event.type == pygame.JOYBUTTONDOWN:
        print('button pressed', event.button)
    if event.type == pygame.JOYAXISMOTION:
        print('axis motion', event.axis, event.value)

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    joystick = pygame.joystick.Joystick(0)
    print('joystick name:', joystick.get_name())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            handle_event(event)
        clock.tick(FRAME_RATE)

main()
