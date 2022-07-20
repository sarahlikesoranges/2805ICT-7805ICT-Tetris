# Controls the game board

class GameBoard:

    def __init__(self, config):
        self.config = config
        self.rows = config.get_rows()
        self.cols = config.get_cols()
        self.generate_board()

    def generate_board(self):
        size = self.rows * self.cols
        gameboard = [0] * size
        self.gameboard = gameboard

    def get_gameboard(self):
        return self.gameboard

    def print_gameboard(self):
        # This is a helper function - dont use in production
        # iterate over the gameboard and then print out each row
        gameboard_by_row = [self.gameboard[x:x+self.rows] for x in range(0, len(self.gameboard), self.rows)]
        for row in gameboard_by_row:
            print(row)