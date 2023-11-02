import time
from turtle import Screen
from player import Player
import car_manager as CM
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CM.CarManager()

ticker = 0


def car_interval():
    global ticker
    ticker += 1
    if ticker == 3:
        car_manager.build_car()
        ticker = 0


game_is_on = True
while game_is_on:
    car_interval()
    car_manager.move_all_cars()
    time.sleep(1.0)
    screen.update()
