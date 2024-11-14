import pygame
import sys, random, time, math

from Core.gameobject import GameObject
from Graphics import graphics

import Core.core as c


def __main__():
    graphics.start()
    running = True

    graphics.add_object(GameObject((100, 100)))

    player = c.Player(difficulty = "medium")
    maze = None # Zde vytvořit mapu

    last_time = 0
    while running:
        current_time = time.time()
        delta_time = (current_time - last_time) / 1000
        last_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
            c.handle_player_movement(event, player, maze)
        if c.check_if_is_over(player):
            # Zavolat funkci endScreen
            pass
        c.check_and_change_map(player)

        graphics.draw_fog_of_war(5)

        graphics.main_draw()

def terminate():
    graphics.end()
    sys.exit()

if __name__ == "__main__":
    __main__()