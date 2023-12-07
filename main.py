import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from tile import Tile
from map import Map

pygame.init()
pygame.display.set_caption('Maow')
screen = pygame.display.set_mode([750, 1000])
clock = pygame.time.Clock()

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
tile = Tile('grass-tile.png')
test_map = Map()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Space bar pressed.')

    screen.fill('white')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    tile.draw(screen=screen)
    test_map.draw(screen=screen)

    pygame.draw.circle(screen, 'blue', player_pos, 40)

    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()
