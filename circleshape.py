import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers) # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def collided(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius


    # subclasses override
    def draw(self, screen):
        pass


    # subclasses override
    def update(self, dt):
        pass
