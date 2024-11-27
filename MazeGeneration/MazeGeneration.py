from asyncio import current_task
from random import shuffle

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
        self.x_coord = int(x_coord)
        self.y_coord = int(y_coord)
        self.top_wall = True
        self.down_wall = True
        self.left_wall = True
        self.right_wall = True

    def break_walls(self, other):
        #Have to be neighboürs
        if self.y_coord < other.y_coord:
            self.down_wall = False
            other.top_wall = False

        elif self.y_coord > other.y_coord:
            self.top_wall = False
            other.down_wall = False

        elif self.x_coord < other.x_coord:
            self.right_wall = False
            other.left_wall = False

        elif self.x_coord > other.x_coord:
            self.left_wall = False
            other.right_wall = False

class GameBoard:
    def __init__(self, size:int):
        '''
        initializes MazeTile
        parameter: size:
        '''

        self.size_of_board_y = size
        self.size_of_board_x = size
        self.board = [[MazeCell(x, y) for x in range(self.size_of_board_x)] for y in
                         range(self.size_of_board_y)]

    def generate_maze(self):
        self.board = [[MazeCell(x, y) for x in range(self.size_of_board_x)] for
                      y in range(self.size_of_board_y)]
        visited_board = [[False for j in range(self.size_of_board_x)] for k in
                         range(self.size_of_board_y)]
        stack = []
        stack_visited = []

        current_cell = self.board[0][0]
        while True:
            #stack_visited.append(current_cell)

            neighbours = []
            x, y = current_cell.x_coord, current_cell.y_coord - 1
            if y >= 0 and not visited_board[y][x]:
                neighbours.append(self.board[y][x])

            x, y = current_cell.x_coord, current_cell.y_coord + 1
            if y < self.size_of_board_y and not visited_board[y][x]:
                neighbours.append(self.board[y][x])

            x, y = current_cell.x_coord - 1, current_cell.y_coord
            if x >= 0 and not visited_board[y][x]:
                neighbours.append(self.board[y][x])

            x, y = current_cell.x_coord + 1, current_cell.y_coord
            if x < self.size_of_board_x and not visited_board[y][x]:
                neighbours.append(self.board[y][x])

            if neighbours:
                shuffle(neighbours)
                new_cell = neighbours.pop()

                current_cell.break_walls(new_cell)
                visited_board[new_cell.y_coord][new_cell.x_coord] = True

                stack.append(current_cell)
                current_cell = new_cell

            elif stack:
                current_cell = stack.pop()

            else:
                break