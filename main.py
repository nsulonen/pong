import pygame
from pygame import SurfaceType
from pygame.time import Clock
from constants import *

def main() -> None:
    pygame.init()
    screen: SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time: Clock = pygame.time.Clock()
    deltatime: float = 0.0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color=(0,0,0))
        
        pygame.display.flip()
        
        time.tick(60)
        deltatime = time.tick(60) / 1000


if __name__ == "__main__":
    main()