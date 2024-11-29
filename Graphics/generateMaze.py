import pygame
from pygame.locals import *
from Graphics.graphics import *
import Core.core as c
import enums




DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
CELL_SIZE = 35 #35 #19 #9.2 #4.7 #1.5
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
COLOR_OF_MAZE = WHITE


    


def draw_maze_scene(maze):
    DISPLAY.fill((0, 0, 0))  # Clear the screen with black
    try:
        for i in range(len(maze.board)):
            for j in range(len(maze.board[i])):
                cell = maze.board[i][j]
                x = j * CELL_SIZE
                y = i * CELL_SIZE

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
        pygame.display.flip()  # Update the display
        draw_end_point(maze)
    except:
        print("aaa")    
    

def draw_player(player):
    #print("aa",player.pos_x, player.pos_y)
    try:
        x = player.pos_x * CELL_SIZE + CELL_SIZE // 2
        y = player.pos_y * CELL_SIZE + CELL_SIZE // 2
        radius = CELL_SIZE // 3
        pygame.draw.circle(DISPLAY, RED, (x, y), radius)
        pygame.display.flip()  # Update the display
    except:
        print("accc")

def draw_end_point(maze):
    pygame.draw.rect(DISPLAY,GREEN,((len(maze.board)-1)*CELL_SIZE+2,(len(maze.board)-1)*CELL_SIZE+2,CELL_SIZE-2,CELL_SIZE-2))
    pygame.display.flip()

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
                    print("a")
                    print(e)
            elif event.type == KEYDOWN:
                return  # Návrat zpět do hlavní smyčky hry

            mouse = pygame.mouse.get_pos()
            #print(mouse)
            draw_button(70, 600, "Quit", mouse, event, c.terminate)
            #draw_button(200, 600, "Eazy", mouse, event, set_difficulty)


def draw_button(pos_x, pos_y, text_message, mouse, event, func):
    start_surf = FONT.render(text_message, True, WHITE)
    start_rect = start_surf.get_rect(center=(pos_x,pos_y))
    DISPLAY.blit(start_surf, start_rect)
    pygame.display.update()

    if start_rect.collidepoint(mouse):
        if event.type == pygame.MOUSEBUTTONDOWN:
            func(param)

