from random import randint
from turtle import Turtle
from faker import Faker
from functions import setupScreen

screen  = setupScreen(720,1280)
tl = Turtle()
tl.speed(0)
tl.hideturtle()
fake = Faker()
Faker.seed(0)

def run():
    left = 1
    for _ in range(360):
        tl.pencolor(fake.hex_color())
        tl.penup()
        tl.goto(0,0)
        tl.setheading(90)
        tl.left(left)
        left += 1
        tl.pendown()
        for size in range(50):
            tl.left(5)
            tl.forward(size)



screen.onkey(run, "r")
screen.listen()
screen.mainloop()