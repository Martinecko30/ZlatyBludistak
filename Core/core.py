import pygame
import sys
import time
from pygame import mixer 
from pygame.locals import *

import MazeGeneration.MazeGeneration as mz
import logger as log
from MazeGeneration import MazeGeneration
from enums import *
from Core.gameobject import GameObject
import Graphics.generateMaze as gz
import logger
import Graphics.graphics as graphics


UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
START_SOUND = "resources\\ElevatorMusic.mp3"
PLAYING_SOUND = "resources\\MinecraftTheme.mp3"
YOU_WIN_SOUND = "resources\\YouWin.mp3"

def terminate():
    logger.end()
    graphics.end()
    sys.exit()

class Player(GameObject):
    #def __init__(self, difficulty: str):
    def __init__(self, position: tuple[int, int], image: pygame.image, difficulty: Difficulty, maze: MazeGeneration.GameBoard):
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
        self.maze = maze
            
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
        return True, diff
    return False, None
    


def check_and_change_map(player: Player, maze):
    '''
    Parameter: player
    Returnig: none
    Functionality: zkontroluje jestli je čas na změnu mapy
    '''
    if time.time() - player.time_in_game > player.time_to_change_map:
        # MazeGeneration.generate_new_map()
        
        maze = None
        maze = mz.GameBoard(player.map_size[0])
        maze.generate_maze()
        # player.maze = mz.GameBoard(player.map_size[0])
        # player.maze.generate_maze()
        player.time_in_game = time.time()
        logger.log(LogLevel.INFO, "Cas na zmenu")
    return player, maze
        
    
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
    # try:
    #     if player.direction == UP:
    #         if player.pos_y > 0:
    #             return not maze.board[player.pos_x][player.pos_y ].top_wall
    #     elif player.direction == DOWN:
    #         if player.pos_y < len(maze.board) - 1:
    #             return not maze.board[player.pos_x][player.pos_y].down_wall
    #     elif player.direction == LEFT:
    #         if player.pos_x > 0:
    #             return not maze.board[player.pos_x][player.pos_y].left_wall
    #     elif player.direction == RIGHT:
    #         if player.pos_x < len(maze.board[0]) - 1:
    #             return not maze.board[player.pos_x][player.pos_y].right_wall
    #     return False
    # except:
    #     log.log(log_level.WARNING, "NECO S POHYBEM")
    direction = player.direction
    x, y = player.pos_x, player.pos_y

    if direction == UP:
        if y == 0 or maze.board[y][x].top_wall:
            return False
        return True
    elif direction == DOWN:
        if y == len(maze.board) - 1 or maze.board[y][x].down_wall:
            return False
        return True
    elif direction == LEFT:
        if x == 0 or maze.board[y][x].left_wall:
            return False
        return True
    elif direction == RIGHT:
        if x == len(maze.board[0]) - 1 or maze.board[y][x].right_wall:
            return False
        return True
    else:
        return False  # Neplatný směr

def start_new_game(diff: Difficulty):
    player = Player(position=(0,0), image=None, difficulty= diff, maze=MazeGeneration.GameBoard(diff.value))
    maze = mz.GameBoard(player.map_size[0])
    maze.generate_maze()
    
    return player, maze


def play_sound_starting():
    mixer.music.load(START_SOUND)
    mixer.music.play(-1)

def play_sound_playing():
    mixer.music.load(PLAYING_SOUND)
    mixer.music.play(-1)

def play_sound_You_win():
    mixer.music.load(YOU_WIN_SOUND)
    mixer.music.play()

def stop_playing_sound():
    if mixer.music.get_busy():
        mixer.music.stop()

def init_sound():
    mixer.init()