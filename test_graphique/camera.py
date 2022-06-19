import pygame
import pytmx
import pyscroll


class camera(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/image/camera_invisible.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([255, 255, 255])  # enleve la couleur blanche de l'image
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.hitbox = pygame.Rect(0,0,self.rect.width,self.rect.height)
        self.old_position = self.position.copy()
        self.speed = 3

    def save_location(self): self.old_position = self.position.copy()

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def move_up(self): self.position[1] -= self.speed

    def move_down(self): self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.hitbox.center = self.rect.center

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.hitbox.center = self.rect.center

    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0), (x,y ,32 , 32))
        return image

    def get_position(self):
        return self.position