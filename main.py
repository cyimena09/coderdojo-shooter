import pygame as pygame
import math
from game import Game

# 1.chargement des éléments nécessaire pour faire fonctionner pygame
pygame.init()

# 2. Créer la fenetre du jeu (titre et taille, fond d'écran)
pygame.display.set_caption("Coder dojo Shooter")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("assets/bg.jpg")

# charger la bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))  # redimensionner l'image
banner_rect = banner.get_rect()  # positionner l'image
banner_rect.x = math.ceil(screen.get_width() / 4)  # positionner en x

# charger le bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()  # positionner l'image
play_button_rect.x = math.ceil(screen.get_width() / 3.33)  # positionner en x
play_button_rect.y = math.ceil(screen.get_height() / 2)  # positionner en y

# 3. charger le jeu
game = Game()

# 4. On fait tourner le jeu indéfiniment
while True:
    # Appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))

    # si le jeu a démarré
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    # si le jeu n'a pas commencé
    else:
        # ajouter écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():

        # Si le joueur décide de fermer le jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # détecter si le joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # lancer un projectile si la barre espace est appuyée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # vérifier si on a cliqué sur le bouton
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # on récupère le rectangle du boutton et on vérifie si la souris est dessus
            if play_button_rect.collidepoint(event.pos):
                # on lance le jeu
                game.start()
