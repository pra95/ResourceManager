# USE THIS METHODS OR CODE TO DO THE PROJECT.
# THIS IS REALLY A GREAT CODE
# NOTE: FIRST ERRASE THE PREVIOUS IMG AND THEN DRAW A NEW ONE

import pygame

pygame.init()


# variables

WIDTH, HEIGHT = 960, 640


# also we can set the time as follows


CLOCK = pygame.time.Clock()

FPS = 24

x = 5
y = 5

# first create a surface or a screen

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)

# then add objects(eg. drawings, images) to the screen

BACKGROUND = pygame.image.load("background.png").convert()

IMG = pygame.image.load("ball.png").convert_alpha()

position = IMG.get_rect()
SCREEN.blit(BACKGROUND, (0, 0))




def move(self):


    self.position = self.position.move(0, 10)

# create game loop

while True:

    for event in pygame.event.get():

        if event.type is pygame.QUIT:

            pygame.quit()
            exit()


    # kind of refresh the screen.
    pygame.display.flip()

    # use blit to add created objects to the screen

    SCREEN.blit(BACKGROUND, position, position)


    move(IMG.get_rect())

    SCREEN.blit(IMG, position)
    pygame.display.update()
    CLOCK.tick(FPS)




pygame.quit()
exit()