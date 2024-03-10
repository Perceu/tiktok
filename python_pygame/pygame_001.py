
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
        self.head = [255,0,0]
        self.x = 0
        self.y = 0
        self.green = 1
        self.left = (-21,0)
        self.right = (21,0)
        self.down = (0,21)
        self.up = (0,-21)
        self.directions = []

    def _get_direction(self):
        direction = random.randint(0,4)
        print(direction)
        if direction == 0:
                    
            if (self.x + self.left[0] < 0):
                return False
            
            self.x += self.left[0]
            self.y += self.left[1]

            if [self.x, self.y] in self.directions:
                return False

            return True
        elif direction == 1:
            if (self.x + self.right[0] > width):
                return False
                      
            self.x += self.right[0]
            self.y += self.right[1]

            if [self.x, self.y] in self.directions:
                return False
            
            return True
        
        elif direction == 2:
            if (self.y + self.down[1] > height):
                return False
            
            self.x += self.down[0]
            self.y += self.down[1]

            if [self.x, self.y] in self.directions:
                return False
            
            return True
        
        elif direction == 3:
            if (self.y + self.up[1] < 0):
                return False
            
            self.x += self.up[0]
            self.y += self.up[1]
            
            if [self.x, self.y] in self.directions:
                return False
            
            return True
        
        else:
            return False
        
    def update(self):      
        new_direction = True
        while new_direction:
            if self._get_direction():
                if [self.x, self.y] not in self.directions:
                    self.directions.append([self.x, self.y])
                new_direction = False

    def draw(self):
        screen.fill((0,0,0))
        for body in self.directions:
            rect = pygame.Rect(body[0], body[1],20,20)
            pygame.draw.rect(self.screen, self.color, rect, 20, 2)

        rect = pygame.Rect(self.x, self.y,20,20)
        pygame.draw.rect(self.screen, self.head, rect, 20, 2)
        
        

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