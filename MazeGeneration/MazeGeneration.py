from random import choice
from diceroll import dice_roll

class MazeTile:
    def __init__(self, x_coord:int, y_coord:int):
        '''
        initializes MazeTile
        parameter: position:
        '''
        self.x_coord = int(x_coord)
        self.y_coord = int(y_coord)
        self.top_wall = False
        self.down_wall = False
        self.left_wall = False
        self.right_wall = False
        self.iterated = False

class GameBoard:
    def __init__(self, size:int):
        '''
        initializes MazeTile
        parameter: size:
        '''
        y_size, x_size = size
        self.size_of_board_y = y_size
        self.size_of_board_x = x_size
        self.board = []

    def generate_board(self):
        '''
        creates a list in GameBoard.board
        :return: None
        '''
        for y in range(self.size_of_board_y):
            self.board.append([])
            for x in range(self.size_of_board_x):
                tile = MazeTile(x, y)
                self.board[x].append(tile)
