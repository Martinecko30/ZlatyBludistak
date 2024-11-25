import pygame
from pygame import Color
from graphics import *
from zlatybludistak import terminate

def end_screen():

    DISPLAY.fill('black')
    message = "You won"
    text_message = "You won"


    text_surf = FONT.render('YOU WON', True, 'white')
    text_rect = text_surf.get_rect()
    text_rect.center = (WIDTH // 2 , HEIGHT // 2 - 30)

    DISPLAY.blit(text_surf, text_rect)

    pygame.display.update()

