from turtle import Turtle


class Player(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape('triangle')
        self.color('black')
        self.penup()
        self.screen = screen
        self.goto(0, 0)
        self.speed(0)
        self.screen.update()
        self.screen.tracer(0)

    def move_forward(self):
        self.forward(10)
        self.screen.update()

    def move_left(self):
        self.lt(18)
        self.screen.update()

    def move_right(self):
        self.rt(18)
        self.screen.update()

    def shoot(self):
        laser = Turtle('square')
        laser.setheading(self.heading())
        laser.shapesize(stretch_wid=0.1, stretch_len=10)
        laser.penup()
        print(self.xcor(), self.ycor())
        laser.goto(self.xcor(), self.ycor())
        while -300 < laser.ycor() < 300 and -300 < laser.xcor() < 300:
            laser.forward(50)
        self.screen.update()
