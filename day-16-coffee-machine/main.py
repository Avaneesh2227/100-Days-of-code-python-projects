from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
continue_on = True
coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
while continue_on:
    response = input(f"What would you like? ({menu.get_items()}): ")
    if response == "off":
        continue_mach = False
        break
    elif response == "report":
        coffee.report()
        money.report()
    else:
        order = menu.find_drink(response)
        if order and coffee.is_resource_sufficient(order):
            if money.make_payment(order.cost):
                coffee.make_coffee(order)
