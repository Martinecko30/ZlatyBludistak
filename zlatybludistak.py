import traceback

import pygame
import sys, random, time, math
import logger
from Graphics import graphics
import Core.core as c
import MazeGeneration.MazeGeneration as mz
from enums import LogLevel

MAX_FPS = 120

def __main__():
    logger.start()

    try:
        graphics.start()
        running = True
        
        player = c.Player(difficulty = "tutorial")
        
        maze = mz.GameBoard(player.map_size[0])
        
        mz.generate_maze(maze)
        

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
            logger.log(LogLevel.INFO, f"{player.pos_x}, {player.pos_y}")
            #print(player.pos_x,player.pos_y)
            c.check_and_change_map(player)

            graphics.main_draw()

            graphics.draw_fog_of_war(5)

            graphics.flip_display()
            clock.tick(MAX_FPS)
    except:
        logger.log(LogLevel.ERROR, traceback.format_exc())
        terminate()

def terminate():
    logger.end()
    graphics.end()
    sys.exit()

if __name__ == "__main__":
    __main__()