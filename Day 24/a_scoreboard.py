from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scoreboard.txt") as high_text:
            self.high_score = int(high_text.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}" ,align=ALIGNMENT, font=FONT)


    def reset_scoreboard(self):
        if self.score > self.high_score :
            self.high_score = self.score

            with open('scoreboard.txt', mode = "w") as highest_text:
                highest_text.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()



    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
