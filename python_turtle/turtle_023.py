from turtle import Turtle
from faker import Faker
from functions import setupScreen, square, square_l

screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
fake = Faker()
Faker.seed(0)

def run():
    tl.pencolor('white')
    for i in range(2,600,4):
        tl.penup()
        tl.back(i//2)
        tl.pendown()
        square(tl, i)
        tl.penup()
        tl.forward(i//2)
        tl.pendown()
    tl.pencolor('red')
    for i in range(2,600,4):
        tl.penup()
        tl.back(i//2)
        tl.pendown()
        square_l(tl, i)
        tl.penup()
        tl.forward(i//2)
        tl.pendown()


screen.onkey(run, "r")
screen.listen()
screen.mainloop()