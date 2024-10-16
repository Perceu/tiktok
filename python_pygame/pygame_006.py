import random
from re import X
import pygame

from common.startfield import Star

pygame.init()

windown_size = width, height = 576, 1024
screen = pygame.display.set_mode(windown_size)
ingame = True
run = False
gravity = pygame.Vector2(0, 0.2)
stars: list[Star] = []
clock = pygame.time.Clock()


for i in range(1000):
    x = random.randint(-(width-50), width-50)
    y = random.randint(-(height-50), height-50)
    z = random.randint(0, width)
    stars.append(Star(x,y,z))


while ingame:
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                run = not run

    for star in stars:
        star.update(screen)
        star.draw(screen)

    pygame.display.update()
