from random import choice

class MazeCell:
    def __init__(self, x_coord:int, y_coord:int):
        '''
        initializes MazeTile
        parameter: position:
        '''
        """
        row == x |  ->   
        
        column == y | ↓
        """
        #False with wall means there is wall
        self.x_coord = int(x_coord)
        self.y_coord = int(y_coord)
        self.top_wall = False
        self.down_wall = False
        self.left_wall = False
        self.right_wall = False
        self.visited = False

class GameBoard:
    def __init__(self, size:int):
        '''
        initializes MazeTile
        parameter: size:
        '''
        #I have no idea if it is supposed to be square or rectangle, I act like rectangle

        self.size_of_board_y = size
        self.size_of_board_x = size
        self.board = []

    def generate_board(self):
        '''
        creates a list in GameBoard.board
        :return: None
        '''
        for y in range(self.size_of_board_y):
            self.board.append([])
            for x in range(self.size_of_board_x):
                tile = MazeCell(x, y)
                self.board[y].append(tile)




"""Keypoints for generation:
how does it work? Marks cell as visited and goes into neighbouring unvisited 
cell and it removes the wall between them. when there are no neighbours
it goes back to the last cell with an neighbour  

backtrack: checks if any neighbouring cell nas been unvisited  



"""


def generate_maze(board:GameBoard):
    board.generate_board()
    iterated = 0
    starting_cell = board.board[0][0]
    moves = []
    moves.append(board.board[starting_cell.y_coord][starting_cell.x_coord])

    while iterated < (board.size_of_board_y * board.size_of_board_x):

        new_cell = neighbouring_cell(board, starting_cell)
        while new_cell is None:
            new_cell = step_back(board, moves)

        #step_back return False for ending
        if not new_cell:
            break

        cells_wall_cut(board, starting_cell, new_cell, moves)

        '''print(f'starting_cell {starting_cell.y_coord}{starting_cell.x_coord} '
              f'\n new_cell {new_cell.y_coord}{new_cell.y_coord} \n' )'''

        starting_cell = new_cell

        iterated += 1

    # for item in board.board:
    #     for item2 in item:
    #         print(item2)
    #         print(item2.top_wall)
    #         print(item2.down_wall)
    #         print(item2.left_wall)
    #         print(item2.right_wall)
    #         print("//////////////////////////////////")
def step_back(board, move):
    '''

    :param board:
    :param move:
    :return:
    '''
    if not move:
        return False
    back_cell = move.pop()
    possible_neighbour = neighbouring_cell(board, back_cell)
    if possible_neighbour is None:
        step_back(board, move)
    return possible_neighbour

def neighbouring_cell(board, cell):
    '''
    :param board:
    :param cell:
    :return:
    '''
    coord_x = cell.x_coord
    coord_y = cell.y_coord
    possible_cells = []
    #for coord_y == 0:
    if coord_y == 0:
        if coord_x == 0:
            possible_cells = [board.board[coord_y][coord_x + 1],
                              board.board[coord_y + 1][coord_x]]

        elif 0 < coord_x < board.size_of_board_x - 1:
            possible_cells = [board.board[coord_y][coord_x + 1],
                              board.board[coord_y + 1][coord_x],
                              board.board[coord_y][coord_x - 1]]

        elif coord_x < board.size_of_board_x - 1:
            possible_cells = [board.board[coord_y][coord_x - 1],
                              board.board[coord_y + 1][coord_x]]

    # for coord_y between 0 and the last one:
    elif  0 < coord_y < board.size_of_board_y - 1:

        if coord_x == 0:
            possible_cells = [board.board[coord_y][coord_x + 1],
                              board.board[coord_y + 1][coord_x],
                              board.board[coord_y - 1][coord_x]]


        elif 0 < coord_x < board.size_of_board_x - 1:
            possible_cells = [board.board[coord_y][coord_x + 1],
                              board.board[coord_y + 1][coord_x],
                              board.board[coord_y - 1][coord_x],
                              board.board[coord_y][coord_x - 1]]

        elif coord_x == board.size_of_board_x - 1:
            possible_cells = [board.board[coord_y][coord_x - 1],
                              board.board[coord_y - 1][coord_x],
                              board.board[coord_y + 1][coord_x]]

    # for coord_y on the last column:
    elif coord_y == board.size_of_board_y - 1:
        if coord_x == 0:
            possible_cells = [board.board[coord_y][coord_x + 1],
                              board.board[coord_y - 1][coord_x]]

        elif 0 < coord_x < board.size_of_board_x - 1:
            possible_cells = [board.board[coord_y][coord_x + 1],
                              board.board[coord_y - 1][coord_x],
                              board.board[coord_y][coord_x - 1]]

        elif coord_x == board.size_of_board_x - 1:
            possible_cells = [board.board[coord_y][coord_x - 1],
                              board.board[coord_y - 1][coord_x]]

    possible_cells = [cell_ for cell_ in possible_cells if not cell_.visited]

    return dice_roll(possible_cells) if possible_cells else None

def cells_wall_cut(board, starting_cell, new_cell, move):
    '''

    :param board:
    :param starting_cell:
    :param new_cell:
    :param move:
    :return: None
    '''
    # checks which direction the cell is

    if new_cell.y_coord > starting_cell.y_coord:
        starting_cell.down_wall = True
        new_cell.top_wall = True

    elif new_cell.y_coord < starting_cell.y_coord:
        starting_cell.top_wall = True
        new_cell.down_wall = True

    elif new_cell.x_coord > starting_cell.x_coord:
        starting_cell.left_wall = True
        new_cell.right_wall = True

    elif new_cell.x_coord < starting_cell.x_coord:
        starting_cell.right_wall = True
        new_cell.left_wall = True

    if (new_cell.y_coord == board.size_of_board_y and
            new_cell.x_coord == board.size_of_board_x):
        new_cell.right_wall = True

    starting_cell.visited = True
    new_cell.visited = True

    move.append(board.board[new_cell.y_coord][new_cell.x_coord])

def dice_roll(numb_of_choices:list):
    '''
    :param numb_of_choices:
    :return: cosen  --- is universal
    '''
    chosen = choice(numb_of_choices)
    return chosen


"""
boar_test = GameBoard(10)
generate_maze(boar_test)"""
