from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.turtles = []
        self.speed = STARTING_MOVE_DISTANCE
        for i in range(0, 2):
            self.new_car()

    def move(self):
        for tur in self.turtles:
            x_c = tur.xcor() - self.speed
            tur.goto(x_c, tur.ycor())

    def new_car(self):
        ari = Turtle()
        ari.penup()
        ari.shapesize(stretch_wid=1, stretch_len=2)
        ari.shape("square")
        ari.color(random.choice(COLORS))
        ari.goto(random.randint(250, 350), random.randint(-250, 250))
        self.turtles.append(ari)

    def next_level(self):
        for tur in self.turtles:
            x_c = tur.xcor() - self.speed
            tur.goto(x_c, tur.ycor())
        self.speed += MOVE_INCREMENT
