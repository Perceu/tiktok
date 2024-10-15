import random
import pygame
import math
from pygame import Vector2

class Particle:
    def __init__(self, x, y, color:str='white', firework=False) -> None:
        self.pos = Vector2(x, y)
        self.firework = firework
        self.lifespan: int = 255
        self.acc = Vector2(0,0)
        self.size = random.randint(1,5)
        self.color = pygame.colordict.THECOLORS.get(color, (255,255,255,255))
        if firework:
            self.vel = Vector2(0,random.randint(-20, -10))
        else:
            self.vel = self.random_direction()
            self.vel *= random.randint(1,6)

    @property
    def done(self):
        if self.lifespan < 0:
            return True
        return False

    def random_direction(self):
        a = math.radians(random.randint(0, 360))
        return pygame.Vector2(math.cos(a), math.sin(a))

    def apply_force(self, force):
        self.acc += force

    def update(self, screen = None):
        if not self.firework:
            self.vel *= 0.9
            self.lifespan -= 4
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw_rect_alpha(self, surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

    def draw(self, display):
        pixel = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)
        if not self.firework:
            self.color = pygame.Color(self.color[0], self.color[1], self.color[2], self.lifespan)
            self.draw_rect_alpha(display, self.color, pixel)
        else:
            self.color = pygame.Color(self.color[0], self.color[1], self.color[2])
            self.draw_rect_alpha(display, self.color, pixel)

class Firework:
    def __init__(self, screen) -> None:
        self.color = random.choice(list(pygame.colordict.THECOLORS.keys()))
        width = screen.get_width()
        x = random.randint(50, width-50)
        height = screen.get_height()
        self.firework = Particle(x, height, color=self.color, firework=True)
        self.screen = screen
        self.particles = []
        self.exploded = False

    def done(self):
        if self.exploded and len(self.particles) == 0:
            return True
        return False

    def explode(self):
        particles_count = random.randint(50,100)
        for i in range(particles_count):
            p = Particle(self.firework.pos.x, self.firework.pos.y, self.color, False)
            self.particles.append(p)

    def update(self, gravity):
        if not self.exploded:
            self.firework.apply_force(gravity)
            self.firework.update(self.screen)
            if self.firework.vel.y >= 0:
                self.exploded = True
                self.explode()

        for idx, p in enumerate(self.particles):
            p.apply_force(gravity)
            p.update()
            if p.done:
                self.particles.pop(idx)

    def draw(self):
        if not self.exploded:
            self.firework.draw(self.screen)
        else:
            for p in self.particles:
                p.draw(self.screen)
