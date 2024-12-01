import traceback

import pygame
import sys, random, time, math, datetime
import logger
from Graphics import graphics, generateMaze
import Core.core as c
from enums import *
import Graphics.generateMaze as gz
import Graphics.Scenes as gs

MAX_FPS = 120

def __main__():
    logger.start()

    try:
        c.init_sound()
        c.play_sound_starting()
        graphics.start()
        diff = gz.draw_start_screen()
        c.stop_playing_sound()
        c.play_sound_playing()
        running = True
        player, maze = c.start_new_game(diff)
        
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
                    c.terminate()
                c.handle_player_movement(event, player, maze)
            is_end, time_in_game = c.check_if_is_over(player)
            if is_end:
                # Zavolat funkci endScreen
                c.stop_playing_sound()
                c.play_sound_You_win()
                
                s = str(datetime.timedelta(seconds=int(time_in_game)))
                #print(s)
                #running = False
                player, maze = gs.end_screen(s)
                c.stop_playing_sound()
                c.play_sound_playing()

            #print(player.pos_x,player.pos_y)
            player, maze = c.check_and_change_map(player, maze)

            generateMaze.draw_maze_scene(maze, player)
            generateMaze.draw_player(player)
            
            graphics.draw_fog_of_war(5)

            graphics.flip_display()
            clock.tick(MAX_FPS)
    except:
        logger.log(LogLevel.ERROR, traceback.format_exc())
        c.terminate()



if __name__ == "__main__":
    __main__()