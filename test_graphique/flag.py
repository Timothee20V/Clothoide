import pygame

'''class flag qui sert à indiquer ou l'utilisateur à placer les points de sa route
definit de la même maniere que la camera sauf que le drapeau n'est pas invisible et ne se deplace pas
'''


class flag(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/image/flag.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([255, 255, 255])  # enleve la couleur blanche de l'image
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.position = [x, y]
        self.old_position = self.position.copy()

    def update(self):
        self.rect.center = self.position

    def move_back(self):
        self.position = self.old_position
        self.rect.center = self.position
        self.hitbox.center = self.rect.center

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 16))
        return image
