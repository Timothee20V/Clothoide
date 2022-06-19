import pygame
import pytmx
import pyscroll
'''utilisation de pygame pour la fenêtre 
utilisation de pytmx et pyscroll pour lire des fichier tmx pour le background 
'''
from test_graphique.Road import road
#retirer: from test_graphique.Voiture import Car
from test_graphique.camera import camera
from test_graphique.flag import flag


class Game:

    def __init__(self):
        '''fenetre du jeu'''
        pygame.display.set_caption("Construction de routes")
        self.screen = pygame.display.set_mode((800, 800))

        '''charger la carte (tmx)'''
        tmx_data = pytmx.util_pygame.load_pygame('assets/image/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 1

        '''generer une voiture'''
        #retirer : self.car = Car(30, 40)
        '''generer la position de la camera'''
        self.camera = camera(250, 250)
        '''initialiser la route'''
        self.road = road()

        '''liste rectangle de delimitation pour le collision en mode zoom'''
        self.walls =[]

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x,obj.y , obj.width, obj.height))

        '''groupe de layer de la carte'''
        self.group = pyscroll.PyscrollGroup(map_layer= self.map_layer, default_layer=3)
        #retirer : self.group.add(self.car)
        self.group.add(self.camera)

    def handle_imput(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            '''deplacement haut'''
            self.camera.move_up()
        elif pressed[pygame.K_s]:
            '''deplacement bas'''
            self.camera.move_down()
        elif pressed[pygame.K_q]:
            '''deplacement gauche'''
            self.camera.move_left()
        elif pressed[pygame.K_d]:
            '''deplacement droite'''
            self.camera.move_right()
        elif pygame.mouse.get_pressed()[0] and self.map_layer.zoom == 1:
            '''placement des drapeau par click droit de la souris'''
            x, y = pygame.mouse.get_pos()
            '''enregitrement des coordonnées des drapeaux pour point de passage de la route'''
            self.road.left_click(x, y)
            drapeau = flag(x, y)
            self.group.add(drapeau)
            pygame.time.wait(100)
        elif pressed[pygame.K_KP_MINUS]:
            '''dezoom de la carte'''
            self.map_layer.zoom = 1
        elif pressed[pygame.K_KP_PLUS]:
            '''zoom de la carte'''
            self.map_layer.zoom = 2

    def update(self):
        self.group.update()

        '''detection de collision '''
        for sprite in self.group.sprites():
            if sprite.hitbox.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        '''orloge'''
        clock = pygame.time.Clock()

        '''variable d'execution'''
        running = True

        '''boucle principale du jeu:'''
        while running:
            '''enregistre la dernière location de la camera'''
            self.camera.save_location()
            '''vérifient  les touche presser du clavier'''
            self.handle_imput()
            '''mettre à jour le groupe de calque'''
            self.update()
            '''centrer sur la camera'''
            self.group.center(self.camera.rect)
            '''mettre à jour l'ecran'''
            self.group.draw(self.screen)
            pygame.display.flip()
            '''si on ferme la fenetre'''
            for event in pygame.event.get():
                '''si on clic sur la croix de fermeture'''
                if event.type == pygame.QUIT:
                    running = False

            '''limitation à 60 frame par seconde'''
            clock.tick(60)

        pygame.quit()
