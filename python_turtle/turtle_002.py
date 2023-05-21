from turtle import Turtle
from functions import setupScreen

screen  = setupScreen(580,1280)

turtle = Turtle()
turtle.speed(0)
turtle.pencolor('white')
turtle.hideturtle()

def run():
    for i in range(500):
        turtle.right(5)
        turtle.forward((10+i)*2)
        turtle.right(90)

screen.onkey(run, "r")
screen.listen()
screen.mainloop()