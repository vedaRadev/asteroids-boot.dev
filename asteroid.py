import pygame
import constants
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,
                           "white",
                           self.position,
                           self.radius,
                           width = 2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        rand1 = self.velocity.rotate(angle)
        rand2 = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = rand1 * 1.2
        asteroid_2.velocity = rand2
