import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
    def update(self, dt):
        self.position += self.velocity * dt
    

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)

            new1 = Asteroid(self.position.x, self.position.y, new_radius)
            new1.velocity = new_velocity1 * 1.2
            new2 = Asteroid(self.position.x, self.position.y, new_radius)
            new2.velocity = new_velocity2 * 1.2
        self.kill()
