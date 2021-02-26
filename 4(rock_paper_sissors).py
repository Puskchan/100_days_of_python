import random

ui = int(input("Rock(0), paper(1), sissors(2)?: \n"))
print(f"player choose {ui}")
r = random.randint(0,2)
print(f"computer choose {r}")
if r == 0 and ui == 2:
    print("Computer wins!")
elif r == 2 and ui ==0:
    print("The player wins!")
elif r>ui:
    print("Computer wins")
elif r<ui:
    print("The player wins!")
else:
    print("Draw!")