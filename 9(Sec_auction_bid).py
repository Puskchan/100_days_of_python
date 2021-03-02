import os

def add_bidder(nam,bd):
    bidders[nam]=bd
    return bidders

game = 0

print('''
                 ___________
                 \         /
                  )_______(
                  |"""""""|_.-._,.---------.,_.-._
                  |       | | |               | | ''-.
                  |       |_| |_             _| |_..-'
                  |_______| '-' `'---------'` '-'
                  )"""""""(
                 /_________\\
               .-------------.
              /_______________\\
''')

bidders = {}

while game == 0:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    all_bidders = add_bidder(name,bid)
    klist = list(all_bidders.keys())
    vlist = list(all_bidders.values())
    go_on = input("Want to add more users? yes/no: ")
    k = max(vlist)
    p = vlist.index(k)
    l = klist[p]
    if go_on == "no":
        print(f"The highest bidder was {l} with a bid of {k}")
        game +=1
    else:
        os.system("cls")

print("Thanks for playing!")