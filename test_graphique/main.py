import pygame
pygame.init()

#fenetre du jeu

pygame.display.set_caption("Chemin de fer")
screen = pygame.display.set_mode((800, 600))

#importer l'arriere plan
background = pygame.image.load('assets/image/Cartoon_green_texture_grass.jpg')
#rescale de l'image
background = pygame.transform.scale(background, (850, 600))

#variable d'execution
running = True

#boucle principale du jeu:
while running:

    #arriere plan du jeu
    screen.blit(background, (0,0))

    #mettre à jour l'ecran
    pygame.display.flip()

    #si on ferme la fenetre
    for event in pygame.event.get(): 
        #si on clic sur la croix de fermeture
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

































#mention graphiste: BZZRINCANTATION ,babysofja