import turtle

turtle.speed(5)
turtle.bgcolor("black")

for i in range(7):
    for colours in ["red", "blue", "yellow", "orange", "green", "white"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
