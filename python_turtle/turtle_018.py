from turtle import Turtle
from random import randint

from functions import setupScreen, gradient_color, format_color
screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()

def desenhar_arvore(tm_tronco, ini, fim):
    color_ini = gradient_color(ini, fim)
    if tm_tronco < 5:
        tl.pencolor(format_color(color_ini))
        tl.circle(3)
        tl.color("white")
        return 
    else:
        lenght = randint(3,tm_tronco)
        lenght_child = randint(3,tm_tronco)
        lenght_child_2 = randint(3,tm_tronco)
        tl.forward(lenght)
        tl.left(30)
        desenhar_arvore(lenght_child, color_ini, fim)
        tl.right(60)
        desenhar_arvore(lenght_child_2, color_ini, fim)
        tl.left(30)
        tl.back(lenght)

def run():
    color_ini = [0xff, 0x00, 0x99]
    color_fim = [0x42, 0x86, 0xf4]
    tl.penup()
    tl.back(200)
    for _ in range(5):
        color_ini = gradient_color(color_ini, color_fim)
        tl.left(90)
        tl.color("white")
        tl.pendown()
        desenhar_arvore(100,color_ini, color_fim)
        tl.penup()
        tl.right(90)
        tl.forward(100)
    

screen.onkey(run, "r")
screen.listen()
screen.mainloop()