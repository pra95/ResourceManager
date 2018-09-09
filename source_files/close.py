import pygame
from process1 import process
pygame.init()

CLOCK = pygame.time.Clock()

FPS = 24
SCREEN = pygame.display.set_mode((960, 640))


def asktoquit():

    QUITWINDOW = pygame.image.load('../media/images/quitwindow.gif')

    i, k = 0, 0
    while True:

        SCREEN.blit(QUITWINDOW, (0, 0))
        pygame.display.update()
        process()
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 300 and pos[0] < 440 and pos[1] > 325 and pos[1] < 365:

                return 1


            elif pos[0] > 495 and pos[0] < 630 and pos[1] > 325 and pos[1] < 365:

                return 0




