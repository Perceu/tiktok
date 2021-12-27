from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=1.0, height=1.0)
turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()
count = 1
turtle.left(90)
def desenhar_arvore(tm_tronco):
    if tm_tronco < 5:
        turtle.color("pink")
        turtle.circle(3)
        turtle.color("black")
        return 
    else:       
        turtle.forward(tm_tronco)
        turtle.left(30)
        desenhar_arvore((tm_tronco*2)/3)
        turtle.right(60)
        desenhar_arvore((tm_tronco*2)/3)
        turtle.left(30)
        turtle.backward(tm_tronco)
desenhar_arvore(100)
screen.exitonclick()