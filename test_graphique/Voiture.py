import pygame
'''class voiture qui à été abandonnée en raison de rotation qui desintegre l'image de la voiture'''

class Car(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/image/voiture_sprite.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([255, 255, 255])  # enleve la couleur blanche de l'image
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.old_position = self.position.copy()
        self.position = [x, y]

    def update(self):
        self.rect.center = self.position

    def rotation(self, angle):
        self.image = pygame.transform.rotozoom(self.image, angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def get_image(self, x, y):
        image = pygame.Surface([31, 43])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 31, 43))
        return image
