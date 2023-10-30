from turtle import Turtle


class Paddle():
    def __init__(self, x):
        super().__init__()
        self.paddle = Turtle('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, 0)
        self.default = (self.paddle.xcor(), self.paddle.ycor())
        self.paddle.color('white')

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def xcor(self):
        return self.paddle.xcor()

    def ycor(self):
        return self.paddle.ycor()

    def reset(self):
        self.paddle.goto(self.default)
