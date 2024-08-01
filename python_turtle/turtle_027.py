from turtle import Turtle
from functions import setupScreen
from functions import triangle

screen = setupScreen(580, 1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()


def get_color(spectre, ini, fim):
    if ini[spectre] > fim[spectre]:
        ini[spectre] -= 0x4
    elif ini[spectre] < fim[spectre]:
        ini[spectre] += 0x4
    return ini[spectre]


def format_color(color):
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


def run():
    color_ini = [0xFF, 0xFF, 0xFF]
    color_fim = [0x00, 0xFF, 0x00]
    circle_size = 2

    for i in range(1000):
        color_ini[0] = get_color(0, ini=color_ini, fim=color_fim)
        color_ini[1] = get_color(1, ini=color_ini, fim=color_fim)
        color_ini[2] = get_color(2, ini=color_ini, fim=color_fim)

        if color_ini[2] <= color_fim[2]:
            color_ini = [0xFF, 0xFF, 0xFF]
            circle_size = 2

        circle_size += 10
        tl.pencolor(format_color(color_ini))
        triangle(tl, circle_size)
        tl.right(4)

    screen.exitonclick()


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
