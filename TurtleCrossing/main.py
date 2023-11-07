import time
from turtle import Screen
from player import Player
import car_manager as CM
from scoreboard import Scoreboard, GameOver
from background import Background


def setup_game():
    global player, car_manager, screen, ticker, level, sb
    screen.tracer(0)
    screen.listen()
    ticker = 0
    player = Player()
    if 'sb' in globals() and game_is_on:
        sb.clear()
        sb = Scoreboard(screen, level)
    else:
        sb = Scoreboard(screen, level)
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
    global game_is_on, level, ticker_max, score, attempts, sb

    while game_is_on:
        car_interval()
        car_manager.move_all_cars()
        sb.score_clear()
        sb.score_text(score, attempts)
        if car_manager.detect_collision():
            attempts += 1
            score -= 10
            if attempts >= 2:
                game_is_on = False
                sb.clear()
                player.goto(600, 680)
                bg.game_end()
                gmov = GameOver(score)
                player.color('black')
            else:
                player.goto(0, -280)
                sb.score_clear()
        if player.finish_line():
            score += 100
            attempts = 0
            sb.score_clear()
            sb.score_text(score, attempts)
            level += 1
            ticker_max -= 1
            setup_game()
        time.sleep(0.05)
        screen.update()


ticker_max = 15
level = 1
score = 0
attempts = 0
screen = Screen()
screen.setup(width=600, height=600)
bg = Background(screen)
setup_game()
game_is_on = True
game()


screen.exitonclick()
#
