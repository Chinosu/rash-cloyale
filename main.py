import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()
pygame.display.set_caption('Maow')
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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

    pygame.draw.circle(screen, 'blue', player_pos, 40)

    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()
