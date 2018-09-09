import pygame
from process import process
from available import chkavail
from textinput import drawtext
from buyplant import *

pygame.init()

CLOCK = pygame.time.Clock()

FPS = 24
SCREEN = pygame.display.set_mode((960, 640))


def inventory():

    INVENT = pygame.image.load('../media/images/inventory.jpg')



    #file operations







    while True:

        process()
        SCREEN.blit(INVENT, (0, 0))
        a = []
        a = chkavail()

        text1 = drawtext(str(a[0])+'/1', 20)
        SCREEN.blit(text1, (250, 217))

        text1 = drawtext(str(a[1])+'/1', 20)
        SCREEN.blit(text1, (530, 220))

        text1 = drawtext(str(a[2]+a[3])+'/2', 20)
        SCREEN.blit(text1, (810, 215))

        text1 = drawtext(str(a[4]+a[5])+'/2', 20)
        SCREEN.blit(text1, (200, 480))

        text1 = drawtext(str(a[6]+a[7])+'/2', 20)
        SCREEN.blit(text1, (410, 480))

        text1 = drawtext(str(a[8]+a[9])+'/2', 20)
        SCREEN.blit(text1, (640, 480))

        text1 = drawtext(str(a[10]+a[11])+'/2', 20)
        SCREEN.blit(text1, (860, 480))



        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 20 < pos[0] < 70 and 20 < pos[1] < 55:

                break

            elif 120 < pos[0] < 280 and 247 < pos[1] < 290:
                buy_atomic()

            elif 400 < pos[0] < 560 and 250 < pos[1] < 290:

                buy_coal()

            elif 680 < pos[0] < 845 and 245 < pos[1] < 294:

                buy_natural()

            elif 75 < pos[0] < 240 and 500 < pos[1] < 560:

                buy_solar()

            elif 290 < pos[0] < 450 and 500 < pos[1] < 560:

                buy_wind()

            elif 517 < pos[0] < 650 and 510 < pos[1] < 560:

                buy_hydro()

            elif 740 < pos[0] < 900 and 510 < pos[1] < 560:

                buy_geothermal()

        CLOCK.tick(FPS)

