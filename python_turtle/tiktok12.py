from turtle import Turtle
from functions import setupScreen, gradient_color, format_color
screen  = setupScreen(720,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
def run():
    tl.penup()
    tl.back(150)
    tl.pendown()
    color_ini = [0xff, 0x00, 0x99]
    color_fim = [0x42, 0x86, 0xf4]
    for k in range(3):
        color_ini = [0x42, 0x86, 0xf4]
        color_fim = [0xff, 0x00, 0x99]
        for i in range(80):
            color_ini = gradient_color(color_ini, color_fim)
            tl.pencolor(format_color(color_ini))
            tl.circle(300,45)
            tl.left(45)
            tl.circle(300,45)
            tl.left(100+k)
    screen.exitonclick()
screen.onkey(run, "r")
screen.listen()
screen.mainloop()