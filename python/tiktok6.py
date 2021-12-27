import turtle
from turtle import Screen, Turtle
screen = Screen()
screen.colormode(255)
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
tl = Turtle()
tl.speed(0)
tl.hideturtle()
for i in range(255):
    tl.pencolor((i,i,i))
    tl.circle(i*2)
    tl.right(5)

screen.exitonclick()