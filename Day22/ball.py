from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.down = False
        self.left = False

    def move(self):
        if self.down == False:
            if self.left == False:
                new_x, new_y = self.xcor()+10, self.ycor()+10
            else:
                new_x, new_y = self.xcor()-10, self.ycor()+10
        else:
            if self.left == False:
                new_x, new_y = self.xcor()+10, self.ycor()-10
            else:
                new_x, new_y = self.xcor()-10, self.ycor()-10
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0, 0)
        self.left = random.choice([True, False])
        time.sleep(3)
