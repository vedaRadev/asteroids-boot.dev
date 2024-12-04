import os
import pygame
from constants import *
from player import Player

def main():
    os.environ["SDL_VIDEODRIVER"] = "x11"

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill(pygame.Color(0, 0, 0))
        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000



# Only run the following if this file was run directly.
# Avoids running when we're imported as a module.
if __name__ == "__main__":
    main()
