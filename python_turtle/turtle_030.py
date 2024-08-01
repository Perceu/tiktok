from turtle import Turtle
from functions import setupScreen
from functions import star, get_color
from faker import Faker

screen = setupScreen(580, 1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
fake = Faker()
Faker.seed(0)


def run():
    circle_size = 2

    for _ in range(10):
        circle_size = 10
        for i in range(100):
            circle_size += 10
            tl.pencolor(fake.hex_color())
            star(tl, circle_size)
            tl.right(4)

    screen.exitonclick()


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
