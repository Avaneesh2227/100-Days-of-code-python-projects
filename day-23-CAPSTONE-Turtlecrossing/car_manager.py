from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.carslist=[]
        self.speed=STARTING_MOVE_DISTANCE
        self.hideturtle()

    def makecar(self):
        new_car=Turtle(shape="square")
        new_car.penup()
        new_car.goto(580, random.randint(-270, 230))
        new_car.speed = STARTING_MOVE_DISTANCE
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        self.carslist.append(new_car)
    def moveCar(self):
        for car in self.carslist:
            car.goto(car.xcor()-car.speed,car.ycor())
    def speed_boost(self):
        self.speed+=MOVE_INCREMENT


