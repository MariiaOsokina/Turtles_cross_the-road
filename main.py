import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard=Scoreboard()

screen.listen()
player = Player()
car_manager=CarManager()


screen.onkey(player.move_up,"Up")
#Ask Anton why we don't use paratheses. Because we use method inside the listener, otherwise we will trigler it at the point
#We need it only then the UP key is detected.


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()
    for car in car_manager.all_cars:
        if player.distance(car) <20:
            scoreboard.game_over()
            game_is_on = False
    if player.is_it_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.increase_speed()

screen.exitonclick()
