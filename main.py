from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

x = 0

paddle = Paddle((0, -250))

block1 = Paddle((0, 250))
block2 = Paddle((-320, 250))
block3 = Paddle((320, 250))


ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 30 and ball.ycor() > -350:
        ball.bounce_y()

    if ball.distance(block1) < 30 and ball.ycor() < 350:
        ball.bounce_y()
        block1.goto(900, 900)

    if ball.distance(block2) < 30 and ball.ycor() < 350:
        ball.bounce_y()
        block2.goto(900, 900)

    if ball.distance(block3) < 30 and ball.ycor() < 350:
        ball.bounce_y()
        block3.goto(900, 900)

    if (block1.ycor() == 900
        and block2.ycor() == 900
        and block3.ycor() == 900):
        print("YOU WIN")
        break

    # Detect R paddle misses
    if ball.ycor() < -300:
        ball.reset_position()

screen.exitonclick()
