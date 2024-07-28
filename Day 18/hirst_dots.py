from turtle import Turtle, Screen
import random
#requirements 10 x 10 rows of spots. 20 in side and 50 paces in between them dots
screen = Screen()
Tortuga = Turtle()
screen.colormode(255)

color_list= [(5,196,178),(48,100,26),(1,58,145),(247,207,32),(235,65,6),(248,181,212),(189,0,32),(76,144,225),(123,18,23),(130,21,112),(245,163,1),(1,128,207)]

Tortuga.penup()
Tortuga.speed("fastest")
Tortuga.hideturtle()
Tortuga.setposition(-300,-200)
for i in range (10):

    for i in range (10):
        Tortuga.dot(20, random.choice(color_list))
        Tortuga.forward(50)
    Tortuga.setheading(90)
    Tortuga.forward(50)
    Tortuga.setx(-300)
    Tortuga.setheading(0)

        
screen.exitonclick()
