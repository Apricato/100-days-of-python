from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800 ,height= 600)
screen.title("PING PONG")
screen.listen()
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_paddle.down , "Down")
screen.onkey(left_paddle.down , "s")
screen.onkey(right_paddle.up,"Up")
screen.onkey(left_paddle.up,"w")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    


  #Detect collision with the upper and lower 
  
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

  #Detect collision with both paddles

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() and ball.xcor() > - 320 :
      ball.bounce_x()


#Detect R paddle misses
    if ball.xcor() > 380 :
       ball.reset_ball()
       scoreboard.l_point()

#Detect L paddle misses
    if ball.xcor() < -380 : 
        ball.reset_ball()
        scoreboard.r_point()





screen.exitonclick()
