from turtle import Turtle
from functions import setupScreen, gradient_color, format_color
screen  = setupScreen(720,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
def run():
    tl.pencolor('white')
    for i in range(5):
        tl.back(100)
        tl.left(170)

    screen.exitonclick()
screen.onkey(run, "r")
screen.listen()
screen.mainloop()