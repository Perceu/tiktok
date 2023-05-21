from turtle import Turtle
from functions import setupScreen

screen  = setupScreen(580,1280)

turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()
turtle.pencolor('white')

def run():
    for i in range(1000):
        turtle.forward(i*0.5)
        turtle.right(40)

screen.onkey(run, "r")
screen.listen()
screen.mainloop()