import pygame
from pygame import SurfaceType
from pygame.time import Clock
from helpers.constants import *
from objects.Player import Player

def main() -> None:
    pygame.init()
    surface: SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    refresh_rate: Clock = pygame.time.Clock()
    delta_time: float = 0.0
    
    # Instantiate Player object
    x: int = PLAYER_POS_X
    y: int = PLAYER_POS_Y
    player: Player = Player(x, y)
    
    # Grouping objects
    drawable = pygame.sprite.Group()
    
    Player.containers = drawable
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        surface.fill(color=(0,0,0))
        
        player.draw(surface)
        player.update(delta_time)
        
        pygame.draw.line(surface,
                         "white",
                         start_pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * -1),
                         end_pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT),
                         width=1
                        )   
        
        pygame.display.flip()
        
        refresh_rate.tick(144)
        delta_time = refresh_rate.tick(60) / 1000


if __name__ == "__main__":
    main()