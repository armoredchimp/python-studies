from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
screen.listen()


class Paddle():
    def __init__(self, x):
        super().__init__()
        self.paddle = Turtle('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, 0)
        self.paddle.color('white')
        screen.update()

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)
        screen.update()

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
        screen.update()


paddleR = Paddle(350)
paddleL = Paddle(-350)
screen.onkey(paddleL.go_up, 'w')
screen.onkey(paddleL.go_down, 's')
screen.onkey(paddleR.go_up, 'Up')
screen.onkey(paddleR.go_down, 'Down')

screen.exitonclick()
