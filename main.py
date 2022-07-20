import json
from config import *
from gameboard import *

__author__ = "Damian Mann, Sarah Puglisi, William Todd, Vinh Phuc Hoang"
__copyright__ = "Copyright 2022, Griffith University"
__license__ = "MIT"
__version__ = "0.1"

def run_game():
    # Grabs the stored config
    config = Config('config.json')
    gameboard = GameBoard(config)
    gameboard.print_gameboard()
    

if __name__ == '__main__':
    run_game()