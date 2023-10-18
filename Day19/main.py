from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
timmy.color("purple")


def move_forward():
    timmy.forward(10)


def move_right():
    timmy.right(45)
    timmy.forward(10)


def move_back():
    timmy.backward(10)


def move_left():
    timmy.left(45)
    timmy.forward(10)


def clear():
    timmy.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="p", fun=clear)
screen.exitonclick()
