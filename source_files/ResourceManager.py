import pygame

pygame.init()

SCREEN = pygame.display.set_mode((960, 640), 0 ,32)

BACKGROUND = pygame.image.load('background.png')

SCREEN.blit(BACKGROUND, (0, 0))

NEW_BACK = pygame.image.load('new_window.png').convert_alpha(BACKGROUND)

while True:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            exit()

        if keys[pygame.K_n] is 1:
            SCREEN.blit(NEW_BACK, (0, 0))

        if keys[pygame.K_x] is 1:
            SCREEN.blit(BACKGROUND, (0, 0))


    pygame.display.flip()



pygame.quit()
exit()