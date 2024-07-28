from turtle import Turtle, Screen
#import and module name

Crush = Turtle()
#Crush.shape("circle")
Crush.color("blue")

for i in range(4):
    Crush.forward(100)
    Crush.right(90)


#keep at the very bottom, 
screen = Screen()
screen.exitonclick()

