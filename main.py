import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

pygame.display.set_caption('Maow')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Space bar pressed.')
        
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()

pygame.quit()