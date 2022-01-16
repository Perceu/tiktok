from turtle import Turtle
from functions import setupScreen, circle_coordenates
screen  = setupScreen(720,1280, color="#0073e5")
tl = Turtle()
tl.speed(0)
tl.hideturtle()
def run():
    coords = circle_coordenates(tl, 300)
    tl.color('#f5f5f5')
    meio = int(len(coords)/2)

    pos = 0
    tl.goto(coords[pos][0],coords[pos][1])
    tl.pendown()
    for c in coords[meio::]:
        tl.goto(c[0],c[1])
        pos +=2
        if pos>179:
            pos=0
        tl.goto(coords[pos][0],coords[pos][1])

    tl.color('#000000') 
    pos = meio
    tl.goto(coords[pos][0],coords[pos][1])
    for c in coords[0:meio:]:
        tl.goto(c[0],c[1])
        pos +=2
        if pos>179:
            pos=0
        tl.goto(coords[pos][0],coords[pos][1])
    screen.exitonclick()

screen.onkey(run, "r")
screen.listen()
screen.mainloop()