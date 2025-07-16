import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for a in asteroids:
            collision = a.collision(player)
            if collision is True:
                print("Game over!")
                sys.exit()
        for a in asteroids:
            for s in shots:
                collision = a.collision(s)
                if collision is True:
                    a.split()
                    s.kill()


        pygame.Surface.fill(screen, "black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
