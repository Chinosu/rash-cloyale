import pygame

class Map:
    def __init__(self, bridge_img, river_img) -> None:
        self.bridge = pygame.image.load(f'assets/images/{bridge_img}').convert_alpha()
        self.river = pygame.image.load(f'assets/images/{river_img}').convert_alpha()
    
    def draw(self, screen):
        bridge_width, bridge_height = self.bridge.get_size()
        river_width, river_height = self.river.get_size()

        river_x = (screen.get_width() - river_width) // 2
        river_y = (screen.get_height() - river_height) // 2
        
        bridge_x = (screen.get_width() - bridge_width) // 2
        bridge_y = (screen.get_height() - bridge_height) // 2

        screen.blit(self.river, (river_x, river_y))
        screen.blit(self.bridge, (bridge_x, bridge_y))