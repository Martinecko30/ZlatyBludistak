import traceback

import pygame
import sys, random, time, math, datetime
import logger
from Graphics import graphics
import Core.core as c
import MazeGeneration.MazeGeneration as mz
from enums import *
import Graphics.generateMaze as gz
import Graphics.Scenes as gs

MAX_FPS = 120

def __main__():
    logger.start()

    try:
        graphics.start()
        running = True
        player, maze = c.start_new_game(Difficulty.TUTORIAL)
        
        #gz.draw_end_point(maze)

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
            is_end, time_in_game = c.check_if_is_over(player)
            if is_end:
                # Zavolat funkci endScreen
                s = str(datetime.timedelta(seconds=int(time_in_game)))
                print(s)
                #running = False
                player, maze = gs.end_screen(s)
                
            logger.log(LogLevel.INFO, f"{player.pos_x}, {player.pos_y}")
            #print(player.pos_x,player.pos_y)
            maze = c.check_and_change_map(player, maze)
            
            
            #graphics.main_draw()
            
            #graphics.draw_fog_of_war(5)

            #graphics.flip_display()
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