import pygame
from pygame import Color
from Graphics.graphics import *
from zlatybludistak import terminate

def end_screen(time_in_game):

    DISPLAY.fill('black')
    message = "You won"
    text_message = "You won"
    print("a")
    while True:
        text_surf = FONT.render('YOU WON', True, 'white')
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH // 2 , HEIGHT // 2 - 30)
        DISPLAY.blit(text_surf, text_rect)

        text_surf = FONT.render(f'YOUR TIME = {time_in_game}', True, 'white')
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH // 2 , HEIGHT // 2 - 60)

        DISPLAY.blit(text_surf, text_rect)

        pygame.display.update()

