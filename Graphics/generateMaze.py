import pygame
from pygame.locals import *

import logger
from Graphics.graphics import *
import Core.core as c
import enums
from enums import LogLevel

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
CELL_SIZE = 35 #35 #19 #9.2 #4.7 #1.5
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
COLOR_OF_MAZE = WHITE


    


def draw_maze_scene(maze, player):
    global DISPLAY
    DISPLAY.fill((0, 0, 0))  # Clear the screen with black
    for i in range(len(maze.board)):
        for j in range(len(maze.board[i])):
            cell = maze.board[i][j]
            x = j * CELL_SIZE - (player.pos_x * CELL_SIZE + CELL_SIZE // 2) + DISPLAY.get_rect().centerx
            y = i * CELL_SIZE - (player.pos_y * CELL_SIZE + CELL_SIZE // 2) + DISPLAY.get_rect().centery

            # if cell.top_wall:
            #     pygame.draw.rect(DISPLAY, (255, 255, 255), (x, y, CELL_SIZE, 2))  # Top wall
            # if cell.down_wall:
            #     pygame.draw.rect(DISPLAY, (255, 255, 255), (x, y + CELL_SIZE - 2, CELL_SIZE, 2))  # Bottom wall
            # if cell.left_wall:
            #     pygame.draw.rect(DISPLAY, (255, 255, 255), (x, y, 2, CELL_SIZE))  # Left wall
            # if cell.right_wall:
            #     pygame.draw.rect(DISPLAY, (255, 255, 255), (x + CELL_SIZE - 2, y, 2, CELL_SIZE))  # Right wall

            if cell.top_wall:
                pygame.draw.line(DISPLAY, COLOR_OF_MAZE, (x, y), (x + CELL_SIZE, y), 2)
            if cell.down_wall:
                pygame.draw.line(DISPLAY, COLOR_OF_MAZE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
            if cell.left_wall:
                pygame.draw.line(DISPLAY, COLOR_OF_MAZE, (x, y), (x, y + CELL_SIZE), 2)
            if cell.right_wall:
                pygame.draw.line(DISPLAY, COLOR_OF_MAZE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)

        draw_end_point(maze, player)
    

def draw_player(player):
    global DISPLAY

    x = DISPLAY.get_rect().centerx
    y = DISPLAY.get_rect().centery
    radius = CELL_SIZE // 3
    pygame.draw.circle(DISPLAY, RED, (x, y), radius)

def draw_end_point(maze, player):
    global DISPLAY
    pygame.draw.rect(DISPLAY,GREEN,
                     (
                         (len(maze.board) - 1) * CELL_SIZE + 2 - (player.pos_x * CELL_SIZE + CELL_SIZE // 2) + DISPLAY.get_rect().centerx,
                         (len(maze.board) - 1) * CELL_SIZE + 2 - (player.pos_y * CELL_SIZE + CELL_SIZE // 2) + DISPLAY.get_rect().centery,
                         CELL_SIZE - 2,
                         CELL_SIZE - 2
                     ))

def draw_start_screen():
    DISPLAY.fill(BLACK)
    
    title_message = "Welcome to the Maze Game"
    start_message = "Press KEY to start the game"
    quit_message = "Press ESC to quit"
    
    title_surf = FONT.render(title_message, True, WHITE)
    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    DISPLAY.blit(title_surf, title_rect)

    start_surf = FONT.render(start_message, True, WHITE)
    start_rect = start_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    DISPLAY.blit(start_surf, start_rect)

    quit_surf = FONT.render(quit_message, True, WHITE)
    quit_rect = quit_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
    DISPLAY.blit(quit_surf, quit_rect)
    
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                try:
                    c.terminate()
                except Exception as e:
                    logger.log(LogLevel.ERROR, str(e))
            elif event.type == KEYDOWN:
                return  # Návrat zpět do hlavní smyčky hry

            mouse = pygame.mouse.get_pos()
            draw_button(70, 600, "Quit", mouse, event, c.terminate)


def draw_button(pos_x, pos_y, text_message, mouse, event, func):
    start_surf = FONT.render(text_message, True, WHITE)
    start_rect = start_surf.get_rect(center=(pos_x,pos_y))
    DISPLAY.blit(start_surf, start_rect)
    pygame.display.update()

    if start_rect.collidepoint(mouse):
        if event.type == pygame.MOUSEBUTTONDOWN:
            func()

