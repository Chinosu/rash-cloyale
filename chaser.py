import pygame
from pygame.math import Vector2
from math import sin, cos, radians

class Chaser:
    def __init__(self, barrier_callback, speed, position = None) -> None:
        """
        barrier_callback must
          - be a function which takes a Vector2 as an argument
          - return True when a barrier is encountered, otherwise false
        """
        self.barrier_callback = barrier_callback
        self.speed = speed
        if position == None:
            self.position = pygame.Vector2(0, 0)
        else:
            self.position = position

    def chase(self, target_position):
        """
        For now, assume target_position is a pygame.Vector2
        """
        _, angle = (target_position - self.position).as_polar()
        angle = radians(angle)
        angle_delta = 0
        count = 0
        while count < 500:
            left = self.speed * Vector2(cos(angle - angle_delta), sin(angle - angle_delta))
            if not self.barrier_callback(self.position + left):
                self.position += left
                return
            right = self.speed * Vector2(cos(angle + angle_delta), sin(angle + angle_delta))
            if not self.barrier_callback(self.position + right):
                self.position += right
                return
            angle_delta += radians(15)
            count += 1
        raise Exception('Likely infinite loop discovered at Chaser.chase')