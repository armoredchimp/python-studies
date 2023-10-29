from turtle import Screen, Turtle
import paddle as p
import time
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
screen.listen()

paddleR = p.Paddle(350)
paddleL = p.Paddle(-350)

game = True


ball = Ball()
screen.onkey(paddleL.go_up, 'w')
screen.onkey(paddleL.go_down, 's')
screen.onkey(paddleR.go_up, 'Up')
screen.onkey(paddleR.go_down, 'Down')


while game:

    time.sleep(0.1)
    if
    ball.move()
    screen.update()


screen.exitonclick()
