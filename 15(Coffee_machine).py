MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def get_money():
    quarters = int(input("How many Quarters? : "))
    dimes = int(input("How many Dimes? : "))
    nickles = int(input("How many Nickles? : "))
    pennies = int(input("How many Pennies? : "))
    total_value = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    return total_value


def check_material(cof):
    for i in MENU[cof]["ingredients"]:
        if MENU[cof]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}!")
            return False
        else:
            resources[i] -= MENU[cof]["ingredients"][i]
            return True


def exchange(wch):
    total = get_money()
    if total > MENU[wch]["cost"]:
        remaining_cost = total - MENU[wch]["cost"]
        print(f"Returning {remaining_cost} in exact change!")
        print(f"Here is your {wch} ☕!")
    else:
        print("Not put in enough money!")


def which_coffee(typ):
    if typ == "espresso":
        espresso()
        return 1
    elif typ == "latte":
        latte()
        return 1
    elif typ == "cappuccino":
        cappuccino()
        return 1
    elif typ == "off":
        print("Machine is ready for maintenance!")
        return get_coffee - 2
    elif typ == "report":
        for i in resources:
            print(f"{i} : {resources[i]}")
        return 1
    else:
        print("Don't enter stupid shit!")
        return get_coffee - 2


def espresso():
    okay = check_material("espresso")
    if okay:
        resources["money"] += MENU["espresso"]["cost"]
        exchange("espresso")


def latte():
    okay = check_material("latte")
    if okay:
        resources["money"] += MENU["latte"]["cost"]
        exchange("latte")


def cappuccino():
    okay = check_material("cappuccino")
    if okay:
        resources["money"] += MENU["cappuccino"]["cost"]
        exchange("cappuccino")


get_coffee = 1

while get_coffee > 0:
    coffee_type = input("Which coffee do you want? (espresso/latte/cappuccino): ")
    get_coffee = which_coffee(coffee_type)
