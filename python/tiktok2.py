from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=1.0, height=1.0)

turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()

for i in range(500):
    turtle.right(5)
    turtle.forward((10+i)*2)
    turtle.right(90)

screen.exitonclick()