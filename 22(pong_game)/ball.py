from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        xc = self.xcor() + self.x_move
        yc = self.ycor() + self.y_move
        self.goto(xc, yc)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def resetting(self):
        self.goto(0, 0)
        self.move_speed = 0.1
