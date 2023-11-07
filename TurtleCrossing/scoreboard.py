from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard:
    def __init__(self, screen, level):
        self.screen, self.level = screen, level
        self.screen.tracer(0)
        self.pen = Turtle()
        self.right_pen = Turtle()
        self.pen.hideturtle()
        self.right_pen.hideturtle()
        self.level_text()

    def level_text(self):
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(-260, 280)
        self.pen.color('black')
        self.pen.pendown()
        self.pen.write(f'Level: {self.level}', font=FONT, align="left")
        self.screen.update()

    def score_text(self, score, attempts):
        self.score, self.attempts = score, attempts
        self.right_pen.penup()
        self.right_pen.goto(180, 280)
        self.right_pen.color('black')
        self.right_pen.pendown()
        self.right_pen.write(
            f'Score: {self.score}     Attempts: {self.attempts}', font=FONT, align="right")

    def clear(self):
        self.pen.clear()
        self.right_pen.clear()

    def score_clear(self):
        self.right_pen.clear()


class GameOver(Turtle):
    def __init__(self, scoreValue):
        super().__init__()
        self.score = scoreValue
        self.color('blue')
        self.penup()
        self.goto(-100, 150)
        self.pendown()
        self.write("GAME OVER", font=("Arial", 40, "normal"), align="center")
        self.penup()
        self.goto(-100, 50)
        self.color('white')
        self.pendown()
        self.write(f"Your score was {self.score}", font=(
            "Arial", 20, 'normal'), align="center")
        self.hideturtle()
