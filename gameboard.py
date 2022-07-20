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