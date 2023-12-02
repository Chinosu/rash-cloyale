import pygame


class Tile():
    def __init__(self, tile_path) -> None:
        self.tile_image = pygame.image.load(f'assets/images/{tile_path}').convert_alpha()

    def draw(self, screen) -> None:
        screen_width, screen_height = screen.get_size()
        tile_width, tile_height = self.tile_image.get_size()
        columns = screen_width // tile_width + 1
        rows = screen_height // tile_height + 1

        for row in range(rows):
            for column in range(columns):
                x = column * tile_width
                y = row * tile_height
                screen.blit(self.tile_image, (x, y))


