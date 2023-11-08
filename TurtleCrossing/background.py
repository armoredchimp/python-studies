from turtle import Turtle


class Background():
    def __init__(self, screen):
        self.screen = screen
        self.screen.tracer(0)
        self.draw_rectangle("green", -310, -300, 600, 30)
        self.draw_rectangle("black", -310, -270, 600, 560)
        self.draw_rectangle("grey", -310, 10, 600, 10)
        self.draw_rectangle("green", -310, 280, 600, 20)

    def game_end(self):
        self.draw_rectangle("black", -310, -300, 600, 20)
        self.draw_rectangle("black", -310, 280, 600, 20)

    def draw_rectangle(self, color, start_x, start_y, width, height):
        t = Turtle()
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()
        t.hideturtle()
