import turtle


def drawBoard():

    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)


    num = 1
    for i in range(3):
      for j in ramge(3):
        drawer.penup()
        drawer.goto(-290 + j * 200, 280 - i * 200)
        drawer.pendown()


        drawer.write(num, font = ("Arial",12))
        num += 1





    
    for i in range(2):
      drawer.penup()
      drawer.goto(-100 + 200 * i, 300)
      drawer.pendown()
      drawer.forward(600)



def draw0(x, y):
    
  drawer.penup()
  drawer.goto(x, y + 75)
  drawer.pendown()

  drawer.setheading(60)

  for i in range(2):
    drawer.forward(75)
    drawer.backward(150)
    drawer.forward(75)
    drawer.left(60)


  screen.update()



def draw0(x, y):
    
  drawer.penup()
  drawer.goto(x, y + 75)
  drawer.pendown()
  

         



drawer = turtle.Turtle()


drawer.pensize(10)
drawer.ht()


screen = turtle.Screen()
screen.tracer(0)


drawBoard()


