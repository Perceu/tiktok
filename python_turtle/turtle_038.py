from PIL import Image
from turtle import Turtle
from functions import setupScreen
import colorsys


screen = setupScreen(576, 1024)
tl = Turtle()
tl.speed(3)
tl._tracer(2)
# tl.hideturtle()
colors = ["orange", "white"]

def run():
    for j in range(-1, 2, 1):
        tl.penup()
        print(j)
        tl.setpos(-60, (j * -400))
        tl.setheading(0)
        print(tl.position())
        tl.pendown()
        for i in range(150):
            tl.pencolor(colors[i % 2])
            tl.rt(i)
            tl.circle(120, i)
            tl.penup()
            tl.fd(i + 60)
            tl.pendown()
            tl.rt(90)
            tl.fd(i - 75)


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
