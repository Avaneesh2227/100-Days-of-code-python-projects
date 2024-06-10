from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def all_shapes(turt):
    for i in range(9):
        for j in range(i + 3, 0, -1):
            turt.forward(100)
            turt.right(360 / (i + 3))

def random_walk(turt):
    directions = [0, 90, 180, 270]
    turt.pensize(10)
    turt.speed(0)
    for i in range(500):
        turt.pencolor(random_color())
        turt.forward(20)
        turt.seth(random.choice(directions))
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return ((r, g, b))

def spirograph(turt,size):
    turt.speed(0)
    for i in range(360//size):
        turt.pencolor(random_color())
        turt.circle(100)
        turt.seth(turt.heading()+size)

def dots(turt):
    turt.penup()
    turt.setx(-300)
    turt.sety(-300)
    for i in range(10):
        turt.setx(-300)
        turt.sety(turt.ycor()+50)
        for j in range(10):
            turt.pencolor(random_color())
            turt.dot(size=20)
            turt.penup()
            turt.forward(50)
dots(t)
screen.exitonclick()
