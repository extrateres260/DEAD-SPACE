import sys
import os
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def run_game(screen, clock):
    # Load frame file names once
    frame_folder = "frames"
    frame_files = sorted([f for f in os.listdir(frame_folder) if f.endswith(".png")])
    frame_index = 0

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    # Assign sprite containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    font = pygame.font.SysFont(None, 30)  # Font for cooldown text
    dt = 0
    
    explosion_frames = []
    explosion_folder = 'frames2'
    frame_files = sorted([f for f in os.listdir(explosion_folder) if f.endswith('.png')])
    

    for file in frame_files:
        img = pygame.image.load(os.path.join(explosion_folder, file)).convert_alpha()
        explosion_frames.append(pygame.transform.scale(img, (64, 64)))  # Adjust size as needed


    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "home"
            
            
        keys = pygame.key.get_pressed()

        # Bomb key check here:
        if keys[pygame.K_b]:
           
            player.explodeEnemies(asteroids, explosions, explosion_frames)

        # Load and scale the next background frame
        frame_path = os.path.join(frame_folder, frame_files[frame_index])
        background = pygame.image.load(frame_path).convert()
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        frame_index = (frame_index + 1) % len(frame_files)

        # Update game state
        updatable.update(dt)
        
        explosions.update(dt)

        # Collision detection
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                return "home"

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        # Draw
        screen.blit(background, (0, 0))
        for obj in drawable:
            obj.draw(screen)
            

        explosions.draw(screen)
            
        # Draw cooldown text
        if player.bomb_Timer > 0:
            cooldown_text = f'Bomb ready in: {player.bomb_Timer:.1f}s'
        else:
            cooldown_text = 'Bomb ready! Press B'

        text_surface = font.render(cooldown_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000
