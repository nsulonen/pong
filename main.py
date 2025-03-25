import pygame
from pygame import SurfaceType
from constants import *

def main() -> None:
    pygame.init()
    screen: SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        
        screen.fill(color=(0,0,0))
        
        pygame.display.flip()
    


if __name__ == "__main__":
    main()