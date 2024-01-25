import pygame
from random import randint


class BlockPlatform(pygame.sprite.Sprite):
    def __init__(self, asset, w, h, x, y):
        super().__init__()
        # Set up colors
        black = (0, 0, 0)
        red = (255, 0, 0)
        # self.image = pygame.image.load(asset)
        # self.image = pygame.transform.scale(self.image, (w, h))
        self.image = pygame.Surface((w, h))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect()
        self.velocity = [0, 0]
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.move_ip(*self.velocity)
