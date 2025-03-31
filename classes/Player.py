import pygame
from helpers.constants import *
from classes.Block import Block


class Player(Block):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        
        self.x = x
        self.y = y
        
    def draw(self, surface) -> None:
        pygame.draw.rect(surface, "white", pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        
    def move(self, delta_time: float) -> None:
        if self.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.y = SCREEN_HEIGHT - PLAYER_HEIGHT
        elif self.y < 0:
            self.y = 0
            
        self.y += 1000 * delta_time
        
    def update(self, delta_time: float) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.move(-delta_time)
        if keys[pygame.K_s]:
            self.move(delta_time)