import pygame
'''utilisation des bibliothèques pygame , pytmx , pyscroll 
insatlation avec la commande: pip install 'nom de la bibliothèque'
'''
from game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()


'''credit des images moi même'''