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
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
# TODO 1. Prompt user by ask "What would you like? (espresso/latte/cappuccino): "


def coffee_machine():
    flavor = input("What would you like? (espresso/latte/cappuccino): ")
    if flavor == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\ncoffee: {resources['coffee']}g\n"
              f"Money: ${resources['money']}")
        coffee_machine()
    elif flavor == "off":
        print("Goodbye!")
        return
    else:
        is_enough(flavor)


def is_enough(flavor):
    water_enough = False
    milk_enough = False
    coffee_enough = False
    ingredients = MENU[flavor]["ingredients"]
    for item in ingredients:
        if resources[item] >= ingredients[item]:
            check_money(flavor)
        else:
            print(f"Sorry, no enough {item}.")
            return coffee_machine()


def check_money(flavor):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dims = int(input("How many dims?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coins = 0.25 * quarters + dims * 0.1 + nickles * 0.05 + pennies * 0.01
    cost = MENU[flavor]["cost"]
    if coins < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return coffee_machine()
    else:
        change = round(coins - cost, 2)
        resources["money"] += cost
        print(f"Here is ${change} in change.")
        make_coffee(flavor, MENU[flavor]["ingredients"])
        coffee_machine()


def make_coffee(flavor, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {flavor}. ☕ Enjoy!")


coffee_machine()

# TODO 2. Turn off the coffee machine by entering "off" to the prompt.

# TODO 3. Print report

# TODO 4. Check resources sufficient?

# TODO 5. Process coins.

# TODO 6. Check transaction successful?

# TODO 7. Make coffee