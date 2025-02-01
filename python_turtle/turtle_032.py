from turtle import Turtle
from functions import setupScreen
from faker import Faker

screen = setupScreen(576, 1024)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
fake = Faker()
Faker.seed(0)


def run():
    tl.pencolor("white")

    for i in range(1, 121):
        tl.penup()
        tl.goto(0, 0)
        tl.setheading(3 * i)
        tl.pendown()
        for i in range(8):
            tl.circle(10, 180)
            tl.circle(-10, 180)

    tl.penup()
    tl.goto(0, 0)
    tl.setheading(90)
    tl.pendown()

    for i in range(1, 121):
        tl.penup()
        tl.goto(0, 0)
        tl.setheading(3 * i)
        tl.pendown()
        tl.forward(1000)

    screen.exitonclick()


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
