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
        
    def move(self, delta_time: float) -> None:
        self.y += 1000 * delta_time
        
    def update(self, delta_time: float) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.move(-delta_time)
        if keys[pygame.K_s]:
            self.move(delta_time)