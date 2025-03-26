import pygame
from helpers.constants import *
from objects.Block import Block


class Player(Block):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

        self.x = x
        self.y = y
        
    def draw(self, surface) -> None:
        pygame.draw.rect(surface, "white", pygame.Rect(self.x, self.y, 20, 100))