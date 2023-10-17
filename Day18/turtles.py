from turtle import Turtle, Screen
import random


timmy = Turtle()

screen = Screen()
timmy.shape("classic")
timmy.color("red")
# i = 4
# while i > 0:
#     timmy.forward(100)
#     timmy.right(90)
#     i -= 1
# j = 10
# while j > 0:
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     j -= 1
screen.colormode(255)

# p = 3
# while p < 100:
#     a = 360 / p
#     timmy.color(random.randint(0, 255), random.randint(
#         0, 255), random.randint(0, 255))
#     for _ in range(p):

#         timmy.forward(40)
#         timmy.right(a)
#     p += 1

# screen.exitonclick()

timmy.speed(0)


directions = [0, 90, 270, 360]
while True:
    timmy.pensize(random.randint(1, 10))
    timmy.color(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    timmy.forward(random.randint(10, 30))
    timmy.right(random.choice(directions))
