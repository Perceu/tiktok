from turtle import Turtle
from functions import setupScreen
from faker import Faker

screen = setupScreen(576, 1024)
tl = Turtle()
tl.speed(10)
tl.hideturtle()
fake = Faker()
Faker.seed(0)


def run():
    tl.pencolor("white")

    for i in range(1, 26):
        tl.pendown()
        tl.circle(40, 180)
        tl.circle(-40, 180)
        tl.circle(40, 180)
        tl.circle(-40, 180)
        tl.penup()
        tl.goto(0, 0)
        tl.setheading(15 * i)

    tl.penup()
    tl.goto(0, 0)
    tl.setheading(90)
    tl.pendown()

    for i in range(1, 26):
        tl.pendown()
        tl.circle(-40, 180)
        tl.circle(40, 180)
        tl.circle(-40, 180)
        tl.circle(40, 180)
        tl.penup()
        tl.goto(0, 0)
        tl.setheading(15 * i)

    screen.exitonclick()


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
