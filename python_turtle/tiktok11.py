from turtle import Turtle
from functions import setupScreen, gradient_color, format_color, square
screen  = setupScreen(360,640)
tl = Turtle()
tl.speed(0)
tl.hideturtle()

def run():
    color_ini = [0x1a, 0x2a, 0x6c]
    color_fim = [0xfb, 0xbb, 0x2d]
    size = 5
    for i in range(80):
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        size += 5
        if size <= 0:
            break
        tl.circle(size)
        tl.right(90)
        tl.penup()
        tl.fd(5)
        tl.pendown()
        tl.left(90)


    tl.penup()
    tl.goto(-45,-45)
    tl.pendown()
    size = 2
    color_ini = [0x00, 0xf2, 0x60]
    color_fim = [0x05, 0x75, 0xe6]
    for i in range(90):
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        size += 8
        if size <= 0:
            break
        tl.penup()
        tl.back(4)
        tl.left(90)
        tl.fd(4)
        tl.right(95)
        tl.pendown()

        square(tl,size)

    screen.exitonclick()

screen.onkey(run, "r")
screen.listen()

screen.mainloop()