import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from tile import Tile
from chaser import Chaser
from map import Map
from card import cardWindow

def barrier_check(pos):
    # print(pos)
    pixel = screen.get_at((round(pos.x), round(pos.y)))
    return pixel == (0, 0, 0) or pixel == (0, 0, 255)

pygame.init()
pygame.display.set_caption('Maow')
screen = pygame.display.set_mode([600, 1000]) # screen <=> surface
clock = pygame.time.Clock()

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
tile = Tile('grass-tile.png')
chaser = Chaser(barrier_check, 1)
test_map = Map()
card_window = cardWindow()
bridge_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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
    card_window.draw(screen=screen)

    if chaser.position.y < bridge_pos.y and player_pos.y < bridge_pos.y:
        chaser.chase(player_pos)
    elif chaser.position.y > bridge_pos.y and player_pos.y > bridge_pos.y:
        chaser.chase(player_pos)
    else:
        chaser.chase(bridge_pos)
    pygame.draw.rect(screen, 'pink', (chaser.position.x, chaser.position.y, 20, 25))
    pygame.draw.circle(screen, 'blue', player_pos, 40)

    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()
