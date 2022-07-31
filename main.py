import json
import pygame as pg 
import sys
from src.config import *
from src.gameboard import *

__author__ = "Damian Mann, Sarah Puglisi, William Todd, Vinh Phuc Hoang"
__copyright__ = "Copyright 2022, Griffith University"
__license__ = "MIT"
__version__ = "0.1"

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def run_game():
    pg.init()
    paused = False
    # Grabs the stored config
    config = Config('config.json')
    # gameboard = GameBoard(config)
    # gameboard.print_gameboard()
    display_width = config.get_cols() * 100
    display_height = config.get_rows() * 100
    display = pg.display.set_mode((display_width, display_height))
    clock = pg.time.Clock()
    pg.display.set_caption('Tetris!')
    # Main gameloop
    while not paused:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        # Display title page -- Will need to refactor (im just playing around)
        display.fill((255, 255, 255))
        largeText = pg.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Tetris!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        display.blit(TextSurf, TextRect)
        pg.display.update()
        clock.tick(15)

if __name__ == '__main__':
    run_game()
    