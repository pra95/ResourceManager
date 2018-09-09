import pygame
from textinput import drawtext
from process import process
from starting import starts

pygame.init()

NEWSCREEN = pygame.display.set_mode((960, 640))

NEWWINDOW = pygame.image.load('../media/images/background2.gif')

CLOCK = pygame.time.Clock()

def pressed_atomic():

    print("you clicked atomic")

    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('ATOMIC POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(12)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/atomic.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_coal():

    print("you clcicked coal")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('COAL POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(10)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/coal.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_natural1():

    print("you pressed natural")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('NATURAL GAS POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(8)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/natural.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_natural2():

    print("you pressed natural")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('NATURAL GAS POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(8)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/natural.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_solar1():

    print("you clciked solar")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('SOLAR POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(6)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/solar.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_solar2():

    print("you clciked solar")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('SOLAR POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(6)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/solar.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_wind1():

    print("you clciked wind")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('WIND POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(6)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/wind.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_wind2():

    print("you clciked wind")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('WIND POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(4)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/wind.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_hydro1():

    print("you clciked hydroelecric")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('HYDROELECTRIC POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(2)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/hydro.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_hydro2():

    print("you clciked hydroelecric")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('HYDROELECTRIC POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(4)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/hydro.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')


def pressed_geothermal1():

    print("you clciked geothermal")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('GEOTHERMAL POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(2)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/geo.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')

def pressed_geothermal2():

    print("you clciked geothermal")
    i = 0

    NEWSCREEN.blit(NEWWINDOW, (0, 0))


    text = drawtext('GEOTHERMAL POWER PLANT', 26)
    start = drawtext('START', 20)
    stop = drawtext('STOP', 20)
    resources = drawtext('RESOURCES', 20)
    one = drawtext('Remaining Resources:', 20)
    two = drawtext('Production Per Hour:', 20)
    three = drawtext('Total Production:', 20)
    four = drawtext('Profit Earned:', 20)
    five = drawtext('Total Pollution:', 20)

    NEWSCREEN.blit(text, (300, 120))
    NEWSCREEN.blit(start, (200, 470))
    NEWSCREEN.blit(stop, (400, 470))
    NEWSCREEN.blit(resources, (600, 470))
    NEWSCREEN.blit(one, (250, 200))
    NEWSCREEN.blit(two, (250, 220))
    NEWSCREEN.blit(three, (250, 240))
    NEWSCREEN.blit(four, (250, 260))
    NEWSCREEN.blit(five, (250, 280))


    while True:

        process()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0] is 1:

            if pos[0] > 740 and pos[0] < 780 and pos[1] > 120 and pos[1] < 160:

                break

            elif pos[0] > 190 and pos[0] < 370 and pos[1] > 460 and pos[1] < 500:

                t1 = drawtext('The production has started', 20)
                NEWSCREEN.blit(t1, (350, 400))
                starts(4)
                print('pressed start')


            elif pos[0] > 390 and pos[0] < 570 and pos[1] > 460 and pos[1] < 500:
                t2 = drawtext('The production has stopped', 20)
                NEWSCREEN.blit(t2, (350, 430))

                print('pressed stop')

            elif pos[0] > 590 and pos[0] < 770 and pos[1] > 460 and pos[1] < 500:
                t3 = drawtext('The resources remained are: 20%', 20)
                NEWSCREEN.blit(t3, (350, 370))

                print('presses resources')


        # outputting from the file
        f = open('../data_files/geo.txt', 'r')
        t = 0
        for line in f:
            line = line[:-1]
            text = drawtext(line, 20)
            NEWSCREEN.blit(text, (450, 200 + t))
            t += 20




        pygame.display.update()

        CLOCK.tick(24)

    f.close()




    print('got out of the while loop')



