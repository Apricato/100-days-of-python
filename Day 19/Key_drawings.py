from turtle import Turtle,Screen

Arrow = Turtle()
screen = Screen()

def forwards():
    Arrow.forward(30)
def backwards():
    Arrow.backward(30)

def counter_clockwise():
    Arrow.right(20)

def clockwise():
    Arrow.left(20)

def clear():
    Arrow.penup()
    Arrow.clear()
    Arrow.home()
    Arrow.pendown()

screen.listen()
screen.onkey( key = "w", fun = forwards)
screen.onkey( key = "s", fun = backwards)
screen.onkey( key = "d", fun = clockwise)
screen.onkey( key = "a", fun = counter_clockwise)
screen.onkey(key = "c", fun =  clear)


screen.exitonclick()