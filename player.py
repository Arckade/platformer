import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, asset, w, h, x, y):
        super().__init__()
        self.image = pygame.image.load(asset)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.velocity_y = 0
        self.rect.x, self.rect.y = x, y
        self.jump = False

    def update(self, height, sprite):
        if sprite:
            height = sprite.rect.y
        # Applica la gravità
        self.velocity_y += 1

        # Applica la velocità in verticale
        self.rect.y += self.velocity_y

        # Impedisce allo sprite di oltrepassare il blocco corrente
        if self.rect.y > height - self.rect.height:
            self.rect.y = height - self.rect.height
            self.velocity_y = 0
            self.jump = False
