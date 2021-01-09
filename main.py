from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

#      []
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
screen.exitonclick()
