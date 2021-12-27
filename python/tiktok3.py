from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=1.0, height=1.0)

turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()

for i in range(1000):
    turtle.right(5)
    turtle.forward(i*0.5)
    turtle.right(47)

screen.exitonclick()