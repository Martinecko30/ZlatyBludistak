import pygame
from pygame.locals import *
from Graphics.graphics import *






DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
CELL_SIZE = 30
BLACK = (255,255,255)
COLOR_OF_MAZE = BLACK



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
    except:
        print("aaa")    
    

def draw_player(player):
    #print("aa",player.pos_x, player.pos_y)
    try:
        x = player.pos_x * CELL_SIZE + CELL_SIZE // 2
        y = player.pos_y * CELL_SIZE + CELL_SIZE // 2
        radius = CELL_SIZE // 3
        pygame.draw.circle(DISPLAY, (255, 0, 0), (x, y), radius)
        pygame.display.flip()  # Update the display
    except:
        print("accc")