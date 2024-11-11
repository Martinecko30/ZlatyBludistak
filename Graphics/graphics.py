from pickle import GLOBAL

import pygame
from pygame import Color

from Core.gameobject import GameObject
from Graphics.drawposition import DrawPosition

DISPLAY = None
CLOCK = None
GAME_OBJECTS = []

def start():
    global DISPLAY, CLOCK
    pygame.init()
    pygame.display.set_caption('Zlaty Bludistak')
    DISPLAY = pygame.display.set_mode((1200, 800))
    CLOCK = pygame.time.Clock()
    DISPLAY.fill(Color('white'))

def end():
    pygame.quit()

def main_draw():
    global GAME_OBJECTS
    for game_object in GAME_OBJECTS:
        draw_object(game_object)

    pygame.display.flip()

def add_objects(_game_objects: list[GameObject]):
    global GAME_OBJECTS
    GAME_OBJECTS.extend(_game_objects)

def add_object(game_object: GameObject):
    global GAME_OBJECTS
    GAME_OBJECTS.append(game_object)

def draw_object(game_object: GameObject):
    global DISPLAY
    pygame.draw.circle(DISPLAY, Color('black'), (game_object.x, game_object.y), 30)

def draw_text(text: str, position: tuple[int, int], draw_position: DrawPosition):
    ...