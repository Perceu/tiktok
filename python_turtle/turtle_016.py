from turtle import Turtle

from functions import setupScreen, gradient_color, format_color
screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
def run():
    color_ini = [0xff, 0x00, 0x99]
    color_fim = [0x42, 0x86, 0xf4]
    circle_rad = 0
    circles = 0
    while True:
        color_ini = gradient_color(color_ini, color_fim)
        tl.pencolor(format_color(color_ini))
        for _ in range(4):
            tl.forward(80)
            tl.right(90)

        tl.right(10)
        circle_rad += 10
        if circle_rad > 360:
            if circles < 13:
                circles += 1
                tl.right(15)
                tl.forward(50)
                circle_rad = 0
                if circles % 2:
                    color_ini = [0x42, 0x86, 0xf4]
                    color_fim = [0xff, 0x00, 0x99]
                else:
                    color_ini = [0xff, 0x00, 0x99]
                    color_fim = [0x42, 0x86, 0xf4]
            else:
                break

screen.onkey(run, "r")
screen.listen()
screen.mainloop()