import pygame
from classes import *
from click import click
from process import process
from textinput import drawtext
from mainmenu import mainmenu
from source_files.gamestart import gamestart
from available import chkavail


pygame.init()
WIDTH = 960
HEIGHT = 640
FPS = 24

CLOCK = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)








text = drawtext('PRODUCTION GROUND', 32)

BACKGROUND = pygame.image.load('../media/images/main_back.png')


# music module

pygame.mixer.music.load('../media/music/bensound-slowmotion.mp3')

pygame.mixer.music.play(-1)
# game start module
gamestart()

# MAIN MENU
mainmenu()

while True:


    process()
    click()

    SCREEN.blit(BACKGROUND, (0, 0))

    SCREEN.blit(text, (260, 20))

    # file usage
    f = open('../data_files/money.txt', 'r')
    for line in f:
        line = line[:-1]

    a = int(line)
    a += 1


    f1 = open('../data_files/money.txt', 'w')

    f1.write(str(a)+'\n')

    t1 = drawtext(str(a), 16)
    SCREEN.blit(t1, (830, 25))

    # power plant availability
    arr = []
    arr = chkavail()

    if arr[0] is 1:
        bug = Bug(228, 121, 40, 40, 'atomic_power_plant1.gif')

    if arr[1] is 1:
        bug1 = Bug(332, 202, 40, 40, 'coal_power_plant.gif')

    if arr[2] is 1:
        bug2 = Bug(454, 132, 40, 40, 'natural_gas_power_plant.gif')

    if arr[3] is 1:
        bug3 = Bug(226, 267, 40, 40, 'natural_gas_power_plant.gif')

    if arr[4] is 1:
        bug4 = Bug(533, 240, 40, 40, 'solar_power_plant.gif')

    if arr[5] is 1:
        bug5 = Bug(400, 326, 40, 40, 'solar_power_plant.gif')

    if arr[6] is 1:
        bug6 = Bug(730, 237, 40, 40, 'wind_power_plant.gif')

    if arr[7] is 1:
        bug7 = Bug(425, 450, 40, 40, 'wind_power_plant.gif')

    if arr[8] is 1:
        bug8 = Bug(590, 340, 40, 40, 'hydroelectric_power_plant.gif')

    if arr[9] is 1:
        bug9 = Bug(25, 105, 40, 40, 'hydroelectric_power_plant.gif')

    if arr[10] is 1:
        bug10 = Bug(348, 43, 40, 40, 'geothermal_power_plant.gif')

    if arr[11] is 1:
        bug11 = Bug(85, 193, 40, 40, 'geothermal_power_plant.gif')




    BaseClass.allsprites.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(FPS)



pygame.quit()
