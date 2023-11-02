from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(-400, 270)
        self.pendown()
        self.goto(400, 270)
        self.hideturtle()


class PlayerScore(Turtle):
    def __init__(self, player, score):
        super().__init__()
        self.player = player
        self.score = score
        self.color('white')
        self.penup()
        if self.player == 'left':
            self.goto(-200, 280)
            self.write("Player 1 Score: ", font=(
                "Arial", 12, "normal"), align="right")
            self.goto(-160, 280)
        else:
            self.goto(200, 280)
            self.write("Player 2 Score: ", font=(
                "Arial", 12, "normal"), align="right")
            self.goto(240, 280)
        self.write(f"{self.score}", font=(
            "Arial", 12, "normal"), align="right")
        self.hideturtle()

    def clear(self):
        super().clear()
