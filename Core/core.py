import pygame
import sys
import time
from pygame.locals import *

import MazeGeneration.MazeGeneration as mz
import logger as log
from enums import *
from Core.gameobject import GameObject

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"



class Player(GameObject):
    #def __init__(self, difficulty: str):
    def __init__(self, position: tuple[int, int], image: pygame.image, difficulty: Difficulty):
        #self.pos_x = 0
        #self.pos_y = 0
        super().__init__(position, image)
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.direction = None
        self.difficulty = difficulty
        self.time_in_game = time.time()
        self.start_time = time.time()

        self.set_difficulty() 
            
    def set_difficulty(self):
        match self.difficulty:
            #case "tutorial":
            case Difficulty.TUTORIAL:
                self.time_to_change_map = 30
                self.map_size = [20, 20]
            #case "easy":
            case Difficulty.EASY:
                self.time_to_change_map = 20
                self.map_size = [40, 40]
            #case "medium":
            case Difficulty.MEDIUM:
                self.time_to_change_map = 10
                self.map_size = [80, 80]
            #case "hard":
            case Difficulty.HARD:
                self.time_to_change_map = 5
                self.map_size = [160, 160]
            #case "dark souls":
            case Difficulty.DARK_SOULS:
                self.time_to_change_map = 1
                self.map_size = [500, 500]
            case _:
                self.time_to_change_map = 10
                self.map_size = [20, 20]

def check_if_is_over(player: Player):
    '''
    Parameter: player
    Returnig: none
    Functionality: Zkontroluje jestli je hráč na konci mapy
    '''
    if player.pos_x == player.map_size[0] - 1 and player.pos_y == player.map_size[1] - 1:
        #print("Je konec hry")
        diff = time.time() - player.start_time
        # Zavolat fuknci endscreen
        return True
    


def check_and_change_map(player: Player, maze):
    '''
    Parameter: player
    Returnig: none
    Functionality: zkontroluje jestli je čas na změnu mapy
    '''
    if time.time() - player.time_in_game > player.time_to_change_map:
        # MazeGeneration.generate_new_map()
        mz.generate_maze(maze)
        player.time_in_game = time.time()
        #print("Cas na zmenu")
        
    
def handle_player_movement(event, player, maze):
    '''
    Parameter: event, player, map
    Returnig: none
    Functionality: NÁVRH po získání eventu pohyb zkontroluje jesli může udělat pohyb a popř. ho udělá
    '''
    if None is not get_key_direction(event, player):
        if can_make_move(player, maze):
            move_player(player)

def get_key_direction(event, player: Player):
    '''
    Parameter: event
    Returnig: direction
    Functionality: vrátí pohyb a uloži ho hráče
    '''
    
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
    '''
    try:
        if player.direction == UP:
            if player.pos_y > 0:
                return not maze.board[player.pos_x][player.pos_y - 1].top_wall
        elif player.direction == DOWN:
            if player.pos_y < len(maze.board[0]) - 1:
                return not maze.board[player.pos_x][player.pos_y + 1].down_wall
        elif player.direction == LEFT:
            if player.pos_x > 0:
                return not maze.board[player.pos_x - 1][player.pos_y].left_wall
        elif player.direction == RIGHT:
            if player.pos_x < len(maze.board) - 1:
                return not maze.board[player.pos_x + 1][player.pos_y].right_wall
        return False
    except:
        log.log(log_level.WARNING, "NECO S POHYBEM")
