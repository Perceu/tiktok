from turtle import Turtle
from functions import setupScreen, gradient_color, format_color, square
screen  = setupScreen(720,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()

def run():
    color_ini = [0xff, 0x00, 0x99]
    color_fim = [0x42, 0x86, 0xf4]
    for _ in range(360):
        for size in range(int(720/2)):
            tl.pendown()
            square(tl, size*4)
            tl.left(3)
            tl.penup()
            tl.goto(0,0)
            tl.back((size*4)/2)
            tl.left(90)
            tl.forward((size*4)/2)
            tl.right(90)


            tl.pencolor(format_color(color_ini))
            color_ini = gradient_color(color_ini, color_fim)
            
screen.onkey(run, "r")
screen.listen()
screen.mainloop()