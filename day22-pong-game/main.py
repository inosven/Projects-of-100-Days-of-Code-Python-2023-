from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
game_is_on = True
BALL_SPEED = 0.2

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong King!")
screen.tracer(0)
paddle_left = Paddle(-390)
paddle_right = Paddle(380)
scoreboard_left = Scoreboard(-200)
scoreboard_right = Scoreboard(200)
scoreboard_left.create_middle()
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_right.up)
screen.onkeypress(key="Down", fun=paddle_right.down)
screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key="s", fun=paddle_left.down)
#

while game_is_on:
    screen.update()
    ball.move()
    # detect colission with up and down boundary
    if ball.ycor() > 270 or ball.ycor() < -280:
        ball.collision_with_up_down()
    # detect collision with paddle
    for seg in paddle_left.paddle_body:
        if ball.distance(seg) < 15:
            ball.collision_with_paddle()
            ball.speed_up()
    for seg in paddle_right.paddle_body:
        if ball.distance(seg) < 15:
            ball.collision_with_paddle()
            ball.speed_up()
    # detect collision with right boundary
    if ball.xcor() > 380:
        scoreboard_left.score +=1
        scoreboard_left.update()
        ball.recenter()
    # detect collision with right boundary
    if ball.xcor() < -380:
        scoreboard_right.score += 1
        scoreboard_right.update()
        ball.recenter()
screen.exitonclick()
