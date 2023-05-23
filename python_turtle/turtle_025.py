from random import randint
from turtle import Turtle
from faker import Faker
from functions import setupScreen

screen = setupScreen(580,1280)
tl = Turtle()
tl.speed(0)
# tl.hideturtle()
tl.pencolor('white')
fake = Faker()
Faker.seed(0)
tl.hideturtle()
def draw_form(turtle, size):
    distance = size//2
    if distance < 25:
        return 

    turtle.back(size/2)
    turtle.left(90)
    turtle.back(size/2)
    turtle.left(90)
    draw_form(turtle, distance)
    turtle.right(90)
    turtle.fd(size)
    turtle.back(size/2)
    turtle.left(90)
    draw_form(turtle, distance)
    turtle.right(90)
    turtle.right(90)   
    turtle.fd(size)   
    turtle.left(90)
    turtle.back(size/2)
    turtle.left(90)
    draw_form(turtle, distance)
    turtle.right(90)
    turtle.fd(size)
    turtle.back(size/2)
    turtle.left(90)
    draw_form(turtle, distance)
    turtle.right(90)
    turtle.right(90)
    turtle.back(size/2)


def run():
    tl.left(90)
    draw_form(tl, 600)

screen.onkey(run, "r")
screen.listen()
screen.mainloop()