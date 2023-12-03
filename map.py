import pygame

class Map:
    def __init__(self, bridge_img, river_img) -> None:
        self.bridge = pygame.image.load(f'assets/images/{bridge_img}').convert_alpha()
        self.river = pygame.image.load(f'assets/images/{river_img}').convert_alpha()
    
    def draw(self, screen):
        pass