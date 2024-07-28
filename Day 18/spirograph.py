from turtle import Turtle,Screen
import random

Tortuga = Turtle()
Tortuga.speed("fastest")
colors = ["PeachPuff2","PeachPuff3","firebrick1","sienna4","gold","dark orange","bisque2","OrangeRed2","bisque3","orange","gold2"]

def draw_spirograph(size_of_gap):

    for i in range(int(360/ size_of_gap)): #even if divided cleanly it will need to be converted to integer since the type will be float
        Tortuga.color(random.choice(colors))
        Tortuga.circle(100)
        Tortuga.setheading(Tortuga.heading()+ size_of_gap)
        #Tortuga.home()


draw_spirograph(6)

screen = Screen()
screen.exitonclick()
