from turtle import Screen , Turtle 
from create_snake import Snake
from scoreboard import Scoreboard
from food import Food
import time



screen = Screen()
screen.setup(width= 600, height= 600)



screen.bgcolor("black")
screen.title("Nokia snakey")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.score_up()


    #Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detect collison with head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()
    #if the head colides with the head:
    


    




   