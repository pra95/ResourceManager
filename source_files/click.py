import pygame
from pressed import *
from resume import resume
from inventory import inventory
from available import chkavail

def click():

    clicked = pygame.mouse.get_pressed()

    pos = pygame.mouse.get_pos()

    a = []

    a = chkavail()


    if clicked[0] is 1:

        if 284 < pos[0] < 388 and 184 < pos[1] < 241:

            if a[0] is 1:
                pressed_atomic()

        elif 397 < pos[0] < 511 and 251 < pos[1] < 313:
            if a[1] is 1:
                pressed_coal()

        elif 500 < pos[0] < 649 and 184 < pos[1] < 249:
            if a[2] is 1:
                pressed_natural1()

        elif 272 < pos[0] < 392 and 320 < pos[1] < 383:
            if a[3] is 1:
                pressed_natural2()

        elif 580 < pos[0] < 700 and 280 < pos[1] < 340:
            if a[4] is 1:
                pressed_solar1()

        elif 436 < pos[0] < 573 and 367 < pos[1] < 426:
            if a[5] is 1:
                pressed_solar2()

        elif 781 < pos[0] < 907 and 266 < pos[1] < 343:
            if a[6] is 1:
                pressed_wind1()

        elif 480 < pos[0] < 620 and 480 < pos[1] < 550:
            if a[7] is 1:
                pressed_wind2()

        elif 644 < pos[0] < 760 and 375 < pos[1] < 440:
            if a[8] is 1:
                pressed_hydro1()

        elif 74 < pos[0] < 190 and 137 < pos[1] < 200:
            if a[9] is 1:
                pressed_hydro2()

        elif 410 < pos[0] < 526 and 88 < pos[1] < 156:
            if a[10] is 1:
                pressed_geothermal1()

        elif 144 < pos[0] < 260 and 249 < pos[1] < 313:
            if a[11] is 1:
                pressed_geothermal2()

        elif 24 < pos[0] < 76 and 17 < pos[1] < 50:

            resume()

        elif 900 < pos[0] < 940 and 10 < pos[1] < 50:

            inventory()
