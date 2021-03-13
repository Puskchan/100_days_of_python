import turtle as t
import random

race_on = False
pg = t.Screen()
pg.setup(width=500, height=400)
colors = ["black", "blue", "green", "red", "yellow", "white"]
user_bet = pg.textinput(title="Make a bet!", prompt=f"Choose a color from {colors}")
yolo = [-70, -40, -10, 20, 50, 80]
all_t = []

for i in range(6):
    ari = t.Turtle(shape="turtle")
    ari.color(colors[i])
    ari.pu()
    ari.goto(x=-230, y=yolo[i])
    all_t.append(ari)

if user_bet:
    race_on = True

while race_on:

    for _ in all_t:
        if _.xcor() > 230:
            race_on = False
            win_color = _.pencolor()
            if win_color == user_bet:
                print(f"You've won! The winning color is {win_color}!")
            else:
                print(f"You've lost! The winning color is {win_color}!")

        rand_dist = random.randint(0, 10)
        _.forward(rand_dist)

pg.exitonclick()
