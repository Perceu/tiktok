from turtle import Screen, Turtle
from functions import setupScreen

screen  = setupScreen(580,1280)

turtle = Turtle()
turtle.goto(-100,100)
turtle.speed(0)
turtle.pencolor('white')
turtle.shape("turtle")
turtle.hideturtle()

def run():
    for i in range(100):
        turtle.right(5)
        turtle.forward(200)
        turtle.right(90)

screen.onkey(run, "r")
screen.listen()
screen.mainloop()