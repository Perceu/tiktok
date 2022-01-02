from turtle import Screen, Turtle
from functions import triangle, get_color, format_color
screen = Screen()
screen.setup(360, 640)
screen.colormode(255)
screen.bgcolor("black")
tl = Turtle()
tl.speed(0)
tl.hideturtle()
      
def gradient_color(color_ini, color_fim):
    color = [0,0,0]
    color[0] = get_color(0, ini=color_ini, fim=color_fim)
    color[1] = get_color(1, ini=color_ini, fim=color_fim)
    color[2] = get_color(2, ini=color_ini, fim=color_fim)
    return color

def run(x, y):
    color_ini = [0x59, 0xc1, 0x73]
    color_fim = [0x5d, 0x26, 0xc1]
    size = 950
    for i in range(200):
        color_ini = gradient_color(color_ini, color_fim)       
        tl.pencolor(format_color(color_ini))
        size -= 5
        if size <= 0:
            break
        triangle(tl, size)
        tl.right(3)
    screen.exitonclick()

screen.onclick(run)
screen.mainloop()