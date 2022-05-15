import pygame

from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100  # point de vie actuel
        self.max_health = 100  # point de vie maximum
        self.attack = 10  # point d'attaque
        self.velocity = 5  # vitesse
        self.image = pygame.image.load("assets/player.png")  # image du joueur
        self.rect = self.image.get_rect()  # rectangle qui prend le contour d'un joueur
        self.rect.x = 400  # positionner le joueur à l'horizontale
        self.rect.y = 500  # positionner le joueur à la verticale
        self.projectiles = pygame.sprite.Group()

    def move_right(self):
        if not self.game.check_collision(self, self.game.monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        self.projectiles.add(Projectile(self))

    def update_health_bar(self, surface):
        # désiner la barre de vie total
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        # désiner la barre de vie acutel
        pygame.draw.rect(surface, (0, 102, 0), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def damage(self, amount):  # dégat subit sur le joueur
        # si les dégats sont inférieur ou = a 0, le joueur est décédé
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()
