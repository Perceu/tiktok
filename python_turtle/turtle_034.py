from turtle import Turtle
from functions import setupScreen, gradient_color, format_color

screen = setupScreen(576, 1024)
tl = Turtle()
tl.speed(0)
tl.hideturtle()

def run():
    color_ini = [0xf5, 0xf5, 0x41]
    color_fim = [0xf5, 0x3c, 0x3c]
    circle = False
    for j in range(30):
        for i in range (15):
            color_ini = gradient_color(color_ini, color_fim)       
            tl.pencolor(format_color(color_ini))
            tl.right(90)
            tl.circle(200-j*4, 90)
            tl.left(90)
            tl.circle(200-j*4, 90)
            tl.right(180)
            tl.circle(50,24)
            if not circle:
                tl.pencolor('white')
                tl.circle(3)
        circle = True
    
    screen.exitonclick()



screen.onkey(run, "r")
screen.listen()
screen.mainloop()
