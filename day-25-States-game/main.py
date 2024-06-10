# import csv
#
# with open("weather_data.csv") as weather:
#     temperatures=[]
#     data=csv.reader(weather)
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
'''
import pandas
data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels,red_squirrels,black_squirrels]
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
'''
import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Indian states")
screen.addshape("india-map.gif")
turtle.shape("india-map.gif")

pointer=Turtle()

total_states = 36
num_guessed = 0

while num_guessed != total_states:
    answer_state = screen.textinput(title=f"Guess the state. {num_guessed}/{total_states} guessed",
                                    prompt="Guess another state").title()
    if answer_state=="exit":
        break
    data = pandas.read_csv("states.csv")
    df=data[data["state"] == answer_state]

    if df.empty:
        continue
    else:
        pointer.penup()
        pointer.hideturtle()
        pointer.goto(int(df.x),int(df.y))
        pointer.write(arg=f"{answer_state}")
        num_guessed+=1




