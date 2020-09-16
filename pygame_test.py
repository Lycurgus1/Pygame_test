import pygame, sys
# Imports several constant variables stored in module
from pygame.locals import *

# Intialises all imported modules before they can be used, must be included
pygame.init()
# Returns pygame surface objec, of width and height specified, tuple taken rather than two ints.
DISPLAYSURF = pygame.display.set_mode((400, 300))
# Sets caption text to appear at top of window
pygame.display.set_caption('Hello World!')
# Goes along forever until sys.exit mentioned
while True: # main game loop
    # For event in list that records all user actions, e.g. clicking, typing
    for event in pygame.event.get():
        # Checks if action was quit event, e.g. pressing escape
        if event.type == QUIT:
            # Opposite of pygame.init, ends the pygame instance
            pygame.quit()
            # Closes window and terminates program
            sys.exit()
    pygame.display.update()
    