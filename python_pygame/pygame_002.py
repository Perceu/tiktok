import pygame
import time
import random

pygame.init()

windown_size = width, height = 720, 1280

fireColors = [
    pygame.Color(0,0,0),
    pygame.Color(7,7,7),
    pygame.Color(31,7,7),
    pygame.Color(45,15,7),
    pygame.Color(71,15,7),
    pygame.Color(87,23,7),
    pygame.Color(103,31,7),
    pygame.Color(119,31,7),
    pygame.Color(143,39,7),
    pygame.Color(159,47,7),
    pygame.Color(175,63,7),
    pygame.Color(191,71,7),
    pygame.Color(199,71,7),
    pygame.Color(223,79,7),
    pygame.Color(223,87,7),
    pygame.Color(223,87,7),
    pygame.Color(215,95,7),
    pygame.Color(215,103,15),
    pygame.Color(207,111,15),
    pygame.Color(207,119,15),
    pygame.Color(207,127,15),
    pygame.Color(207,135,23),
    pygame.Color(199,135,23),
    pygame.Color(199,143,23),
    pygame.Color(199,151,31),
    pygame.Color(191,159,31),
    pygame.Color(191,159,31),
    pygame.Color(191,167,39),
    pygame.Color(191,167,39),
    pygame.Color(191,175,47),
    pygame.Color(183,175,47),
    pygame.Color(183,183,47),
    pygame.Color(183,183,55),
    pygame.Color(207,207,111),
    pygame.Color(223,223,159),
    pygame.Color(239,239,199),
    pygame.Color(255,255,255),
]
font = pygame.font.SysFont('ubuntu', 30)

screen = pygame.display.set_mode(windown_size)
ingame = True
firePixelArray = []

fireHeight = 60
fireWidth = 80

pixelHeight = 25
pixelWidth = 25

firePixelArray = [0,]*(fireHeight*fireWidth)  

def createFireSource():
    for col in range(fireWidth):
        overflowPixel = fireHeight*fireWidth
        pixelIndex = (overflowPixel - fireWidth) + col
        firePixelArray[pixelIndex] = len(fireColors)-1

def updatePixelIntensity(currentPixel):
    bellowPixel = currentPixel + fireWidth
    decay = random.randint(1,5)
    if bellowPixel >= (fireHeight*fireWidth):
        return
    newIntencity = firePixelArray[bellowPixel] - decay
    if newIntencity > 0:
        firePixelArray[currentPixel + decay] = newIntencity
    else:
        firePixelArray[currentPixel + decay] = 0

def calculatePropagation():
    for col in range(fireWidth):
        for row in range(fireHeight):
            pixelIndex = col + (fireWidth * row)
            updatePixelIntensity(pixelIndex)

def renderFire():
    debug = False
    for row in range(fireHeight):
        for col in range(fireWidth):
            pixelIndex = col + (fireWidth * row)
            colY = height - (pixelHeight * (fireHeight - row))
            colX = col * pixelWidth
            if debug == True:
                textsurface = font.render(str(firePixelArray[pixelIndex]), False, (255, 255, 255))
                screen.blit(textsurface,(colX,colY))
            else:
                intensity = firePixelArray[pixelIndex]
                myPixel = pygame.Rect(colX,colY, pixelWidth,pixelHeight)
                pygame.draw.rect(screen, fireColors[intensity], myPixel)

createFireSource()

while ingame:
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False 
    screen.fill((0,0,0))
    calculatePropagation()
    renderFire()
    pygame.display.update()