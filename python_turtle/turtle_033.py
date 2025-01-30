from turtle import Turtle
from functions import setupScreen
from functions import triangle, triangle_l
from faker import Faker
from random import randint, choice

screen = setupScreen(580, 1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
fake = Faker()
Faker.seed(0)


def reset(turtle):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.pencolor(fake.hex_color())
    turtle.pendown()


def run():
    tl.pencolor("white")
    up_down = randint(-1, 1)
    left_right = randint(-1, 1)

    for _ in range(5000):
        if tl.xcor() > 300:
            reset(tl)
            up_down = randint(-1, 1)
            left_right = randint(-1, 1)

        if tl.xcor() < -300:
            reset(tl)
            up_down = randint(-1, 1)
            left_right = randint(-1, 1)

        if tl.ycor() < -500:
            reset(tl)
            up_down = randint(-1, 1)
            left_right = randint(-1, 1)

        if tl.ycor() > 500:
            reset(tl)
            up_down = randint(-1, 1)
            left_right = randint(-1, 1)

        if randint(0, 1):
            triangle_l(tl, 20)
        else:
            triangle(tl, 20)

        if left_right == 0:
            left_right = randint(-1, 1)

        if up_down == 0:
            up_down = randint(-1, 1)

        tl.forward(20 * left_right)

        if randint(0, 1):
            tl.setheading(choice([60, 120, 240]) * up_down)

    screen.exitonclick()


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
