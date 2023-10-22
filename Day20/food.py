from turtle import Turtle
import random
import snake_file as snk


class Food(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.shape('circle')
        self.color('green')
        self.penup()
        self.goto(x, y)

    def clear(self):
        self.hideturtle()
