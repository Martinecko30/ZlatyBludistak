import pygame
import sys
import time
from pygame.locals import *

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"



class Player:
    def __init__(self, difficulty: str):
        self.pos_x = 0
        self.pos_y = 0
        self.direction = None
        self.difficulty = difficulty
        self.time_in_game = time.time()

        self.set_difficulty() 
            
    def set_difficulty(self):
        match self.difficulty:
            case "tutorial":
                self.time_to_change_map = 30
                self.map_size = [20, 20]
            case "easy":
                self.time_to_change_map = 20
                self.map_size = [40, 40]
            case "medium":
                self.time_to_change_map = 10
                self.map_size = [80, 80]
            case "hard":
                self.time_to_change_map = 5
                self.map_size = [160, 160]
            case "dark souls":
                self.time_to_change_map = 1
                self.map_size = [500, 500]
            case _:
                self.time_to_change_map = 10
                self.map_size = [20, 20]

def check_and_change_map(player: Player):
    '''
    Parameter: player
    Returnig: none
    Functionality: zkontroluje jestli je čas na změnu mapy
    '''
    if time.time() - player.time_in_game > player.time_to_change_map:
        # MazeGeneration.generate_new_map()
        pass
    
def handle_player_movement(event, player, maze):
    '''
    Parameter: event, player, map
    Returnig: none
    Functionality: NÁVRH po získání eventu pohyb zkontroluje jesli může udělat pohyb a popř. ho udělá
    '''
    get_key_direction(event, player)
    if can_make_move(player, maze):
        move_player(player)  

def get_key_direction(event, player: Player):
    '''
    Parameter: event
    Returnig: direction
    Functionality: vrátí pohyb a uloži ho hráče
    '''
    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        terminate()
    if event.type == pygame.KEYDOWN:
        if event.key == K_LEFT or event.key == K_a:
            player.direction = LEFT
            return LEFT
        elif event.key == K_RIGHT or event.key == K_d:
            player.direction = RIGHT
            return RIGHT
        elif event.key == K_UP or event.key == K_w:
            player.direction = UP
            return UP
        elif event.key == K_DOWN or event.key == K_s:
            player.direction = DOWN
            return DOWN
        player.direction = None
        return None

def move_player(player: Player):
    '''
    Parameter: player
    Returnig: none
    Functionality: obsluhuje pohyb hráče
    '''
    if player.direction == UP and player.pos_y > 0:
        player.pos_y -= 1
    elif player.direction == DOWN and player.pos_y < player.map_size[1]:
        player.pos_y += 1
    elif player.direction == LEFT and player.pos_x > 0:
        player.pos_x -= 1
    elif player.direction == RIGHT and player.pos_x < player.map_size[0]:
        player.pos_x += 1



def can_make_move(player: Player, maze):
    '''
    Parameter: player, map
    Returnig: true, false
    Functionality: Zjisti jeslti může udělat pohyb (jestli tam není zed)

    Zatím nic nebot nevím jak bude implementováné bludiště
    '''
    return True






def terminate():
    '''
    Parameter: none
    Returnig: none
    Functionality: ukončí aplikaci
    '''
    pygame.quit()
    sys.exit()


