from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.down = False

    def move(self):
        if self.down == False:
            new_x, new_y = self.xcor()+10, self.ycor()+10
        else:
            new_x, new_y = self.xcor()-10, self.ycor()-10
        self.goto(new_x, new_y)
