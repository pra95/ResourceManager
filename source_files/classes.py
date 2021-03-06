import pygame

class BaseClass(pygame.sprite.Sprite):
    allsprites = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):


        pygame.sprite.Sprite.__init__(self)

        BaseClass.allsprites.add(self)

        self.image = pygame.image.load('../media/images/' + image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

class Bug(BaseClass):

    List = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):

        BaseClass.__init__(self, x, y, width, height, image_string)
        Bug.List.add(self)
        self.velx = 3

    def motion(self):

        self.rect.x += self.velx

        if self.rect.x > 920 or self.rect.x < 0:
            self.velx = -self.velx
