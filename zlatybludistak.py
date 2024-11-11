import pygame
from pygame.locals import *
import sys
import random

from Core.gameobject import GameObject
from Graphics import graphics


def __main__():
    graphics.start()
    running = True

    graphics.add_object(GameObject((100, 100)))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

        graphics.main_draw()

def terminate():
    graphics.end()
    sys.exit()

if __name__ == "__main__":
    __main__()