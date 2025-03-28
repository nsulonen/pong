import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.position: tuple = pygame.Vector2(x, y)
        self.velocity: tuple = pygame.Vector2(0, 0)
        
        def collides(self, other) -> bool:
            # TODO
            pass
        
        def draw(self, surface) -> None:
            # sub-class overrides
            pass
        
        def update(self, delta_time) -> None:
            # sub-class overrides
            pass