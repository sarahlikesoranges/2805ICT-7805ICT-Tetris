import json
import pygame as pg 
import sys
from src.config import *
from src.gameboard import *

__author__ = "Damian Mann, Sarah Puglisi, William Todd, Vinh Phuc Hoang"
__copyright__ = "Copyright 2022, Griffith University"
__license__ = "MIT"
__version__ = "0.1"

def run_game():
    pg.init
    paused = False
    # Grabs the stored config
    config = Config('config.json')
    # gameboard = GameBoard(config)
    # gameboard.print_gameboard()
    pg.display.set_mode((config.get_cols()*100, config.get_rows()*100))
    pg.display.set_caption('Tetris!')
    # Main gameloop
    while not paused:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        

if __name__ == '__main__':
    run_game()
    