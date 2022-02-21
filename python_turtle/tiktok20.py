from random import randint
from turtle import Turtle, color
from functions import setupScreen, gradient_color, format_color, square
screen  = setupScreen(720,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()

def run():
    color_ini = [0xff, 0x15, 0x59]
    color_fim = [0x22, 0x99, 0xff]
    tl.penup()
    tl.forward(200)
    tl.pendown()
    for _ in range(360):
        tl.pencolor(format_color(color_ini))
        tl.forward(100)
        tl.left(2)
        tl.back(100)
        tl.right(3)
        color_ini = gradient_color(color_ini, color_fim)

    tl.penup()
    tl.goto(0,0)
    tl.pendown()

    color_ini = [0x22, 0x99, 0xff]
    color_fim = [0xff, 0x15, 0x59]
    for r in range(2,800,4):
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))

        tl.penup()
        tl.goto(0,0)
        tl.right(90)
        tl.forward(r)
        tl.left(90)
        tl.pendown()

        tl.circle(r)


screen.onkey(run, "r")
screen.listen()
screen.mainloop()