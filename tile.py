import pygame


class Tile():
    def __init__(self, tilepath) -> None:
        self.tile_image = pygame.image.load(f'assets/images/{tilepath}').convert_alpha()

    def draw(self, screen, size, start_pos) -> None:
        rows, cols = 10, 15
        for row in range(rows):
            for col in range(cols):
                screen.blit(self.tile_image, (start_pos[0] + col * size[0], start_pos[1] + row * size[1]))
