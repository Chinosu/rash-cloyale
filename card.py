import pygame

class cardWindow:
    def __init__(self) -> None:
        card_width = 100
        card_height = 150
        card_colour = 'Green'

        self.window = pygame.Surface((600, 200))
        self.window.fill('Grey')

        self.card1 = pygame.Surface((card_width, card_height))
        self.card1.fill(card_colour)

        self.card2 = pygame.Surface((card_width, card_height))
        self.card2.fill(card_colour)

        self.card3 = pygame.Surface((card_width, card_height))
        self.card3.fill(card_colour)

        self.card4 = pygame.Surface((card_width, card_height))
        self.card4.fill(card_colour)
    
    def draw(self, screen):
        screen.blit(self.window, (0, 800))

        screen.blit(self.card1, (25, 825))
        screen.blit(self.card2, (175, 825))
        screen.blit(self.card3, (325, 825))
        screen.blit(self.card4, (475, 825))