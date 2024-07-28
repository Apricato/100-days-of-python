from turtle import Turtle,Screen
import random

A_Turtle = Turtle()
colors = ["PeachPuff2","PeachPuff3","firebrick1","sienna4","gold","dark orange","bisque2","OrangeRed2","bisque3","orange","gold2"]
directions= [0,90,180,270]
A_Turtle.width(20)



for i in range (100):
    A_Turtle.pencolor(random.choice(colors))
    A_Turtle.setheading(random.choice(directions))
    A_Turtle.forward(30)



screen= Screen()
screen.exitonclick()