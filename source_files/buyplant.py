import pygame
from process import process
from textinput import drawtext
from available import chkavail

pygame.init()

CLOCK = pygame.time.Clock()

FPS = 24
SCREEN = pygame.display.set_mode((960, 640))


def buy_atomic():

    BUY = pygame.image.load('../media/images/buy.gif')


    SCREEN.blit(BUY, (0, 0))
    text = drawtext('BUY ATOMIC POWER PLANT: 100000/-', 20)
    SCREEN.blit(text, (250, 200))

    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 660 < pos[0] < 715 and 190 < pos[1] < 220:

                break

            elif 420 < pos[0] < 540 and 350 < pos[1] < 400:

                a = []
                a = chkavail()

                if a[0] is 1:
                    text1 = drawtext('You have already got one unit', 20)
                    SCREEN.blit(text1, (300, 320))
                else:
                    f = open('../data_files/money.txt', 'r')

                    for line in f:
                        line = line[:-1]

                    f.close()
                    b = int(line)


                    if b > 100000:

                        b -= 100000


                        f = open('../data_files/money.txt', 'w')

                        f.write(str(b)+'\n')



                        text1 = drawtext('You bought one Atomic Power Plant', 20)
                        SCREEN.blit(text1, (300, 300))
                        a[0] = 1

                        f = open('../data_files/availability.txt', 'w')


                        for i in range(12):
                            f.write(str(a[i])+'\n')

                        f.close()

                        pygame.time.delay(200)

                    else:
                        tr = drawtext('You dont have enough money', 20)
                        SCREEN.blit(tr, (300, 320))



        CLOCK.tick(FPS)


def buy_coal():
    BUY = pygame.image.load('../media/images/buy.gif')


    SCREEN.blit(BUY, (0, 0))
    text = drawtext('BUY COAL POWER PLANT: 100000/-', 20)
    SCREEN.blit(text, (250, 200))

    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 660 < pos[0] < 715 and 190 < pos[1] < 220:

                break

            elif 420 < pos[0] < 540 and 350 < pos[1] < 400:

                a = []
                a = chkavail()

                if a[1] is 1:
                    text1 = drawtext('You have already got one unit', 20)
                    SCREEN.blit(text1, (300, 320))
                else:
                    f = open('../data_files/money.txt', 'r')

                    for line in f:
                        line = line[:-1]

                    f.close()
                    b = int(line)


                    if b > 100000:

                        b -= 100000


                        f = open('../data_files/money.txt', 'w')

                        f.write(str(b)+'\n')



                        text1 = drawtext('You bought one Coal Power Plant', 20)
                        SCREEN.blit(text1, (300, 300))
                        a[1] = 1

                        f = open('../data_files/availability.txt', 'w')


                        for i in range(12):
                            f.write(str(a[i])+'\n')

                        f.close()

                        pygame.time.delay(200)

                    else:
                        tr = drawtext('You dont have enough money', 20)
                        SCREEN.blit(tr, (300, 320))

        CLOCK.tick(FPS)


def buy_natural():
    BUY = pygame.image.load('../media/images/buy.gif')


    SCREEN.blit(BUY, (0, 0))
    text = drawtext('BUY NATURAL GAS POWER PLANT: 100000/-', 20)
    SCREEN.blit(text, (250, 200))

    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 660 < pos[0] < 715 and 190 < pos[1] < 220:

                break

            elif 420 < pos[0] < 540 and 350 < pos[1] < 400:

                a = []
                a = chkavail()

                if a[2]+a[3] is 2:
                    text1 = drawtext('You have already got two units', 20)
                    SCREEN.blit(text1, (300, 320))
                else:
                    f = open('../data_files/money.txt', 'r')

                    for line in f:
                        line = line[:-1]

                    f.close()
                    b = int(line)


                    if b > 100000:

                        b -= 100000


                        f = open('../data_files/money.txt', 'w')

                        f.write(str(b)+'\n')



                        text1 = drawtext('You bought one Natural Gas Power Plant', 20)
                        SCREEN.blit(text1, (300, 300))
                        if a[2] is 0:
                            a[2] = 1
                        else:
                            a[3] = 1

                        f = open('../data_files/availability.txt', 'w')


                        for i in range(12):
                            f.write(str(a[i])+'\n')

                        f.close()

                        pygame.time.delay(200)

                    else:
                        tr = drawtext('You dont have enough money', 20)
                        SCREEN.blit(tr, (300, 320))



        CLOCK.tick(FPS)

