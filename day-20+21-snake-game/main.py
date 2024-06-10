from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.move_food()
        scoreboard.increase_score()
        snake.add_segment()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or \
            snake.segments[0].ycor() < -290:
        snake.reset()
        scoreboard.reset_score()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            snake.reset()
            scoreboard.reset_score()


screen.exitonclick()
