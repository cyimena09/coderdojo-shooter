import pygame

# 1. générer la fenetre
from game import Game
from player import Player

pygame.display.set_caption("Coder dojo Shooter")  # titre de la fenetre
screen = pygame.display.set_mode((1080, 720))  # taille de la fenetre
background = pygame.image.load("assets/bg.jpg")  # fond d'écran de la fenetre

# générer le jeu et le joueur
game = Game()
player = game.player

# 2. Le while True permet de garder la fenetre ouverte
while True:
    screen.blit(background, (0, -200))
    game.update(screen)

    # Détecter les touches sur le clavier ou la souris
    for event in pygame.event.get():

        # 1.1. Si on a appuyé sur la croix
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Le joueur a quitté le jeu")

        # 1.2. Si une touche du clavier a été appuyé
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True # faire une action sans devoir appuyer plusieurs fois sur la touche
            print("Le joueur a appuyé sur une touche")
            print(event.key)

            # Si le joueur a appuyé sur la touche A
            if event.key == pygame.K_a:
                print("On fait l'action A")
                game.player.move_right()
            elif event.key == pygame.K_b:
                print("On fait l'action B")

            # ....

        # 1.3. Si une touche du clavier a été relaché
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False # permet d'arreter une action lorsque la touche est relachée
            print("Le joueur a relaché une touche")
            print(event.key)

    pygame.display.flip()
