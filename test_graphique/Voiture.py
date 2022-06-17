import pygame
import pytmx
import pyscroll

class Car(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/image/voiture_sprite.png')
        self.image = self.get_image(0,0)
        self.rect = self.image.get_rect()

    def get_image(self,x,y):
        image = pygame.surface((31,43))
        image.blit(self.sprite_sheet, (0,0), (x,y ,31 , 43))