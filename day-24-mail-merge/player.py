from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.seth(90)
        self.goto(STARTING_POSITION)
        self.finish=False

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.finish=True
            self.goto(STARTING_POSITION)
