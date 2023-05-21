from turtle import Turtle
from functions import setupScreen, gradient_color, format_color, triangle_2

screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()

def run():
    color_ini = [0x1a, 0x2a, 0x6c]
    color_fim = [0xfb, 0xbb, 0x2d]
    size = 15
    for i in range(270):
        color_ini = gradient_color(color_ini, color_fim)       
        tl.pencolor(format_color(color_ini))
        size += 5
        if size <= 0:
            break
        triangle_2(tl, size)
        tl.right(3)
    screen.exitonclick()

screen.onkey(run, "r")
screen.listen()
screen.mainloop()