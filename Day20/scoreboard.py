from turtle import Turtle
import snake_file as snkf


class StaticBoard():
    def __init__(self):
        self.createText()
        self.createLine()

    def createText(self):
        pen = Turtle()
        pen.color('white')
        pen.penup()
        pen.goto(-10, 280)
        pen.pendown()
        pen.write("Current Score: ", font=(
            "Arial", 12, "normal"), align="center")
        pen.hideturtle()

    def createLine(self):
        line = Turtle()
        line.color('white')
        line.penup()
        line.goto(-300, 270)
        line.pendown()
        line.goto(300, 270)
        line.hideturtle()


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
