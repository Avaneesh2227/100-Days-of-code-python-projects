from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)
pred=screen.textinput(title="Make your bet", prompt="Who will win the race? red/yellow/green/blue/orange/purple: ").lower()
turtles=[]
colors=["red","orange","yellow","green","blue","purple"]
y=175
game=True

for i in range(6):
    ori=Turtle(shape="turtle")
    ori.penup()
    ori.color(colors[i])
    ori.setpos(-225, y)
    y-=66
    turtles.append(ori)

while game:
    for tur in turtles:
        tur.forward(random.randint(0,10))
        if tur.xcor()>=220:
            game=False
            if pred==tur.pencolor():
                print("You've won!")
            else:
                print("You lost")
            break






screen.exitonclick()