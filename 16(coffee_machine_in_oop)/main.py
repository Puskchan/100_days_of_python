from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


card = Menu()
machine = CoffeeMaker()
mon_mon = MoneyMachine()

go_on = 1

while go_on > 0:
    coffee = input("Which coffee do you want? " + card.get_items() + " ")
    if coffee == "report":
        machine.report()
        mon_mon.report()
    elif coffee == "off":
        go_on = -1
        print("Good to go for maintenance")
    else:
        coffee_type = card.find_drink(coffee)
        if machine.is_resource_sufficient(coffee_type):
            if mon_mon.make_payment(coffee_type.cost):
                machine.make_coffee(coffee_type)