import pygame
import pygame.locals as pl
from pygame_textinput import *

# Defining variables
user_response = "test"

# Creating function to print text for user response
def display_question():
    # import pygame module in this program
    import pygame

    # activate the pygame library
    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()

    # define the RGB value for white,
    #  green, blue colour .
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # assigning values to X and Y variable
    X = 400
    Y = 400

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Show Text')

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)

    # create a text suface object,
    # on which text is drawn on it.
    text = font.render('GeeksForGeeks', True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)

    # infinite loop
    while True:

        # completely fill the surface object
        # with white color
        display_surface.fill(white)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display_surface.blit(text, textRect)
        for event in pygame.event.get():
            # Draws the surface object to the screen.
            pygame.display.update()

# Creating display text function to enable scaling applicaton
def display_text(events):
    # Feed it with events every frame
    if textinput.update(events):
        user_response = textinput.get_text()
        print(user_response)
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))

def test_response():
    if user_response.lower() == "yes":
        print("This test has worked")

if __name__ == "__main__":
    pygame.init()

    # Create TextInput-object
    textinput = TextInput()

    screen = pygame.display.set_mode((1000, 200))
    clock = pygame.time.Clock()

    while True:
        screen.fill((200, 225, 225))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        display_question()
        display_text(events)
        test_response()
        pygame.display.update()
        clock.tick(30)
