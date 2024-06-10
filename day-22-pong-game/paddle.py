from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(cor)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)