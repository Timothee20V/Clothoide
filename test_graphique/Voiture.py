import pygame
import pytmx
import pyscroll

class Car(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/image/voiture_sprite.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([255,255,255]) #enleve la couleur blanche de l'image
        self.rect = self.image.get_rect()
        self.position = [x,y]

    def update(self):
        self.rect.center = self.position

    def rotation(self,angle,screen):
        originPos = [31/2, 43/2]
        #calcule de la boite alligné au bord de l'image en rotation
        box = [pygame.math.Vector2(p) for p in [(0, 0), (originPos[0], 0), (originPos[0], -originPos[1]), (0, -originPos[1])]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        #calcule de la translation du pivot
        pivot = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot
        #calcule de l'origine "en haut à gauche" de l'image en rotation
        origin = (self.position[0] - originPos[0] + min_box[0] - pivot_move[0], self.position[1] - originPos[1] - max_box[1] + pivot_move[1])
        #rotation de l'image
        self.image = pygame.transform.rotate(self.image, angle)
        screen.blit(self.image, self.position)

    def get_image(self,x,y):
        image = pygame.Surface([31,43])
        image.blit(self.sprite_sheet, (0,0), (x,y ,31, 43))
        return image