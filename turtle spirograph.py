import turtle
import random


screen = turtle.Screen()
bob = turtle.Turtle()
screen.bgcolor("black")
bob.pencolor("cyan")
bob.speed(100)
def crazy(var1):
  for i in range(360):
      bob.forward(i)
      bob.left(var1)
crazy(50)
