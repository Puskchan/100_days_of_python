from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        ar = Turtle("square")
        ar.color("white")
        ar.penup()
        ar.goto(position)
        self.segments.append(ar)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            x_c = self.segments[seg_no - 1].xcor()
            y_c = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(x_c, y_c)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

