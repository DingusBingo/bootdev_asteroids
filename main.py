import pygame
from constants import *
from circleshape import *
from player import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color_black = (0, 0, 0)

def main():
    pygame.init()
    


def draw_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    screen.fill(color_black)
    player.draw(screen)
    pygame.display.flip()
    dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    player = Player(SCREEN_HEIGHT/2, SCREEN_HEIGHT/2)

    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        draw_loop()