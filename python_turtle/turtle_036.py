from PIL import Image
from turtle import Turtle
from functions import setupScreen

screen = setupScreen(576, 1024)
tl = Turtle()
tl.speed(0)
tl._tracer(5)
tl.hideturtle()

def fn(x):
    return 255 if x > thresh else 0

img = Image.open(r"./python_turtle/images/cristo.jpg")
thresh = 200
result_image = img.convert("L").point(fn, mode="1")
result_image = result_image.rotate(180)



def run():
    tl.pencolor('white')
    tl.penup()
    tl.fillcolor('black')
    for i in range(700):
        tl.up()
        tl.circle(i, 45)
        tl.down()
        tl.begin_fill()
        tl.circle(40, 145)
        tl.left(80)
        tl.circle(40, 145)
        tl.end_fill()

screen.onkey(run, "r")
screen.listen()
screen.mainloop()
