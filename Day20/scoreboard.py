from turtle import Turtle
import snake_file as snkf
with open('data.txt', mode='r') as file:
    high_score = int(file.read())


class StaticBoard():
    def __init__(self):
        self.createText()
        self.createLine()

    def createText(self):
        self.pen = Turtle()
        self.pen.color('white')
        self.pen.penup()
        self.pen.goto(-10, 280)
        self.pen.pendown()
        self.pen.write("Current Score: ", font=(
            "Arial", 12, "normal"), align="center")
        self.pen.hideturtle()

    def createLine(self):
        self.line = Turtle()
        self.line.color('white')
        self.line.penup()
        self.line.goto(-300, 270)
        self.line.pendown()
        self.line.goto(300, 270)
        self.line.hideturtle()

    # def clear(self):
    #     self.pen.clear()
    #     self.line.clear()


class DynamicScore(Turtle):
    def __init__(self, scoreValue):
        super().__init__()
        self.score = scoreValue
        self.color('green')
        self.penup()
        self.goto(70, 280)
        self.pendown()
        self.write(f"{self.score}", font=(
            "Arial", 12, "normal"), align="right")
        self.hideturtle()

    def clear(self):
        super().clear()


class GameOver(Turtle):
    def __init__(self, scoreValue):
        super().__init__()
        self.score = scoreValue
        self.high_score = high_score
        if (self.score > self.high_score):
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.color('blue')
        self.penup()
        self.goto(-100, 150)
        self.pendown()
        self.write("GAME OVER", font=("Arial", 40, "normal"), align="center")
        self.penup()
        self.goto(-100, 50)
        self.color('white')
        self.pendown()
        self.write(f"Your score was {self.score}, the high score is {self.high_score}", font=(
            "Arial", 14, 'normal'), align="center")
        self.hideturtle()
