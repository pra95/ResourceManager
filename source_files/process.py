import pygame
from close import asktoquit


def process():
    i = 0
    for event in pygame.event.get():

        if event.type is pygame.QUIT:
            i = asktoquit()
            if i is 1:
                pygame.quit()
                exit()