import random

import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100  # vitesse du projectile
        self.attack = 0.3
        self.image = pygame.image.load("assets/mummy.png")  # image du projectile
        self.rect = self.image.get_rect()  # rectangle qui prend le contour du monstre
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 545
        self.velocity = random.randint(1, 3)

    def forward(self):
        if not self.game.check_collision(self, self.game.players):
            self.rect.x -= self.velocity

        # si le monstre ne se déplace pas, c'est qu'il inflige des dégats au joueur
        else:
            self.game.player.damage(self.attack)

    def damage(self, amount):  # dégat subit sur le monstre
        self.health -= amount

        # les points de vie sont en dessous de 0, alors le monstre est mort
        if self.health <= 0:
            # réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = 100

    def update_health_bar(self, surface):
        # désiner la barre de vie total du monstre
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        # désiner la barre de vie acutel du monstre
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
