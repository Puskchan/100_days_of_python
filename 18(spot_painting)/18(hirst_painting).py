import random
from turtle import Turtle, Screen

colours = [(255, 255, 100),
           (128, 128, 128),
           (0, 128, 128),
           (128, 0, 0),
           (128, 0, 128),
           (255, 0, 255),
           (255, 255, 0),
           (0, 255, 255),
           (255, 165, 0),
           (0, 0, 165)]

ari = Turtle()
playground = Screen()
playground.colormode(255)
playground.setworldcoordinates(-500, -500, 500, 500)
ari.up()
ari.goto(-450, -445)
ari.down()
ari.speed("fastest")

i = -445

for j in range(10):
    for _ in range(10):
        ari.dot(40, random.choice(colours))
        ari.up()
        ari.fd(100)
        ari.down()
    ari.up()
    i += 100
    ari.goto(-450, i)
    ari.down()


playground.exitonclick()
