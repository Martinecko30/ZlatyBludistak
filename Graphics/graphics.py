import pygame
from pygame import Color

from Core.gameobject import GameObject
from Graphics.drawposition import DrawPosition

DISPLAY = None
CLOCK = None
GAME_OBJECTS = []
WIDTH, HEIGHT = 1200, 800

from pathlib import Path

'''
VSETKO ESTE LEN TESTUJEM!!!
'''

def start():
    global DISPLAY, CLOCK
    pygame.init()
    pygame.display.set_caption('Zlaty Bludistak')
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
    CLOCK = pygame.time.Clock()
    DISPLAY.fill(Color('white'))

def end():
    pygame.quit()

def main_draw():
    global GAME_OBJECTS

    DISPLAY.fill("white")

    for game_object in GAME_OBJECTS:
        draw_object(game_object)

def flip_display():
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

def draw_fog_of_war(radius: float):
    global DISPLAY, WIDTH, HEIGHT
    path_to_file = Path('resources/fog_of_war.png')
    fog_of_war = pygame.image.load(path_to_file).convert_alpha()
    size = fog_of_war.get_size()
    fog_of_war = pygame.transform.scale(fog_of_war, (size[0] * radius, size[1] * radius))

    top_left = (- abs((WIDTH / 2) - (size[0] * radius / 2)), - abs((HEIGHT / 2) - (size[1] * radius / 2)))

    DISPLAY.blit(fog_of_war, top_left)
    pygame.display.flip()

def draw_rect(x: int, y: int):
    global DISPLAY
    pygame.draw.rect(DISPLAY, Color('red'), (x, y, 30, 30))

