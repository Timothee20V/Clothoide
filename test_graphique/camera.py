import pygame


class camera(pygame.sprite.Sprite):

    '''initialise les veraible de la class camera, prend l'image de la camera et la rend invisible '''
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

    '''enregistre la dernière location de la camera '''
    def save_location(self): self.old_position = self.position.copy()

    '''deplacment de la camera à droite'''
    def move_right(self): self.position[0] += self.speed

    '''deplacment de la camera à gauche'''
    def move_left(self): self.position[0] -= self.speed

    '''deplacment de la camera en haut'''
    def move_up(self): self.position[1] -= self.speed

    '''deplacment de la camera en bas'''
    def move_down(self): self.position[1] += self.speed

    '''fonction de rafraichisent de la position de la camera et de sa hitbox'''
    def update(self):
        self.rect.topleft = self.position
        self.hitbox.center = self.rect.center

    '''retour en arriere de la position de la camera utilie lorsque la hitbox de la camera pietine celle d'un mur'''
    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.hitbox.center = self.rect.center

    '''retourne l'image pris du png en dossier et definit sa surface'''
    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0), (x,y ,32 , 32))
        return image

    '''retourne la position de la camera'''
    def get_position(self):
        return self.position