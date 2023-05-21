from turtle import Turtle

from functions import setupScreen, gradient_color, format_color
screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
def run():
    color_ini = [0xff, 0x00, 0x99]
    color_fim = [0x42, 0x86, 0xf4]
    rtdeg=46
    turndir=-2
    for _ in range(360*16):
        tl.fd(10)
        tl.rt(rtdeg)
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        if rtdeg>46:
            rtdeg=46
            turndir=-2
            color_ini = [0x42, 0x86, 0xf4]
            color_fim = [0xff, 0x00, 0x99]
        elif rtdeg<-45:
            rtdeg=-45
            turndir=2
            color_ini = [0xff, 0x00, 0x99]
            color_fim = [0x42, 0x86, 0xf4]
        rtdeg+=turndir

screen.onkey(run, "r")
screen.listen()
screen.mainloop()