import pygame
import random

def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class Star():

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.pz = self.z
        self.color = pygame.colordict.THECOLORS['white']

    def draw(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        sx = remap(self.x/self.z,0,1,0,width)+ int(width/2)
        sy = remap(self.y/self.z,0,1,0,height)+ int(height/2)

        size = remap(self.z, 0, width, 8, 0)
        if sx < 0:
            size = 0
            sx = 0

        if sy < 0:
            size = 0
            sy = 0

        pygame.draw.circle(screen, self.color, (sx, sy), size)

    def update(self, screen):
        self.z -= 10
        if self.z <= 0:
            width = screen.get_width()
            height = screen.get_height()
            self.z = width
            self.x = random.randint(-width, width)
            self.y = random.randint(-height, height)
            self.pz = self.z
        pass
