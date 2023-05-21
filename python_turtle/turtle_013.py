from turtle import Turtle
from functions import setupScreen, gradient_color, format_color
screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
def run():
    color_ini = [0x42, 0x86, 0xf4]
    color_fim = [0xff, 0x00, 0x99]
    for k in range(180):
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        tl.forward(180)
        tl.back(180)
        tl.left(2)
        tl.penup()
        tl.forward(5)
        tl.pendown()

    tl.penup()
    tl.back(5)
    tl.right(2)
    tl.left(90)
    tl.forward(90)
    tl.right(90)
    tl.pendown()

    color_ini = [0xff, 0x00, 0x99]
    color_fim = [0x42, 0x86, 0xf4]

    for k in range(180):
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        tl.forward(80)
        tl.back(80)
        tl.left(2)
        tl.penup()
        tl.forward(2)
        tl.pendown()

    screen.exitonclick()
screen.onkey(run, "r")
screen.listen()
screen.mainloop()