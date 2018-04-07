# Star Pusher (a Sokoban clone)
# By Al Sweigart al@inventwithpython.com
# Creative Commons BY-NC_SA 3.0

import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30
WINWIDTH  = 800
WINHEIGHT = 600
HALF_WINWIDTH  = int(WINWIDTH  / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# The total width and height of each tile in pixels.
TILEWIDTH  = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 45

# How many pixels per frame the camera moves
CAN_MOVE_SPEED = 5 

# The percentage of outdoor tiles that have additional 
# decoration on them
OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = (  0, 170, 255)
WHITE      = (255, 255, 255)
BGCOLOR    = BRIGHTBLUE
TEXTCOLOR  = WHITE

UP    = 'up'
DOWN  = 'down'
LEFT  = 'left'
RIGHT = 'right'


def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

    # Pygame initialization and basic set up of the global variables.
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    # Surface object that is drawn to the actual computer screen
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    # Setting the title of the window and the font of the game
    pygame.display.set_caption('Star Pusher')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    # A global Dictionary that will contain all the Pygame
    # Surface objects returned by pygame.image.load()
    IMAGESDICT = {
        'uncovered goal': pygame.image.load('RedSelector.png'),
        'covered goal':   pygame.image.load('Selector.png'),
        'star':           pygame.image.load('Star.png'),
        'corner':         pygame.image.load('Wall Block Tall.png'),
        'wall':           pygame.image.load('Wood Block Tall.png'),
        'inside floor':   pygame.image.load('Plain block.png'),
        'outside floor':  pygame.image.load('Grass Block.png'),
        'title':          pygame.load.image('star_title.png'),
        'solved':         pygame.image.load('star_solved.png'),
        'princess':       pygame.image.load('princess.png'),
        'boy':            pygame.image.load('boy.png'),
        'catgirl':        pygame.image.load('catgirl.png'),
        'horngirl':       pygame.image.load('horngirl.png'),
        'pinkgirl':       pygame.image.load('pinkgirl.png'),
        'rock':           pygame.image.load('Rock.png'),
        'short tree':     pygame.image.load('Tree_Short.png'),
        'tall tree':      pygame.image.load('Tree_Tall.png'),
        'ugly tree':      pygame.image.load('Tree_Ugly.png')}

    # Map from level file to the Surface Object it represents.
    TILEMAPPING = {
        'x': IMAGESDICT['corner'],
        '#': IMAGESDICT['wall'],
        'o': IMAGESDICT['inside floor'],
        ' ': IMAGESDICT['outside floor']}

    OUTSIDEDECOMAPPING = {
        '1': IMAGESDICT['rock'],
        '2': IMAGESDICT['short tree'],
        '3': IMAGESDICT['tall tree'],
        '4': IMAGESDICT['ugly tree']}

    # PLAYERIMAGES is a list of all possible characters the player can be.
    # currentImage is the index of the player's current player image.
    currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['princess'],
                    IMAGESDICT['boy'],
                    IMAGESDICT['catgirl'],
                    IMAGESDICT['horngirl'],
                    IMAGESDICT['pinkgirl']]

    startScreen() # show the title screen until the user presses a key

    # Read in the levels from the text file
    levels = readLevelsFile('starPusherLevels.txt')
    currentLevelIndex = 0

    # The main game loop. This rloop runs a single level, then the user
    # finishes that level, the next/previous level is loaded.
    while True:
            result = runLevel(levels, currentLevelIndex)

            if result in ('solved', 'next'):
                # Go to the next level
                currentLevelIndex += 1
                if currentLevelIndex >= len(levels):
                    # If there are no more levels, go back to the first one.
                    currentLevelIndex = 0
            
            elif result == 'back':
                # Go to the previous level.
                currentLevelIndex -= 1
                if currentLevelIndex < 0:
                    # If there are no previous levels, go to the last one.
                    currentLevelIndex = len(levels) -1
            elif result == 'reset':
                pass # Do nothing. Loop re-calls runLevel() to reset the level
            

    
                
    
