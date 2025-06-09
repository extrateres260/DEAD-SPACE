import sys
import pygame
import pygwidgets
import cv2

def show_homepage(screen):
    background = pygwidgets.Image(screen, (0, 0), 'NEW_BACK.png')
    play_button = pygwidgets.TextButton(screen, (400, 530), 'ENTER', width=100, height=45)
    quit_button = pygwidgets.TextButton(screen, (880, 530), 'QUIT', width=100, height=45)
    
    pygame.mixer.music.load('sound/battle-march-action-loop-6935.mp3')
    pygame.mixer.music.play(-1, 0.0)

    buttonSound = pygame.mixer.Sound('sound/button-202966.mp3')
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if play_button.handleEvent(event):
                buttonSound.play()
                pygame.mixer.music.stop()
                return "game"

            if quit_button.handleEvent(event):
                buttonSound.play()
                pygame.quit()
                sys.exit()

        screen.fill("black")
        background.draw()
        play_button.draw()
        quit_button.draw()

        pygame.display.flip()
        clock.tick(60)
