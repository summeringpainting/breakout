from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -250))

# Create all the paddle objects
blocks = []
x1 = 0
for i in range(5):
    x = -480
    x1 += 160
    i = Paddle((x + x1, 250))
    q = Paddle((x + x1, 150))
    blocks.append(i)
    blocks.append(q)

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

    for i in blocks:
        if ball.distance(i) < 30 and ball.ycor() < 350:
            ball.bounce_y()
            i.goto(900, 900)

    if all(i.ycor() == 900 for i in blocks):
        print("You Win")
        break

    # Detect R paddle misses
    if ball.ycor() < -300:
        ball.reset_position()

screen.exitonclick()
