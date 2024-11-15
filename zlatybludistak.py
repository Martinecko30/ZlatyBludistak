import pygame
import sys, random, time, math

from Core.gameobject import GameObject
from Graphics import graphics

import Core.core as c

import MazeGeneration.MazeGeneration as mz

MAX_FPS = 120


def __main__():
    graphics.start()
    running = True

    graphics.add_object(GameObject((100, 100)))

    player = c.Player(difficulty = "hard")
    maze = mz.GameBoard(player.map_size[0])
    maze.generate_board()
    maze = mz.maze_generation_main()

    clock = pygame.time.Clock()

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
        print(player.pos_x, player.pos_y)
        c.check_and_change_map(player)

        graphics.main_draw()

        graphics.draw_fog_of_war(5)

        graphics.flip_display()
        clock.tick(MAX_FPS)

def terminate():
    graphics.end()
    sys.exit()

if __name__ == "__main__":
    __main__()