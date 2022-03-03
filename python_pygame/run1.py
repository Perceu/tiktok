
import pygame
import time
import random
pygame.init()

windown_size = width, height = 720, 1280
screen = pygame.display.set_mode(windown_size)
ingame = True

class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.color = [0,255,0]
        self.x = 0
        self.y = 0
        self.multiplicador = 1
        self.blue = -1
        self.green = 1
        
    def update(self):

        self.color[1] = self.color[1] + (1*self.blue)

        if (self.color[1] < 0):
            self.color[1] = 0
            self.blue = 1

        if (self.color[1] > 255):
            self.color[1] = 255
            self.blue = -1


        self.color[2] = self.color[2] + (1*self.green)

        if (self.color[2] > 255):
            self.color[2] = 255
            self.green = -1

        if (self.color[2] < 0):
            self.color[2] = 0
            self.green = 1


        if self.x > 720:
            self.y += 21
            self.multiplicador = -1

        if self.x < 0:
            self.y += 21
            self.multiplicador = 1

        self.x += 21 * self.multiplicador

    def draw(self):
        rect = pygame.Rect(self.x, self.y,20,20)
        pygame.draw.rect(self.screen, self.color, rect, 20, 2)
        

waves = []
square = Snake(screen)
screen.fill((0,0,0))
run = False
while ingame:
    time.sleep(0.03)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                run = True
    if run:
        square.draw()
        square.update()

    pygame.display.update()