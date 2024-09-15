import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./Day 25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

class MapText(turtle.Turtle):
    def __init__ (self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
    
    def write_map (self,x,y,answer_state):
        self.goto(x,y)
        self.write(f"{answer_state}",align ="center",font =("Arial",12,"normal"))



data_states = pandas.read_csv("./Day 25/day-25-us-states-game-start/50_states.csv") #no difference between backa¿lash or the other slash in python
all_states = data_states.state.to_list()
guessed_states = []

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 states correct", prompt = " What's another state's name?").title() #gives back capitalized the letter
    if answer_state == "Exit":
        missing = []
        for state in all_states:
            if state not in guessed_states:
                missing.append(state)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = MapText()
        row = data_states[data_states.state == answer_state] #pulls out th entire row with all the stuff it has 
        state.write_map(int(row.x.item()),int(row.y.item()),answer_state)






#screen.exitonclick()

'''
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
'''
