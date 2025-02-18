from PIL import Image
from turtle import Turtle
from functions import setupScreen
import colorsys


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
    h=0.0
    for i in range(800):
        h += 0.003
        color = colorsys.hsv_to_rgb(h, 1, 1)
        tl.pencolor(int(color[0]*255), int(color[1]*255), int(color[2]*255))
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
