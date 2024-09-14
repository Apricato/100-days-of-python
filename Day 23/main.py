import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tortuga = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(tortuga.avance , "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision

    for car in car_manager.all_cars:
        if car.distance(tortuga) < 20:
            game_is_on = False
            scoreboard.game_over()
            tortuga.starting_point()
    
    #detect succesful crossing
    if tortuga.ycor() > 280 :
        tortuga.starting_point()
        car_manager.level_up()
        scoreboard.update_scoreboard()




screen.exitonclick()


