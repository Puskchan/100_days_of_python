from turtle import Turtle

SCORE = (-90, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def score_value(self, scr):
        self.reset()
        self.up()
        self.goto(SCORE)
        self.color("white")
        self.write(f"Score : {scr}", False, font=("Arial", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

