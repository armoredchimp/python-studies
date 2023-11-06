from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        # self.attempts = attempts
        self.screen.tracer(0)
        self.pen = Turtle()
        self.pen.hideturtle()
        self.level_text()

    def level_text(self):
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(-260, 280)
        self.pen.color('black')
        self.pen.pendown()
        self.pen.write(f'Level: {self.level}', font=FONT, align="left")
        self.screen.update()

    # def attempts(self):
    #     self.pen.penup()
    #     self.pen.goto(0, 280)
    #     self.pen.pendown()
    #     self.pen.write(f'Attempts: {self.attempts}', font=FONT, align="right")
    #     self.screen.update()

    def clear(self):
        self.pen.clear()

# class GameOver(Turtle):
#     def __init__(self, scoreValue):
#         super().__init__()
#         self.score = scoreValue
#         self.color('blue')
#         self.penup()
#         self.goto(-100, 150)
#         self.pendown()
#         self.write("GAME OVER", font=("Arial", 40, "normal"), align="center")
#         self.penup()
#         self.goto(-100, 50)
#         self.color('white')
#         self.pendown()
#         self.write(f"Your score was {self.score}", font=(
#             "Arial", 20, 'normal'), align="center")
#         self.hideturtle()
