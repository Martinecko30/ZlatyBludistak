import pygame

from Core.GameObject import GameObject

DISPLAY_SURFACE = None

def init():
    global DISPLAY_SURFACE
    pygame.init()
    DISPLAY_SURFACE = pygame.display.set_mode((1200, 800))

def main_draw_loop(game_objects: list[GameObject]):
    for game_object in game_objects:
        draw_object(game_object)

def draw_object(game_object: GameObject):
    # TODO: draw Object
    ...