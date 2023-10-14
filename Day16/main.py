from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


m = Menu()
maker = CoffeeMaker()
bank = MoneyMachine()


def init(menu, machine, bank):
    first = input(
        "Welcome to the coffee machine! Type report to see the machine data, off to turn off the machine, or any key to see the menu:").lower()
    if first == 'report':
        machine.report()
        init(m, maker, bank)
    elif first == 'off':
        exit()
    else:
        print(m.get_items())
        order = menu.find_drink(input("What would you like to order: \n"))
        if (machine.is_resource_sufficient(order) == True):
            if (bank.make_payment(order.cost) == True):
                machine.make_coffee(order)
                init(m, maker, bank)


init(m, maker, bank)
