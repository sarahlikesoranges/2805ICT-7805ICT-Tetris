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

    # Ah, i can instantly see an issue with the game being
    # paused and resumed. But we can sort that later.
    # Main gameloop
    while not paused:
        for event in pg.event.get():
            # Exits the game if the window is closed
            if event.type == pg.QUIT: sys.exit()

            # Main game loop
            # We will have functions to deal with these inputs

            # Listen for a key press
            # List of keys avaliable here:
            # https://www.pygame.org/docs/ref/key.html
            if event.type == pg.KEYDOWN:
                if event.key ==  pg.K_LEFT:
                    # Move the block left 1 square
                    pass
                if event.key == pg.K_RIGHT:
                    # Move the block right 1 square
                    pass
                if event.key == pg.K_UP:
                    # Do nothing? I think
                    pass
                if event.key == pg.K_DOWN:
                    # Move the block down at an faster rate
                    pass
                if event.key == pg.K_p:
                    # Pause the game
                    pass
                if event.key == pg.K_m:
                    # Toggle the music/audio
                    pass
                if event.key == pg.K_SPACE:
                    # Drop the block immediately
                    pass
        
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
    