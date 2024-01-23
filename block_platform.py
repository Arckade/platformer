import pygame
from random import randint


class BlockPlatform(pygame.sprite.Sprite):
    def __init__(self, asset, w, h, x, y):
        super().__init__()
        self.image = pygame.image.load(asset)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.velocity = [0, 0]
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.move_ip(*self.velocity)
