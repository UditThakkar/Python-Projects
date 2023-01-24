from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    print(items.get_items())
    choice = input("What would you like to have? ")
    if choice == "report":
        maker.report()
        money.report()
    elif choice == "off":
        is_on = False
    else:
        cost = items.menu
        order = items.find_drink(choice)
        if maker.is_resource_sufficient(order):
            # money.process_coins()
            if money.make_payment(order.cost):
                maker.make_coffee(order)
            else:
                pass
            
