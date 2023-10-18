import random
from turtle import Turtle, Screen

screen = Screen()
screen.listen()
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']


class RaceTurtle(Turtle):
    def __init__(self, number, x, y):
        super().__init__()
        self.number = number
        self.shape('turtle')
        self.speed(0)
        color = random.choice(colors)
        self.color(color)
        colors.remove(color)
        self.penup()
        self.setpos(x, y)


turtles = []


def assign_turtles(n):
    x = -(screen.window_width() // 2 - 100)
    y = -(screen.window_height() // 2 - 100)
    while n > 0:
        turtles.append(RaceTurtle(n, x, y))
        y += 150
        n -= 1


assign_turtles(6)


def start_race():
    finish_line = screen.window_width() // 2 - 100
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(0, 15))
            if turtle.xcor() >= finish_line:
                print(f"Turtle {turtle.color()[0]} {turtle.number} wins!")
                return


screen.onkey(key="space", fun=start_race)
screen.exitonclick()
