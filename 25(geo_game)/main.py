import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

screen = turtle.Screen()
screen.title("USA game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
correct = []

game = True

while game:
    answer_state = (screen.textinput(title=f"{len(correct)}/50 States Correct", prompt="Enter A State's Name:")).title()

    x_data = data[data["state"] == answer_state]
    loc_x = x_data["x"].to_list()
    loc_y = x_data["y"].to_list()

    ari = turtle.Turtle()
    ari.hideturtle()
    ari.penup()

    if answer_state == "Exit":
        game = False

    if answer_state in states and len(correct) < 50:
        states.remove(answer_state)
        ari.goto(loc_x[0], loc_y[0])
        ari.write(f"{answer_state}", False, align="center", font=("Arial", 20, "normal"))
        correct.append(answer_state)
    elif len(states) == 0:
        game = False
        print("You found all the States!!")
    else:
        continue

states_data = pandas.DataFrame(states)
states_data.to_csv("States_left.csv")

screen.exitonclick()
