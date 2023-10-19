from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


def createSnake(n):
    x = 0
    for _ in range(n):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.speed(0)
        turtle.goto(x, 0)
        x -= 20


createSnake(10)
screen.exitonclick()
