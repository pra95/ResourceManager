import pygame


def process():
    for event in pygame.event.get():

        if event.type is pygame.QUIT:
                pygame.quit()
                exit()