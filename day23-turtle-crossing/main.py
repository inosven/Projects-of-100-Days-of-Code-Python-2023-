import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
car_manager = CarManager()
scoreboard = Scoreboard()
refresh_interval = 0.1
screen.listen()
screen.onkey(fun=player.move, key="Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    # detect collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update()
screen.exitonclick()
