import time
from turtle import Screen
from player import Player
import car_manager as CM
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CM.CarManager(player, screen)

ticker = 0


def car_interval():
    global ticker
    ticker += 1
    if ticker == 15:
        car_manager.build_car()
        ticker = 0


game_is_on = True
while game_is_on:
    car_interval()
    car_manager.move_all_cars()
    car_manager.detect_collision()
    player.finish_line()
    time.sleep(0.05)
    screen.update()
    screen.onkey(key="a", fun=player.move_left)
    screen.onkey(key="w", fun=player.move_up)
    screen.onkey(key="d", fun=player.move_right)
    screen.onkey(key="s", fun=player.move_down)
