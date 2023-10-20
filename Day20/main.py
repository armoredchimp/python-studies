from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segments = []


def createSnake(n):
    x = 0
    for _ in range(n):
        turtle = Turtle('square')
        turtle.color('white')
        # turtle.speed(0)
        turtle.penup()
        turtle.goto(x, 0)
        x -= 20
        segments.append(turtle)


createSnake(10)

gameActive = True
for _ in range(0, 20):
    screen.update()
    time.sleep(0.1)

    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()
