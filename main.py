import pygame as pygame
import math
from game import Game

# 1. Chargement des éléments nécessaire pour faire fonctionner pygame
pygame.init()

# 2. Créer la fenetre du jeu (titre et taille, fond d'écran)
pygame.display.set_caption("Coder dojo Shooter")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("assets/bg.jpg")

# 3. Charger la bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))  # redimensionner l'image
banner_rect = banner.get_rect()  # positionner l'image
banner_rect.x = math.ceil(screen.get_width() / 4)  # positionner en x

# 4. Charger le bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()  # positionner l'image
play_button_rect.x = math.ceil(screen.get_width() / 3.33)  # positionner en x
play_button_rect.y = math.ceil(screen.get_height() / 2)  # positionner en y

# 5. Charger le jeu
game = Game()

# 6. On fait tourner le jeu indéfiniment. Chaque boucle correspond à un instant du jeu
while True:
    # 6.1. Appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))

    # 6.2. Si le jeu a démarré, mettre à jour les éléments et les instructions du jeu
    if game.is_playing:
        game.update(screen)

    # 6.3. Si le jeu n'a pas commencé, afficher l'écran de bienvenue
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # 6.4. Ecoute des évenements du clavier. Le joueur a avance, recule ? etc.
    for event in pygame.event.get():
        # 6.4.1. Si le joueur décide de fermer le jeu
        if event.type == pygame.QUIT:
            pygame.quit()

        # 6.4.2. Détecter si le joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # 6.4.2.1. Lancer un projectile si la barre espace est appuyée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        # 6.4.3. Si le joueur à relacher une touche
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # 6.4.4. Vérifier si on a cliqué sur le bouton
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # on récupère le rectangle du boutton et on vérifie si la souris est dessus
            if play_button_rect.collidepoint(event.pos):
                game.start()  # on lance le jeu

    pygame.display.flip()  # mettre à jour l'affichage graphique
