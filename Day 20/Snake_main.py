from turtle import Screen , Turtle 
from create_snake import Snake
import time

screen = Screen()
screen.setup(width= 600, height= 600)

screen.bgcolor("black")
screen.title("Nokia snakey")
screen.tracer(0)

starting_positions= [(0,0),(-20,0), (-40,0)]
segments= []

for turtle in range (3):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.setpos(starting_positions[turtle])
    segments.append(segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range (2,0,-1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x ,new_y)
    seg_num[0].forwards(20)

    
        



screen.exitonclick()