# asteroid.py

import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Load a random enemy spaceship image here
        asteroid_images = [
            pygame.image.load("Images/PNG/Enemies/enemyBlack5.png").convert_alpha(),
            pygame.image.load("Images/PNG/Enemies/enemyBlack4.png").convert_alpha(),
            pygame.image.load("Images/PNG/Enemies/enemyBlack3.png").convert_alpha(),
        ]
        self.original_image = random.choice(asteroid_images)
        size = int(self.radius * 2)  # Width and height for scaling
        self.original_image = pygame.transform.scale(self.original_image, (size, size))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = a * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = b * 1.2
