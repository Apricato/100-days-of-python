from turtle import Turtle, Screen


Crush = Turtle()

for i in range (15):
    Crush.forward(10)
    Crush.penup()
    Crush.forward(10)
    Crush.pendown()


screen= Screen()
screen.exitonclick()