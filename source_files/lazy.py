import pygame

pygame.init()

# variables

FPS = 24


clock = pygame.time.Clock()

screen = pygame.display.set_mode((960, 640), 0, 32)

background = pygame.image.load('background.png')

new_window = pygame.image.load("me.jpg").convert(background)

player = pygame.image.load('ball.png').convert(background)

position = player.get_rect()

screen.blit(background, (0, 0))


while True:

    screen = pygame.display.set_mode((960, 640), 0, 32)
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        if event.type is pygame.QUIT:
            pygame.quit()
            exit()


        if keys[pygame.K_n] is 1:
            # create a new screen
            print("n was pressed")
            flag = 0
            screen1 = pygame.display.set_mode((640, 360))
            while True:


                print("inside the loop")

                for event in pygame.event.get():
                    keyss = pygame.key.get_pressed()

                    if keyss[pygame.K_x] is 1:
                        print("x is pressed")
                        flag = 1
                        break

                if flag is 1:
                    break

                pygame.display.update()

    pygame.display.flip()

    screen.blit(background, position, position)

    screen.blit(player, position)

    clock.tick(FPS)


pygame.quit()
exit()
