from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.penup()
        self.hideturtle()
        self.goto(-200, 270)
        self.write(f"Current level: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over at level: {self.level}", False, align="center", font=FONT)
