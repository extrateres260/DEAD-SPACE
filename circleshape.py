import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius=0):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self._position = pygame.Vector2(x, y)        # Protected
        self.__radius = radius                       # Private
        self._velocity = pygame.Vector2(0, 0)         # Protected

    # --- Getters and Setters ---

    def get_position(self):
        return self._position

    def set_position(self, new_position):
        self._position = pygame.Vector2(new_position)

    def get_velocity(self):
        return self._velocity

    def set_velocity(self, new_velocity):
        self._velocity = pygame.Vector2(new_velocity)

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius): 
        self.__radius = new_radius

    # --- Methods ---

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision(self, other):
        # Use getters for encapsulated data
        return self.get_position().distance_to(other.get_position()) <= self.get_radius() + other.get_radius()
