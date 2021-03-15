from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def position_(self, loc):
        if loc == "right":
            loc = 350
        if loc == "left":
            loc = -350
        self.penup()
        self.seth(90)
        self.goto(loc, 0)

    def up(self):
        self.fd(10)

    def down(self):
        self.fd(-10)
