import turtle
import turtle
turtle.shape("turtle")
turtle.setup(500, 500)

turtle.penup()
turtle.Screen().bgcolor("blue")



# WINDOW SETUP
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("TURTLE RACE", font=("Arial", 30, "bold"))
turtle.penup()



# DIRT
turtle.setpos(-400, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
forward(300)
end_fill()


# FINISH LINE
stamp_size = 20
square_size = 15
finish_line = 200


turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()



for i in range (10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()


for j in range (10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()








