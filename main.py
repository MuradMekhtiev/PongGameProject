from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

l_scoreboard = Scoreboard((-250, 260))
r_scoreboard = Scoreboard((230, 260))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 45 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        l_scoreboard.track_score()

    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.track_score()


screen.exitonclick()
