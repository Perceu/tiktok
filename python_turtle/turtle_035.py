from PIL import Image
from turtle import Turtle
from functions import setupScreen

screen = setupScreen(576, 1024)
tl = Turtle()
tl.speed(0)
tl._tracer(10)
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
    for i in range(result_image.width-1, 0, -3):
        for j in range(result_image.height-1, 0, -3):
            if result_image.getpixel((i, j)) < 255:
                tl.goto((i-300, j-300))
                tl.pendown()
                tl.goto((i-299, j-299))
                tl.penup()

    screen.exitonclick()


screen.onkey(run, "r")
screen.listen()
screen.mainloop()
