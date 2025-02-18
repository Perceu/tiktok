from PIL import Image
from turtle import Turtle
from functions import setupScreen
import colorsys


screen = setupScreen(576, 1024)
tl = Turtle()
tl.speed(0)
tl._tracer(2)
tl.hideturtle()

def fn(x):
    return 255 if x > thresh else 0

img = Image.open(r"./python_turtle/images/cristo.jpg")
thresh = 200
result_image = img.convert("L").point(fn, mode="1")
result_image = result_image.rotate(180)

def run():
    tl.pencolor('white')
    h=0.0
    for i in range(700):
        tl.penup()
        tl.pencolor('black')
        tl.goto(0,0)
        tl.forward(i)
        tl.rt(120)
        color = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.003
        for i in range(7):
            tl.pendown()
            tl.color(int(color[0]*255), int(color[1]*255), int(color[2]*255))
            tl.fd(30)
            tl.rt(143)


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
