import time
from turtle import Screen
from player import Player
import car_manager as CM
from scoreboard import Scoreboard


def setup_game():
    global player, car_manager, screen, ticker, level
    screen.tracer(0)
    screen.listen()
    ticker = 0
    player = Player()
    if 'car_manager' in globals():
        car_manager.clear_all_cars()
    car_manager = CM.CarManager(player, screen, level)
    screen.onkey(key="a", fun=player.move_left)
    screen.onkey(key="w", fun=player.move_up)
    screen.onkey(key="d", fun=player.move_right)
    screen.onkey(key="s", fun=player.move_down)


def car_interval():
    global ticker, ticker_max
    ticker += 1
    if ticker == ticker_max:
        car_manager.build_car()
        ticker = 0


def game():
    global game_is_on, level, ticker_max
    while game_is_on:
        car_interval()
        car_manager.move_all_cars()
        car_manager.detect_collision()
        if player.finish_line():
            level += 1
            ticker_max -= 1
            setup_game()
        time.sleep(0.05)
        screen.update()


ticker_max = 15
level = 1
screen = Screen()
screen.setup(width=600, height=600)
setup_game()
game_is_on = True
game()


#
