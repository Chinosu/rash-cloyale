import pygame


class Chaser:
    def __init__(self, screen, speed, position = None) -> None:
        if position == None:
            self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        else:
            self.position = position
        self.speed = speed

    def chase(self, target_position):
        """
        For now, assume target_position is a pygame.Vector2
        """
        direction = target_position - self.position
        unit = direction.normalize()
        self.position += unit * self.speed;
