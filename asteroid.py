import pygame
import random
from circleshape import CircleShape
from constants import *

color_yellow = (255, 255, 0)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, color_yellow, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self,):
        r = self.radius
        p = self.position
        v = self.velocity
        self.kill()
        if r == ASTEROID_MIN_RADIUS:
            return
        else:
            a = random.uniform(20, 50)
            va = v.rotate(a)
            vb = v.rotate(-a)
            r -= ASTEROID_MIN_RADIUS
            aa = Asteroid(p.x, p.y, r)
            aa.velocity = va * 1.2
            ab = Asteroid(p.x, p.y, r)
            ab.velocity = vb * 1.2
