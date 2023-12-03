import pygame


class Chaser:
    def __init__(self, speed, position = None) -> None:
        self.speed = speed
        if position == None:
            self.position = pygame.Vector2(0, 0)
        else:
            self.position = position

    def chase(self, target_position):
        """
        For now, assume target_position is a pygame.Vector2
        """
        direction = target_position - self.position
        unit = direction.normalize()
        self.position += unit * self.speed;
