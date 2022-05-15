import pygame

from monster import Monster
from player import Player


class Game:

    def __init__(self):
        self.is_playing = False
        self.players = pygame.sprite.Group()
        self.player = Player(self)  # charger le joueur dans le jeu
        self.players.add(self.player)
        self.monsters = pygame.sprite.Group()  # groupe de monstre
        self.pressed = {}  # contient toutes les touches qui sont appuyées

    def start(self):
        self.is_playing = True
        self.spawn_monster()  # charger un monstre au démarrage du jeu
        self.spawn_monster()

    def spawn_monster(self):
        self.monsters.add(Monster(self))  # charger le monstre dans le jeu

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        self.is_playing = False
        # retirer les monstres, reset la barre de vie du monstre et afficher le menu du jeu
        self.monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image du joueur au coordonnées indiqué en second paramètre
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        # récupérer les projectiles et les faire se déplacer
        for projectile in self.player.projectiles:
            projectile.move()

        # récupérer les monstres et les faire se déplacer
        for monster in self.monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer les images du groupe de projectile sur l'écran
        self.player.projectiles.draw(screen)

        # appliquer les images du groupe de monstres sur l'écran
        self.monsters.draw(screen)

        # vérifier si le joueur souahite aller à droite ou à gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
