from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.reset_scoreboard()

    def read_highscore(self):
        with open("data.txt") as hscore:
            self.highscore =int(hscore.read())

    def write_highscore(self, score):
        with open("data.txt", mode="w") as hs:
            hs.write(score)

    def reset_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.reset_scoreboard()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset_score(self):
        self.read_highscore()
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore(f"{self.highscore}")
        self.score = 0
        self.reset_scoreboard()

