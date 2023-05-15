from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
flag = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while flag:
    flavor = input(f"What would you like? {menu.get_items()}")
    if flavor == "off":
        flag = False
    elif flavor == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(flavor)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)



