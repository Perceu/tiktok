import pygame
import time
import math
import random

pygame.init()

windown_size = width, height = 720, 1280
screen = pygame.display.set_mode(windown_size)
ingame = True
run = False

class Wave():
    def __init__(self, position):
        self.position_initial = position
        self.size_out = 5
        self.size_in = 0
        self.running = True
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.size = random.randint(2,7)

    def update(self):
        self.size_in += self.size
        self.size_out += self.size

    def draw_circle(self):
        pygame.draw.circle(screen, self.white, self.position_initial, self.size_out)
        pygame.draw.circle(screen, self.black, self.position_initial, self.size_in)
        self.update()

    def draw(self):
        self.draw_circle()

waves = []
while ingame:
    screen.fill((0,0,0))
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                run = not run

    if run:
        if random.randint(0,1) and len(waves) < 30:
            pos_1 = random.randint(80, width-80)
            pos_2 = random.randint(80, height-80)
            waves.append(Wave((pos_1, pos_2)))

        for wave in waves:
            wave.draw()

        for key, wave in enumerate(waves):
            if wave.size_out > width and wave.size_out > height:
                del(waves[key])
        
    pygame.display.update()