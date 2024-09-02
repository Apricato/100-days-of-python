from turtle import Turtle

class Paddle (Turtle):
    def __init__(self,position):
        super().__init__()
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.shape("square")
        self.goto(0,0)
        self.color("white")
        self.goto(position)
    
    def up (self): #methods always have a first attribute as the self 
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

   
