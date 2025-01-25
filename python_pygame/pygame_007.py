import random
import pygame
import time

pygame.init()

windown_size = width, height = 576, 1024
screen = pygame.display.set_mode(windown_size)
ingame = True
run = False
clock = pygame.time.Clock()

def my_line(top_left, bottom_right, color):
    left = top_left + pygame.Vector2(random.randint(-2,2), random.randint(-2,2))
    right = bottom_right + pygame.Vector2(random.randint(-2,2), random.randint(-2,2))
    pygame.draw.line(screen, color, left, right)

def frame_1():
    pygame.draw.circle(screen,'black', (288, 512), 222)

def frame_2():
    pygame.draw.polygon(screen, 'black', ((288,312),(68,662),(508,662)))

def frame_3():
    pygame.draw.rect(screen,'black', pygame.Rect(88, 312, 400, 400))

loop = 0
color = 'white'

frames = [frame_1, frame_2, frame_3]

while ingame:
    clock.tick(15)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                run = not run
    if run:
        loop += 1
        if loop < 50:
            frame = 0
        if loop > 50:
            frame = 1
        if loop > 100:
            frame = 2

        if loop > 150:
            frame = 0
        if loop > 180:
            frame = 1
        if loop > 210:
            frame = 2

        if loop > 240:
            frame = 0
        if loop > 270:
            frame = 1
        if loop > 300:
            frame = 2

        if loop > 320:
            frame = 0
        if loop > 340:
            frame = 1
        if loop > 360:
            frame = 2

        if loop > 380:
            frame = 0
        if loop > 400:
            frame = 1
        if loop > 420:
            frame = 2

        if loop > 430:
            frame = 0
        if loop > 440:
            frame = 1
        if loop > 450:
            frame = 2

        if loop > 460:
            frame = 0
        if loop > 470:
            frame = 1
        if loop > 480:
            frame = 2

        if loop > 490:
            frame = 0
        if loop > 500:
            frame = 1
        if loop > 510:
            frame = 2
        if loop > 520:
            frame = 0
            loop = 490

        top_left = pygame.Vector2(5,5)
        top_right = pygame.Vector2(15,5)
        bottom_left = pygame.Vector2(5,15)
        bottom_right = pygame.Vector2(15,15)
        line_width = 5
        if loop % 3 :
            color = random.choice(list(pygame.colordict.THECOLORS.keys()))
        else:
            color = 'white'
        while line_width < width:
            top_left = pygame.Vector2(5,5)
            top_right = pygame.Vector2(15,5)
            bottom_left = pygame.Vector2(5,15)
            bottom_right = pygame.Vector2(15,15)
            while top_left[1] < height:
                top_left[0] = line_width
                top_right[0] = line_width + 15
                bottom_right[0] = line_width + 15
                bottom_left[0] = line_width

                if random.randint(0,1):
                    if random.randint(0,1):
                        my_line(top_left, bottom_right, color)
                    else:
                        my_line(top_right, bottom_left, color)

                top_left += pygame.Vector2(0, 15)
                top_right += pygame.Vector2(0, 15)
                bottom_right += pygame.Vector2(0, 15)
                bottom_left += pygame.Vector2(0, 15)
            line_width += 15

        frames[frame]()
        

        
    pygame.display.update()