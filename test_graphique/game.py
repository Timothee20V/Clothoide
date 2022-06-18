import pygame
import pytmx
import pyscroll

from test_graphique.Voiture import Car
from test_graphique.camera import camera

class Game:

    def __init__(self):
        #fenetre du jeu
        pygame.display.set_caption("Construction de routes")
        self.screen = pygame.display.set_mode((800, 600))

        #charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('assets/image/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        #generer une voiture
        self.car = Car(30,40)

        self.camera = camera(250,250)

        #groupe de layer de la carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.car)
        self.group.add(self.camera)

    def handle_imput(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            #haut
            self.camera.move_up()
        elif pressed[pygame.K_s]:
            #bas
            self.camera.move_down()
        elif pressed[pygame.K_q]:
            #gauche
            self.camera.move_left()
        elif pressed[pygame.K_d]:
            #droite
            self.camera.move_right()
        elif pressed[pygame.K_r]:
            self.car.rotation(3, self.screen)



    def run(self):

        clock = pygame.time.Clock()

        #boucle principale du jeu:

        # variable d'execution
        running = True

        while running:

            #check les touche presser du clavier
            self.handle_imput()
            #mettre à jour le groupe de calque
            self.group.update()
            #centrer sur la camera
            self.group.center(self.camera.rect)
            #mettre à jour l'ecran
            self.group.draw(self.screen)
            pygame.display.flip()
            #si on ferme la fenetre
            for event in pygame.event.get():
                #si on clic sur la croix de fermeture
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()