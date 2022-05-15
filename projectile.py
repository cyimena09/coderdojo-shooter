import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 5  # vitesse du projectile
        self.image = pygame.image.load("assets/projectile.png")  # image du projectile
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()  # rectangle qui prend le contour du projectile
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image  # garder l'image originel sans la rotation pour éviter de la perdre pdt la modif
        self.angle = 0

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # supprimer le projectile s'il est entré en collision avec le monstre
        for monster in self.player.game.check_collision(self, self.player.game.monsters):
            self.remove()
            monster.damage(self.player.attack)

        # si le projectile n'est plus visible a l'écran, on le supprime du groupe de projectile
        if self.rect.x > 1080:
            self.remove()

    def remove(self):
        self.player.projectiles.remove(self)

    def rotate(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
