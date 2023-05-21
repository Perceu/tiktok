from turtle import Screen

def setupScreen(width, height, color="black"):
    screen = Screen()
    screen.setup(width, height)
    screen.colormode(255)
    screen.bgcolor(color)
    return screen

def circle_coordenates(tl, raio):
    tl.color('#ffffff')
    coordenates = list()
    for _ in range(180):
        tl.penup()
        tl.fd(raio)
        coordenates.append(tl.pos())
        tl.pendown()
        tl.circle(1)
        tl.penup()
        tl.back(raio)
        tl.left(2)
    return coordenates

def square(turtle, size):
    for i in range(4):
        turtle.fd(size)
        turtle.right(90)

def triangle(turtle, size):
    for i in range(3):
        turtle.fd(size)
        turtle.right(120)

def triangle_2(turtle, size):
    for i in range(4):
        turtle.fd(size)
        turtle.right(120)

def get_color(spectre, ini, fim):
    if ini[spectre] > fim[spectre]:
        ini[spectre] -= 0x1
    elif ini[spectre] < fim[spectre]:
        ini[spectre] += 0x1
    return ini[spectre]

def gradient_color(color_ini, color_fim):
    color = [0,0,0]
    color[0] = get_color(0, ini=color_ini, fim=color_fim)
    color[1] = get_color(1, ini=color_ini, fim=color_fim)
    color[2] = get_color(2, ini=color_ini, fim=color_fim)
    return color

def format_color(color):
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"