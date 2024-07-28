from turtle import Turtle,Screen
import random


screen= Screen()
screen.colormode(255)
A_Turtle = Turtle()
directions= [0,90,180,270]
A_Turtle.pensize(15)
A_Turtle.speed("fastest")


def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb =(r,g,b)
    return rgb

for i in range (100):
    A_Turtle.color(random_colour())
    A_Turtle.setheading(random.choice(directions))
    A_Turtle.forward(30)



#screen= Screen()

screen.exitonclick()