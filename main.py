import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_Manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.move_forward, key='Up')
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_Manager.create_cars()
    car_Manager.move_cars()

    for car in car_Manager.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_Manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()
