from turtle import Turtle, Screen
import random
import painting

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

timmy.speed(0)


# directions = [0, 90, 270, 360]
# while True:
#     timmy.pensize(random.randint(1, 10))
#     timmy.color(random.randint(0, 255), random.randint(
#         0, 255), random.randint(0, 255))
#     timmy.forward(random.randint(10, 30))
#     timmy.right(random.choice(directions))
# def paintColor(colors, object):
#     color_choice = random.choice(colors)
#     return object.color(color_choice)


# def spirograph(angle):
#     n = int(360 / angle)
#     while n > 0:
#         paintColor(painting.rgb_colors, timmy)
#         timmy.circle(100)
#         timmy.right(angle)
#         n -= 1
# spirograph(12)


def startPos():
    width = screen.window_width() // 2 - 30
    height = screen.window_height() // 2 - 30
    return (-width, -height)


def move_and_dot():
    timmy.forward(100)
    timmy.dot(20, random.choice(painting.rgb_colors))


def dotPainting():
    timmy.penup()
    timmy.goto(startPos())
    timmy.dot(20, random.choice(painting.rgb_colors))
    while True:
        move_and_dot()
        curr_x, curr_y = timmy.xcor(), timmy.ycor()

        if curr_x >= screen.window_width() // 2 - 20:
            timmy.left(90)
            move_and_dot()
            timmy.left(90)
            curr_y = timmy.ycor()
            if curr_y >= screen.window_height() // 2 - 20:
                print("Image complete")
                break

        elif curr_x <= -screen.window_width() // 2 + 10:
            timmy.right(90)
            move_and_dot()
            timmy.right(90)
            curr_y = timmy.ycor()
            if curr_y >= screen.window_height() // 2 - 20:
                print("Image complete")
                break


dotPainting()
screen.exitonclick()
