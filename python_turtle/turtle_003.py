from turtle import Turtle
from functions import setupScreen

screen  = setupScreen(580,1280)

turtle = Turtle()
turtle.speed(0)
turtle.pencolor('white')
turtle.hideturtle()

def run():
    for i in range(1000):
        turtle.right(5)
        turtle.forward(i*0.5)
        turtle.right(47)

screen.onkey(run, "r")
screen.listen()
screen.mainloop()