from turtle import Screen, Turtle
from functions import square
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
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
      
def run(x, y):
    color_ini = [0x40, 0xc9, 0xff]
    color_fim = [0xe8, 0x1c, 0xff]
    circle_size = 3
    size = 5
    while (color_ini != color_fim):
        color_ini[0] = get_color(0, ini=color_ini, fim=color_fim)
        color_ini[1] = get_color(1, ini=color_ini, fim=color_fim)
        color_ini[2] = get_color(2, ini=color_ini, fim=color_fim)
        circle_size += 1
        tl.pencolor(format_color(color_ini))
        size += 5
        square(tl, size)
        tl.right(3)
    screen.exitonclick()

screen.onclick(run)
screen.mainloop()