def buy_solar():
    BUY = pygame.image.load('../media/images/buy.gif')


    SCREEN.blit(BUY, (0, 0))
    text = drawtext('BUY SOLAR POWER PLANT: 100000/-', 20)
    SCREEN.blit(text, (250, 200))

    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 660 < pos[0] < 715 and 190 < pos[1] < 220:

                break

            elif 420 < pos[0] < 540 and 350 < pos[1] < 400:

                a = []
                a = chkavail()

                if a[4]+a[5] is 2:
                    text1 = drawtext('You have already got two units', 20)
                    SCREEN.blit(text1, (300, 320))
                else:
                    f = open('../data_files/money.txt', 'r')

                    for line in f:
                        line = line[:-1]

                    f.close()
                    b = int(line)


                    if b > 100000:

                        b -= 100000


                        f = open('../data_files/money.txt', 'w')

                        f.write(str(b)+'\n')



                        text1 = drawtext('You bought one Solar Power Plant', 20)
                        SCREEN.blit(text1, (300, 300))
                        if a[4] is 0:
                            a[4] = 1
                        else:
                            a[5] = 1

                        f = open('../data_files/availability.txt', 'w')


                        for i in range(12):
                            f.write(str(a[i])+'\n')

                        f.close()

                        pygame.time.delay(200)

                    else:
                        tr = drawtext('You dont have enough money', 20)
                        SCREEN.blit(tr, (300, 320))



        CLOCK.tick(FPS)

def buy_wind():
    BUY = pygame.image.load('../media/images/buy.gif')


    SCREEN.blit(BUY, (0, 0))
    text = drawtext('BUY WIND POWER PLANT: 100000/-', 20)
    SCREEN.blit(text, (250, 200))

    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 660 < pos[0] < 715 and 190 < pos[1] < 220:

                break

            elif 420 < pos[0] < 540 and 350 < pos[1] < 400:

                a = []
                a = chkavail()

                if a[6]+a[7] is 2:
                    text1 = drawtext('You have already got two units', 20)
                    SCREEN.blit(text1, (300, 320))
                else:
                    f = open('../data_files/money.txt', 'r')

                    for line in f:
                        line = line[:-1]

                    f.close()
                    b = int(line)


                    if b > 100000:

                        b -= 100000


                        f = open('../data_files/money.txt', 'w')

                        f.write(str(b)+'\n')



                        text1 = drawtext('You bought one Wind Power Plant', 20)
                        SCREEN.blit(text1, (300, 300))
                        if a[6] is 0:
                            a[6] = 1
                        else:
                            a[7] = 1

                        f = open('../data_files/availability.txt', 'w')


                        for i in range(12):
                            f.write(str(a[i])+'\n')

                        f.close()

                        pygame.time.delay(200)

                    else:
                        tr = drawtext('You dont have enough money', 20)
                        SCREEN.blit(tr, (300, 320))


        CLOCK.tick(FPS)

def buy_hydro():
    BUY = pygame.image.load('../media/images/buy.gif')


    SCREEN.blit(BUY, (0, 0))
    text = drawtext('BUY HYDROELECTRIC POWER PLANT: 100000/-', 20)
    SCREEN.blit(text, (250, 200))

    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 660 < pos[0] < 715 and 190 < pos[1] < 220:

                break

            elif 420 < pos[0] < 540 and 350 < pos[1] < 400:

                a = []
                a = chkavail()

                if a[8]+a[9] is 2:
                    text1 = drawtext('You have already got two units', 20)
                    SCREEN.blit(text1, (300, 320))
                else:
                    f = open('../data_files/money.txt', 'r')

                    for line in f:
                        line = line[:-1]

                    f.close()
                    b = int(line)


                    if b > 100000:

                        b -= 100000


                        f = open('../data_files/money.txt', 'w')

                        f.write(str(b)+'\n')



                        text1 = drawtext('You bought one Hydroelectric Power Plant', 20)
                        SCREEN.blit(text1, (300, 300))
                        if a[8] is 0:
                            a[8] = 1
                        else:
                            a[9] = 1

                        f = open('../data_files/availability.txt', 'w')


                        for i in range(12):
                            f.write(str(a[i])+'\n')

                        f.close()

                        pygame.time.delay(200)

                    else:
                        tr = drawtext('You dont have enough money', 20)
                        SCREEN.blit(tr, (300, 320))




        CLOCK.tick(FPS)

def buy_geothermal():

    BUY = pygame.image.load('../media/images/buy.gif')


    SCREEN.blit(BUY, (0, 0))
    text = drawtext('BUY GEOTHERMAL POWER PLANT: 100000/-', 20)
    SCREEN.blit(text, (250, 200))

    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 660 < pos[0] < 715 and 190 < pos[1] < 220:

                break

            elif 420 < pos[0] < 540 and 350 < pos[1] < 400:

                a = []
                a = chkavail()

                if a[10]+a[11] is 2:
                    text1 = drawtext('You have already got two units', 20)
                    SCREEN.blit(text1, (300, 320))
                else:

                    f = open('../data_files/money.txt', 'r')

                    for line in f:
                        line = line[:-1]

                    f.close()
                    b = int(line)


                    if b > 100000:

                        b -= 100000


                        f = open('../data_files/money.txt', 'w')

                        f.write(str(b)+'\n')



                        text1 = drawtext('You bought one Geothermal Power Plant', 20)
                        SCREEN.blit(text1, (300, 300))
                        if a[10] is 0:
                            a[10] = 1
                        else:
                            a[11] = 1

                        f = open('../data_files/availability.txt', 'w')


                        for i in range(12):
                            f.write(str(a[i])+'\n')

                        f.close()

                        pygame.time.delay(200)

                    else:
                        tr = drawtext('You dont have enough money', 20)
                        SCREEN.blit(tr, (300, 320))



        CLOCK.tick(FPS)




