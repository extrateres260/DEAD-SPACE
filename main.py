import pygame
from homePage import show_homepage
from Play import run_game

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))  # Match SCREEN_WIDTH and SCREEN_HEIGHT
    clock = pygame.time.Clock()
    current_screen = "home"

    while True:
        if current_screen == "home":
            current_screen = show_homepage(screen)
        elif current_screen == "game":
            current_screen = run_game(screen, clock)

if __name__ == "__main__":
    main()