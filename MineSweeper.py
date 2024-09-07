"""
.......................
.......................
.........111...........
.........101...........
.........202.......8...
.........123...........
.......................
.......................
"""

CELL_UNKNOWN = "?"

def new_grid(self, width, height, default_value):
    g = []
    for _ in range(height):
        g.append([default_value]*width)
    return g

class MineSweeper:
    def __init__ (self, width, height):
        self.external = ???
        self.internal = list(list(CELL_UNKNOWN for _ in range(width)) for _ in range(height))

        self.internal=[]
        self.external=[]
        for i in range(len(height)):
            new_row=[]
            for j in range(len(width)):
                new_row.append('_')
                # TODO: talk about this
            self.internal.append(new_row)
            self.external.append(new_row)
        self.width=width
        self.height=height

    def board_state (self):
        return self.external

    def on_click(self, row, column):
        if self.is_bomb(row, column):
            return "Game Lost"

        self.reveal_tile(row, column)
        #for ddx, ddy in [(0,1), (0,-1), (-1, 0), (1, 0)]:
        #    pass

    def reveal_tile(self, row, col):
        # we know (row, col) isn't a bomb
        if self.external[row][col] != CELL_UNKNOWN:
            return
        num_bombs = self.num_adjacent_bombs(row, col)
        self.external[row][col]=num_bombs
        if num_bombs > 0:
            return
        else: # zero adjacent bombs
            for (nr, nc) in self.get_neighbors(row, col):
                self.reveal_tile(row, col)

    def is_bomb (self, row, column):
        return self.internal[row][column]=='*'

    def num_adjacent_bombs(self, row, column): 
        count=0
        for (n_x, n_y) in self.get_neighbors(row, column):
            if self.is_bomb(n_x, n_y):
                count+=1
        return count
                
    def get_neighbors (self, row,column):
        neighbors=[]
        for ddx in [-1,0,1]:
            for ddy in [-1,0,1]:
                if ddx == 0 and ddy == 0: continue
                new_row = row+ddx
                new_col = column+ddy
                if (new_row<0 or new_row>=self.height) or (new_col<0 or new_col>=self.width): continue
                neighbors.append((new_row, new_col))
        return neighbors

@functools.lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


"""

 11111111
 1ynnyn??
 1n??
"""

class Bot:
    def __init__(self, board):
        self.board = board
        #2d array --> bomb or CELL_UNKNOWN
        self.bot_internal = list(list(CELL_UNKNOWN for _ in range(width)) for _ in range(height))

    
    def solve_game(self):
        while True:
            self.board.on_click(some_x, some_y)
