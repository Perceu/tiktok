import random
import pygame
import time

from firework_common import Firework

pygame.init()

windown_size = width, height = 576, 1024
screen = pygame.display.set_mode(windown_size)
ingame = True
run = False
gravity = pygame.Vector2(0, 0.2)
fireworks: list[Firework] = []
clock = pygame.time.Clock()

# for p in particles:
#     p.apply_force(10)


while ingame:
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                run = not run
    if run:
        if random.random() < 0.1:
            fireworks.append(
                Firework(screen)
            )

    for idx, f in enumerate(fireworks):
        f.update(gravity)
        f.draw()

    pygame.display.update()
