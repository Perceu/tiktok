from turtle import Turtle
from functions import setupScreen, circle_coordenates, gradient_color, format_color
screen  = setupScreen(720,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
def run():
    c_1 = circle_coordenates(tl, 150)
    c_2 = circle_coordenates(tl, 300)
    c_2 = c_2[::-1]
    tl.goto(c_1[0][0],c_1[0][1])
    tl.color('#FFFFFF')
    tl.pendown()

    color_ini = [0xff, 0x00, 0x99]
    color_fim = [0x42, 0x86, 0xf4]

    for c, c2 in zip(c_1, c_2):
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        tl.goto(c2[0],c2[1])
        tl.goto(c[0],c[1])
    
    c_1 = c_1[::-1]
    color_ini = [0x42, 0x86, 0xf4]
    color_fim = [0xff, 0x00, 0x99]
    for c, c2 in zip(c_1, c_2):
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        tl.goto(c2[0],c2[1])
        tl.goto(c[0],c[1])

screen.onkey(run, "r")
screen.listen()
screen.mainloop()