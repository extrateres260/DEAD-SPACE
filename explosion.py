import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, frames, *groups):
        super().__init__(*groups)
        self.frames = frames
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=position)
        self.animation_speed = 0.1  # seconds per frame
        self.timer = 0
        

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.index += 1
            if self.index >= len(self.frames):
                self.kill()  # Remove explosion after animation finishes
            else:
                self.image = self.frames[self.index]
