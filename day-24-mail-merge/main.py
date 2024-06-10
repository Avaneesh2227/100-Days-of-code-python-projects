import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
cars = CarManager()

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.07)
    screen.update()
    if counter % 3 == 0:
        cars.makecar()
    cars.moveCar()
    for car in cars.carslist:
        if player.distance(car) < 20:
            game_is_on = False
            score.finish_game()
            break
    screen.onkeypress(player.move, "Up")
    if player.finish:
        score.update_score()
        cars.speed_boost()
        player.finish = False
    counter += 1

screen.exitonclick()
