from turtle import Turtle, Screen
import random

Tortuga = Turtle ( )
screen = Screen ()
screen.setup(width = 500,height = 400) #keyword arguments are easier to understan dand we want easy to understand code regardless. Clean code practice 
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race ? Enter a color :")
colors = ["red", "blue","yellow","green","purple","orange"]
y_positions = [ -70, -40 , -10 ,20,50,80]
all_turtles=[]


for turtle_index in range (0,6):
    turtle = Turtle(shape ="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230 , y= y_positions[turtle_index])
    all_turtles.append(turtle)



if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print ( f"You've lost ! The {winning_color} tirtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
