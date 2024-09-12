from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.starting_point()

 
    
    def avance(self):
        if self.ycor() < FINISH_LINE_Y :
         self.forward(MOVE_DISTANCE)
        
        else:
           self.starting_point()
    
    def starting_point(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
  


       


        

