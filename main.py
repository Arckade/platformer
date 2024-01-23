import pygame
import sys
from block_platform import BlockPlatform
from player import Player
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pong")

# Set up colors
black = (0, 0, 0)
blue = (0, 0, 255)

# Main game loop
dir_x = 0
dir_y = 0
speed = 0.1
# piattaforme
block_w, block_h = 70, 50
off_screen = width // 2
griglia = [1, 1, 3, 0, 1, 1, 1, 1, 3, 3, 5, 5, 3, 3, 3, 5, 5, 3, 3, 3, 4, 3, 0, 1, 1, 1, 1, 2, 3, 5, 5, 3, 3, 3, 5, 5,
           3, 3]
altezza_griglia = (height // 20)


def restart():
    erbe_ = []
    terre_ = []
    for i in range(len(griglia)):  # i =0, 1, 2, ...
        if griglia[i] == 0:
            continue
        indice_griglia = 20 - griglia[i]

        y = indice_griglia * altezza_griglia
        block = BlockPlatform("assets/Platform.png", block_w, 20, off_screen + block_w * i, y)
        erbe_.append(block)
        y += block.rect.height

        for j in range(griglia[i] - 1, 0, -1):
            block = BlockPlatform("assets/Platform-terra.png", block_w, 20, off_screen + block_w * i, y)
            terre_.append(block)
            y += block.rect.height
    return erbe_, terre_


# player
player = Player("assets/Platform.png", 20, 20, width // 2, height // 2)

v_x, v_y = -1, -2

erbe_, terre_ = restart()
erbe = pygame.sprite.Group(*erbe_)
terre = pygame.sprite.Group(*terre_)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # and not player.jump:
                # Se il giocatore non è già in salto, applica la forza verso l'alto
                player.velocity_y = -15
                player.jump = True

    # movimento blocchi
    for sprite in erbe.sprites():
        sprite.rect.x += v_x
    for sprite in terre.sprites():
        sprite.rect.x += v_x

    # Check for collisions
    erbe_hit = pygame.sprite.spritecollide(player, erbe, False)
    terre_hit = pygame.sprite.spritecollide(player, terre, False)
    if terre_hit:
        erbe_, terre_ = restart()
        erbe = pygame.sprite.Group(*erbe_)
        terre = pygame.sprite.Group(*terre_)

    # movimento player
    player.update(height, erbe_hit[0] if len(erbe_hit) > 0 else None)

    # Draw to the screen
    screen.fill(black)
    for sprite in erbe.sprites():
        screen.blit(sprite.image, sprite.rect)

    for sprite in terre.sprites():
        screen.blit(sprite.image, sprite.rect)

    screen.blit(player.image, player.rect)
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
