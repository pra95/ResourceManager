import pygame
from process import process
from close import asktoquit
from sound import sound
from credits import credit
from help import helps

pygame.init()

CLOCK = pygame.time.Clock()

FPS = 24
SCREEN = pygame.display.set_mode((960, 640))


def mainmenu():

    MENU = pygame.image.load('../media/images/mainmenu.jpg')

    i = 0
    while True:

        process()
        SCREEN.blit(MENU, (0, 0))
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()


        if clicked[0] is 1:

            if 330 < pos[0] < 625 and 160 < pos[1] < 220:

                pygame.time.delay(500)
                break

            elif 330 < pos[0] < 625 and 250 < pos[1] < 300:

                sound()

            elif 330 < pos[0] < 625 and 330 < pos[1] < 390:

                helps()

            elif 330 < pos[0] < 625 and 425 < pos[1] < 480:

                credit()

            elif 330 < pos[0] < 625 and 510 < pos[1] < 570:

                i = asktoquit()
                if i is 1:
                    pygame.quit()
                    exit()


        CLOCK.tick(FPS)

