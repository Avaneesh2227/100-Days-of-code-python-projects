from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
play_ball = Ball()
score = Scoreboard()

screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

game = True
while game:
    screen.update()
    time.sleep(0.05)
    play_ball.move()

    if play_ball.ycor() > 280 or play_ball.ycor() < -280:
        play_ball.bounce()

    if (play_ball.distance(r_paddle) < 50 and play_ball.xcor() > 320) or (
            play_ball.distance(l_paddle) < 50 and play_ball.xcor() < -320):
        play_ball.x_move += 1
        play_ball.y_move += 1
        play_ball.deflect()

    if play_ball.xcor() > 380:
        play_ball.reset_pos()
        play_ball.x_move = 10
        play_ball.y_move = 10
        score.l_point()

    if play_ball.xcor() < -380:
        play_ball.reset_pos()
        play_ball.x_move = 10
        play_ball.y_move = 10
        score.r_point()

screen.exitonclick()
