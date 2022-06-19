import pygame


class flag(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/image/flag.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([255, 255, 255])  # enleve la couleur blanche de l'image
        self.rect = self.image.get_rect()
        self.position = [x, y]

    def update(self):
        self.rect.center = self.position

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 16))
        return image
