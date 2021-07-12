from turtle import Screen, Turtle
from netting import Netting
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
game_on = True
speed = 0.06

for line in range(21):
    Netting(line)

paddle1 = Paddle(-360)
paddle2 = Paddle(360)
ball = Ball()
scoring = ScoreBoard()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

while game_on:
    time.sleep(speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        if speed >= .005:
            speed -= .005

    # detect if ball hits paddle
    if ball.distance(paddle2) < 50 and ball.xcor() > 336 \
            or ball.distance(paddle1) < 50 and ball.xcor() < -336:
        ball.hit()
        if speed >= .005:
            speed -= .005

    # detect point
    if ball.xcor() > 465:
        ball.home()
        ball.hit()
        scoring.score_player1()
        scoring.update_score()
        speed = 0.05

    if ball.xcor() < -465:
        ball.home()
        ball.hit()
        scoring.score_player2()
        scoring.update_score()
        speed = 0.05







screen.exitonclick()

