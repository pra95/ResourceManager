import pygame


pygame.init()

CLOCK = pygame.time.Clock()

FPS = 24
SCREEN = pygame.display.set_mode((960, 640))


def gamestart():

    STARTWINDOW = pygame.image.load('../media/images/startimage.jpg')

    i, k = 0, 0
    while True:

        SCREEN.blit(STARTWINDOW, (0, 0))
        pygame.draw.rect(SCREEN, (0, 0, 0), (330, 500, 300, 20), 2)

        pygame.draw.rect(SCREEN, (0, 0, 0), (330, 510, k, 0), 20)
        pygame.display.update()
        if k < 301:
            k += 1



        i += 1
        if i > 320:
            break

