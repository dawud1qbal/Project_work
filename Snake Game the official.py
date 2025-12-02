import turtle
import time



WIDTH = 500
HEIGHT = 500
SNAKE_CELL_SIZE = 20
FOOD_SIZE = 10
SQUARE_SIZE = 20
DELAY = 0.5 # MILLISECONDS


def move_snake(): 
    if head.direction == "up":
        head.sety(head.ycor() + SNAKE_CELL_SIZE)
    elif head.direction == "right":
        head.setx(head.xcor() + SNAKE_CELL_SIZE)
    elif head.direction == "down":
        head.sety(head.ycor() - SNAKE_CELL_SIZE)
    elif head.direction == "left":
        head.setx(head.xcor() - SNAKE_CELL_SIZE)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"
        
        
# Set up screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")



# Snake head
head  = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(100, 100)

hide.directions = "up"

while True:
    screen.update()
    move_snake()
    time.sleep(DELAY)


turtle.done()


