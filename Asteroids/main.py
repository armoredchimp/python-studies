import turtle as Turtle
from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player(screen)
screen.onkey(key="a", fun=player.move_left)
screen.onkey(key="w", fun=player.move_forward)
screen.onkey(key="d", fun=player.move_right)
screen.onkey(key="space", fun=player.shoot)

screen.exitonclick()
