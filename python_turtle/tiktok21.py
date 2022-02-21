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
    for _ in range(300):
        tl.pencolor(fake.hex_color())
        tl.penup()
        tl.goto(0,0)
        tl.pendown()
        for size in range(randint(15,50)):
            tl.left(randint(5,10))
            tl.forward(size)



screen.onkey(run, "r")
screen.listen()
screen.mainloop()