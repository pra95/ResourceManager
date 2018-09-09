import pygame

pygame.init()


def drawtext(string, size, clr=(0, 0, 0)):

    return pygame.font.Font('C:\Python34\Lib\site-packages\pygame\examples\data\sans.ttf', size).render(string, 0, clr)

