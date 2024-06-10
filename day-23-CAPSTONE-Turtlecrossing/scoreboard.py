from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-240, 250)
        self.level = 1
        self.color("black")
        self.write(arg=f"Level {self.level}", font=FONT, move=False)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level {self.level}", font=FONT, move=False)

    def finish_game(self):
        self.goto(-20, 0)
        self.write(arg=f"GAME OVER", font=FONT, move=False)
