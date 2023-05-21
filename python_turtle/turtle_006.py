from turtle import Turtle
from functions import setupScreen

screen = setupScreen(580,1280)

tl = Turtle()
tl.speed(0)
tl.hideturtle()

def run():
    for i in range(255):
        tl.pencolor((i,i,i))
        tl.circle(i*2)
        tl.right(5)

screen.onkey(run, "r")
screen.listen()
screen.mainloop()