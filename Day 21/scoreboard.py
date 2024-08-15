from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Courier",24,"normal")

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.color ("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        
    
    def game_over(self):
        self.goto(0,0)
        self.write ("GAME OVER ",  align = "center", font = ("Arial",24,"normal"))
    
    def update_scoreboard(self):
        self.write (f"Score: {self.score_count}", align = "center", font = ("Arial",24,"normal"))
       
    def score_up(self):
        self.score_count += 1
        self.clear()
        self.update_scoreboard()


