import pygame
from process import process
from mainmenu import mainmenu

pygame.init()

CLOCK = pygame.time.Clock()

FPS = 24
SCREEN = pygame.display.set_mode((960, 640))


def resume():

    RESUME = pygame.image.load('../media/images/resume.gif')

    SCREEN.blit(RESUME, (0, 0))


    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 300 < pos[0] < 450 and 310 < pos[1] < 350:
                mainmenu()
                break

            elif 520 < pos[0] < 660 and 310 < pos[1] < 350:

                break


        CLOCK.tick(FPS)

