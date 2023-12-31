from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()


class Snake:
    def __init__(self, game_instance):
        self.segments = []
        self.game = game_instance

    def create(self, n):
        x = 0
        for _ in range(n):
            turtle = Turtle('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(x, 0)
            x -= 20
            self.segments.append(turtle)
            screen.update()

    def add_segment(self):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        last_segment = self.segments[-1]
        turtle.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(turtle)
        screen.update()

    def move(self):
        screen.update()
        time.sleep(0.08)
        food_x, food_y = self.game.food_coords[0], self.game.food_coords[1]
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.food_collision(food_x, food_y)
        self.snake_collision()
        self.wall_collision(self.segments[0].xcor(), self.segments[0].ycor())

    def food_collision(self, x, y):
        if abs(self.segments[0].xcor() - x) < 20 and abs(self.segments[0].ycor() - y) < 20:
            self.game.add_point()
            self.game.create_food()
            self.add_segment()

    def snake_collision(self):
        head_x, head_y = self.segments[0].xcor(), self.segments[0].ycor()
        for seg in self.segments[1:]:
            seg_x, seg_y = seg.xcor(), seg.ycor()
            if abs(head_x - seg_x) < 10 and abs(head_y - seg_y) < 10:
                self.game.active = False
                self.clear_snake()
                screen.update()
                self.game.print_score()
                return

    def wall_collision(self, x, y):
        if (x >= 300 or x <= -300) or (y >= 270 or y <= -300):
            self.game.active = False
            self.clear_snake()
            screen.update
            self.game.print_score()
            return

    def turn_left(self):
        self.segments[0].left(90)
        self.move()

    def turn_right(self):
        self.segments[0].right(90)
        self.move()

    def clear_snake(self):
        for segment in self.segments:
            segment.hideturtle()
            segment.clear()
