import pygame

from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.get_position(), self.get_radius(), 2)   
        
    def update(self, dt):
        new_position = self.get_position() + self.get_velocity() * dt
        self.set_position(new_position)
    