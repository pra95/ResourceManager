import pygame
import pygame.font

pygame.init()

SCREEN = pygame.display.set_mode((960, 640))

IMG = pygame.image.load('atomic_power_plant1.gif')

SCREEN.blit(IMG, (20, 20))
pygame.font.Font.render('prashant degaonkar', (20, 240, 10))


while True:

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            exit()



    print(pygame.mouse.get_pos())
    pygame.display.flip()



pygame.quit()
exit()