from turtle import Turtle, Screen
import random

Crush = Turtle()
colors = ["blue","red","green","purple","pink","gray","black"]

for i in range (3,10):
    degrees = 360 /i
    Crush.pencolor(random.choice(colors))
    for j in range (i):
        Crush.forward(100)
        Crush.right(degrees)





pantalla = Screen()
pantalla.exitonclick()
