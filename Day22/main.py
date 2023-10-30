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
p1, p2 = 0, 0

ball = Ball()
screen.onkey(paddleL.go_up, 'w')
screen.onkey(paddleL.go_down, 's')
screen.onkey(paddleR.go_up, 'Up')
screen.onkey(paddleR.go_down, 'Down')


while game:
    if (ball.xcor() == paddleR.xcor()) and paddleR.ycor()-60 <= ball.ycor() <= paddleR.ycor() + 50:
        ball.left = True
    if (ball.xcor() == paddleL.xcor()) and paddleL.ycor()-60 <= ball.ycor() <= paddleL.ycor() + 50:
        ball.left = False
    if ball.ycor() >= 290:
        ball.down = True
    if ball.ycor() <= -290:
        ball.down = False
    if ball.xcor() >= 390:
        p1 += 1
        ball.left = True
        ball.reset()
        paddleR.reset()
        paddleL.reset()
    if ball.xcor() <= -390:
        p2 += 1
        ball.left = True
        ball.reset()
        paddleR.reset()
        paddleL.reset()
    time.sleep(0.1)
    ball.move()
    screen.update()


screen.exitonclick()
