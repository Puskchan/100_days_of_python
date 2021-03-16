import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

playboy = Player()

screen.listen()
screen.onkey(playboy.up, "Up")

cars = CarManager()

scoreboard = Scoreboard()
game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()

    if counter % 6 == 0:
        cars.new_car()
    counter += 1

    for i in range(len(cars.turtles)):
        if playboy.distance(cars.turtles[i].xcor(), cars.turtles[i].ycor()) < 25:
            scoreboard.game_over()
            game_is_on = False

    if playboy.ycor() > 280:
        cars.next_level()
        playboy.goto(0, -280)
        scoreboard.level_up()


screen.exitonclick()
