from turtle import Screen, Turtle
import paddle as p
import time
from ball import Ball
from scoring import PlayerScore, Line

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
p1_Score = PlayerScore('left', 0)
p2_Score = PlayerScore('right', 0)


ball = Ball()
line = Line()
screen.onkey(paddleL.go_up, 'w')
screen.onkey(paddleL.go_down, 's')
screen.onkey(paddleR.go_up, 'Up')
screen.onkey(paddleR.go_down, 'Down')


def paddle_collision(paddle, offset):
    if offset > 0:  # for paddleL
        return (ball.xcor() <= paddle.xcor() + offset) and (paddle.ycor() - 60 <= ball.ycor() <= paddle.ycor() + 50)
    else:  # for paddleR
        return (ball.xcor() >= paddle.xcor() + offset) and (paddle.ycor() - 60 <= ball.ycor() <= paddle.ycor() + 50)


while game:
    if paddle_collision(paddleR, -20):
        ball.left = True
    if paddle_collision(paddleL, 20):
        ball.left = False
    if ball.ycor() >= 260:
        ball.down = True
    if ball.ycor() <= -290:
        ball.down = False
    if ball.xcor() >= 390:
        p1 += 1
        ball.left = True
        ball.reset()
        paddleR.reset()
        paddleL.reset()
        p1_Score.clear()
        p1_Score = PlayerScore('left', p1)
    if ball.xcor() <= -390:
        p2 += 1
        ball.left = True
        ball.reset()
        paddleR.reset()
        paddleL.reset()
        p2_Score.clear()
        p2_Score = PlayerScore('right', p2)
    time.sleep(0.1)
    ball.move()
    screen.update()


screen.exitonclick()
