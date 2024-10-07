CELL_UNKNOWN = "?"

def new_grid(width, height, default_value):
    g = []
    for _ in range(height):
        g.append([default_value]*width)
    return g

class MineSweeper:
    def __init__ (self, width, height):
        self.external = new_grid(width, height, CELL_UNKNOWN)
        self.internal = new_grid(width, height, '_') 

        self.width = width
        self.height = height

    def board_state(self):
        return self.external

    def on_click(self, row, column):
        if self.is_bomb(row, column):
            return "Game Lost"

        self.reveal_tile(row, column)

    def reveal_tile(self, row, col):
        # we know (row, col) isn't a bomb
        if self.external[row][col] != CELL_UNKNOWN:
            return
        num_bombs = self.num_adjacent_bombs(row, col)
        self.external[row][col] = str(num_bombs) if num_bombs > 0 else '0'
        if num_bombs == 0:  # zero adjacent bombs
            for (nr, nc) in self.get_neighbors(row, col):
                self.reveal_tile(nr, nc)

    def is_bomb(self, row, column):
        return self.internal[row][column] == '*'

    def num_adjacent_bombs(self, row, column):
        count = 0
        for (n_x, n_y) in self.get_neighbors(row, column):
            if self.is_bomb(n_x, n_y):
                count += 1
        return count
                
    def get_neighbors(self, row, column):
        neighbors = []
        for ddx in [-1, 0, 1]:
            for ddy in [-1, 0, 1]:
                if ddx == 0 and ddy == 0: 
                    continue
                new_row = row + ddx
                new_col = column + ddy
                if (new_row < 0 or new_row >= self.height) or (new_col < 0 or new_col >= self.width): 
                    continue
                neighbors.append((new_row, new_col))
        return neighbors


class Bot:
    def __init__(self, board, width, height):
        self.board = board
        self.bot_internal = new_grid(width, height, CELL_UNKNOWN)

    def solve_game(self):
        some_x, some_y = 0, 0  
        self.board.on_click(some_x, some_y)
