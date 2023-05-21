from turtle import Turtle
from functions import setupScreen

screen = setupScreen(580,1280)

turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()
count = 1
turtle.left(90)

def run():
    desenhar_arvore(100)

def desenhar_arvore(tm_tronco):
    if tm_tronco < 5:
        turtle.color("pink")
        turtle.circle(3)
        turtle.color("white")
        return 
    else:       
        turtle.forward(tm_tronco)
        turtle.left(30)
        desenhar_arvore((tm_tronco*2)/3)
        turtle.right(60)
        desenhar_arvore((tm_tronco*2)/3)
        turtle.left(30)
        turtle.backward(tm_tronco)


screen.onkey(run, "r")
screen.listen()
screen.mainloop()