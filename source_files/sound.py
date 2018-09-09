import pygame
from process import process

pygame.init()

CLOCK = pygame.time.Clock()

FPS = 24
SCREEN = pygame.display.set_mode((960, 640))


def sound():

    SOUNDMENU = pygame.image.load('../media/images/soundmenu.jpg')

    SCREEN.blit(SOUNDMENU, (0, 0))


    i = 0
    while True:

        process()
        pygame.display.update()

        clicked = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if clicked[0] is 1:

            if 875 < pos[0] < 917 and 25 < pos[1] < 54:
                print('1')
                break

            elif 360 < pos[0] < 600 and 175 < pos[1] < 230:
                print('1')
                pygame.mixer.music.play(-1)

            elif 360 < pos[0] < 600 and 270 < pos[1] < 320:
                print('1')
                pygame.mixer.music.pause()


        CLOCK.tick(FPS)

