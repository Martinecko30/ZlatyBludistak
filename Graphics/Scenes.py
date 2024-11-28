import pygame
from pygame.locals import *
from pygame import Color
from Graphics.graphics import *
from zlatybludistak import terminate
import Core.core as c
from enums import *

def end_screen(time_in_game):

    DISPLAY.fill('black')
    message = "You won"
    text_message = "You won"
    
    
    text_surf = FONT.render('YOU WON', True, 'white')
    text_rect = text_surf.get_rect()
    text_rect.center = (WIDTH // 2 , HEIGHT // 2 - 30)
    DISPLAY.blit(text_surf, text_rect)

    text_surf = FONT.render(f'YOUR TIME = {time_in_game}', True, 'white')
    text_rect = text_surf.get_rect()
    text_rect.center = (WIDTH // 2 , HEIGHT // 2 - 60)
    DISPLAY.blit(text_surf, text_rect)

    text_surf = FONT.render("Press ESC to quit", True, 'white')
    text_rect = text_surf.get_rect()
    text_rect.center = (WIDTH // 2 , HEIGHT // 2)
    DISPLAY.blit(text_surf, text_rect)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                terminate()
            elif event.type == KEYDOWN:
                return c.start_new_game(Difficulty.TUTORIAL)