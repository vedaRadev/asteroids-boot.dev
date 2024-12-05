import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # os.environ["SDL_VIDEODRIVER"] = "x11"

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)               # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = (updatable)                  # type: ignore

    # Some python black magic to construct the player within its assigned groups or something.
    # I guess technically it only creates it once then shares a reference to it in each group.
    # But still, this API where you just instantiate a player
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        _ = screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


# Only run the following if this file was run directly.
# Avoids running when we're imported as a module.
if __name__ == "__main__":
    main()
