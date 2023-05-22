from turtle import Turtle
from functions import setupScreen

screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()

def get_color(spectre, ini, fim):
    if ini[spectre] > fim[spectre]:
        ini[spectre] -= 0x1
    elif ini[spectre] < fim[spectre]:
        ini[spectre] += 0x1
    return ini[spectre]

def format_color(color):
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
      
def run():
    color_ini = [0xff, 0x00, 0x42]
    color_fim = [0x00, 0xa7, 0xff]
    circle_size = 4
    while (color_ini != color_fim):
        color_ini[0] = get_color(0, ini=color_ini, fim=color_fim)
        color_ini[1] = get_color(1, ini=color_ini, fim=color_fim)
        color_ini[2] = get_color(2, ini=color_ini, fim=color_fim)
        circle_size += 1
        tl.pencolor(format_color(color_ini))
        tl.circle(circle_size)
        tl.right(5)
    screen.exitonclick()

screen.onkey(run, "r")
screen.listen()
screen.mainloop()