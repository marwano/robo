#!/usr/bin/env python3
import pygame

FRAME_RATE = 60
WINDOW_SIZE = [100, 100]

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            print('event detected:', event)
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        clock.tick(FRAME_RATE)

main()
