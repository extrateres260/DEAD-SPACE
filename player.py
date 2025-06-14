

import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from asteroid import *
from explosion import Explosion

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.shoot_sound = pygame.mixer.Sound('sound/laser-312360.mp3')
        self.bomb_Timer = 0
        self.explosion_sound = pygame.mixer.Sound('sound/explosion.mp3')

        self.original_image = pygame.image.load("Images/PNG/player.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (60, 100))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.get_position())

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)
        rotated_rect = rotated_image.get_rect(center=self.get_position())
        screen.blit(rotated_image, rotated_rect)
        self.rect = rotated_rect

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot_sound.play()
            self.shoot()

        if self.bomb_Timer > 0:
            self.bomb_Timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.set_position(self.get_position() + forward * PLAYER_SPEED * dt)

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.get_position().x, self.get_position().y)
        shot.set_velocity(pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)

    def explodeEnemies(self, asteroids, explosions_group, explosion_frames):
        if self.bomb_Timer > 0:
            return

        for enemy in asteroids:
            Explosion(enemy.rect.center, explosion_frames, explosions_group)
            self.explosion_sound.play()
            enemy.kill()

        self.bomb_Timer = BOMB_COOL_DOWN
