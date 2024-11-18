# Imports
import pygame
from pygame import Color

from Core.gameobject import GameObject
from enums import DrawPosition

from pathlib import Path

# Constants
WIDTH, HEIGHT = 1200, 800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
GAME_OBJECTS = []

pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)


'''
VSETKO ESTE LEN TESTUJEM!!!
'''

def start() -> None:
    '''
    Initializes graphics
    :return: None
    '''
    global DISPLAY
    pygame.init()
    pygame.display.set_caption('Zlaty Bludistak')
    DISPLAY.fill(Color('white'))

def end() -> None:
    pygame.quit()

def main_draw() -> None:
    '''
    Main draw function
    Draws white screen then overdraws objects on top
    :return: None
    '''
    global GAME_OBJECTS

    DISPLAY.fill("white")

    for game_object in GAME_OBJECTS:
        draw_object(game_object)

def flip_display() -> None:
    '''
    Default call to finish current frame
    :return: None
    '''
    pygame.display.flip()

def add_objects(_game_objects: list[GameObject]) -> None:
    global GAME_OBJECTS
    GAME_OBJECTS.extend(_game_objects)

def add_object(game_object: GameObject) -> None:
    global GAME_OBJECTS
    GAME_OBJECTS.append(game_object)

def draw_object(game_object: GameObject) -> None:
    '''
    Private function
    Draws current game object
    :param game_object: Game object to draw
    :return:
    '''
    global DISPLAY

    if game_object.image is None:
        return

    DISPLAY.blit(game_object.image, game_object.position)
    pygame.display.flip()

def draw_text(text: str, position: tuple[int, int], bold: bool = False, italic: bool = False, color: Color = Color('black')) -> None:
    '''
    Draws text on given coordinates
    :param text: String of text to draw
    :param position: tuple[int, int] X and Y position of the text
    :param bold: If text is bold
    :param italic: If text is italic
    :param color: Color of text
    :return: None
    '''
    global FONT, DISPLAY
    FONT.set_bold(bold)
    FONT.set_italic(italic)
    text_surface = FONT.render(text, True, color)
    DISPLAY.blit(text_surface, position)

def draw_fog_of_war(radius: float) -> None:
    '''
    Draws fog of war in middle of screen
    :param radius: radius of the fog on the screen
    :return: None
    '''
    global DISPLAY, WIDTH, HEIGHT
    path_to_file = Path('resources/fog_of_war.png')
    fog_of_war = pygame.image.load(path_to_file).convert_alpha()
    size = fog_of_war.get_size()
    fog_of_war = pygame.transform.scale(fog_of_war, (size[0] * radius, size[1] * radius))

    top_left = (- abs((WIDTH / 2) - (size[0] * radius / 2)), - abs((HEIGHT / 2) - (size[1] * radius / 2)))

    DISPLAY.blit(fog_of_war, top_left)
    pygame.display.flip()

'''
Test functions
'''

def draw_rect(x: int, y: int):
    '''
    Test function
    :param x: X
    :param y: Y
    :return: None
    '''
    global DISPLAY
    pygame.draw.rect(DISPLAY, Color('red'), (x, y, 30, 30))
