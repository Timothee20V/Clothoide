import pygame
import pytmx
import pyscroll

from test_graphique.Voiture import Car


class Game:

    def __init__(self):
        #fenetre du jeu
        pygame.display.set_caption("Chemin de fer")
        self.screen = pygame.display.set_mode((800, 600))

        #charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('assets/image/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        #generer une voiture
        self.car = Car()

        #groupe de layer de la carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.car)

    def run(self):
        #boucle principale du jeu:

        # variable d'execution
        running = True

        while running:

            #mettre à jour l'ecran
            self.group.draw(self.screen)
            pygame.display.flip()
            #si on ferme la fenetre
            for event in pygame.event.get():
                #si on clic sur la croix de fermeture
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()