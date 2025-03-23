import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color_black = (0, 0, 0)

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def draw_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    screen.fill(color_black)
    pygame.display.flip()

if __name__ == "__main__":
    main()
    while True:
        draw_loop()