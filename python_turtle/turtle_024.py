from turtle import Turtle
from functions import setupScreen

screen  = setupScreen(580,1280)

turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()
turtle.pencolor('white')
def run():
    for i in range(150):
        for r in range(8):
            turtle.left(360/8)
            if r%2:
                turtle.pencolor('white')
            else:
                turtle.pencolor('red')
            turtle.fd(4*i)
        turtle.penup()
        turtle.fd(4/2)
        turtle.right(90)
        turtle.fd(5)
        turtle.left(90)
        turtle.pendown()

screen.onkey(run, "r")
screen.listen()
screen.mainloop()