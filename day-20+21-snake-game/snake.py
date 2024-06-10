from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()

    def make_snake(self):
        for i in range(3):
            next_seg=self.make_segment()
            next_seg.goto(START_POS[i])
            self.segments.append(next_seg)
    def add_segment(self):
        next_seg=self.make_segment()
        next_seg.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(next_seg)

    def make_segment(self):
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color("white")
        return new_seg


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            xcor_seclast = self.segments[seg - 1].xcor()
            ycor_seclast = self.segments[seg - 1].ycor()
            self.segments[seg].goto(xcor_seclast, ycor_seclast)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].seth(270)

    def right(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].seth(0)

    def left(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].seth(180)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.make_snake()