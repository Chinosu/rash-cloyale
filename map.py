import pygame

class Map:
    def __init__(self) -> None:
        # To be used once assets have been found
        # self.bridge = pygame.image.load(f'assets/images/{bridge_img}').convert_alpha()
        # self.river = pygame.image.load(f'assets/images/{river_img}').convert_alpha()

        self.bridge = pygame.Surface((75, 100))
        self.bridge.fill('Brown')

        self.river = pygame.Surface((1500, 50))
        self.river.fill('Blue')

        self.king = pygame.Surface((150, 150))
        self.king.fill('Black')

        self.princess = pygame.Surface((100, 100))
        self.princess.fill('Black')

        self.enemy_king = pygame.Surface((150, 150))
        self.enemy_king.fill('Black')

        self.enemy_princess = pygame.Surface((100, 100))
        self.enemy_princess.fill('Black')
    
    def draw(self, screen):
        bridge_width, bridge_height = self.bridge.get_size()
        river_width, river_height = self.river.get_size()

        river_x = (screen.get_width() - river_width) // 2
        river_y = (screen.get_height() - river_height) // 2
        
        bridge_x = (screen.get_width() - bridge_width) // 2
        bridge_y = (screen.get_height() - bridge_height) // 2

        screen.blit(self.river, (river_x, river_y))
        screen.blit(self.bridge, (bridge_x, bridge_y))

        screen.blit(self.king, (100, 750))
        screen.blit(self.princess, (1300, 600))

        screen.blit(self.enemy_king, (1250, 100))
        screen.blit(self.enemy_princess, (100, 300))