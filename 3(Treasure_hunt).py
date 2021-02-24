print("Welcome to treasure island!!")
choice1 = input("Where do you want to go? Right or left?: ")
if choice1.lower() == "right":
    print("Game over")
elif choice1.lower() == "left":
    choice2 = input("What will you do? swim or wait?: ")
    if choice2.lower() == "swim":
        print("Game over")
    elif choice2.lower() == "wait":
        choice3 = input("What door? Red, yellow, blue?: ")
        if choice3.lower() == "red":
            print("Game over")
        if choice3.lower() == "blue":
            print("Game over")
        if choice3.lower() == "yellow":
            print("You win!")
        else:
            print("Try again,Wrong input!")

    else:
        print("Try again,Wrong input!")

else:
    print("Try again,Wrong input!")
