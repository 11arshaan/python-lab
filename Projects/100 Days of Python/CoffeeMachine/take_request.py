from handle_transaction import handle_transaction
from check_ingredients import check_ingredients


def take_request(costs, resources):
    request_item = input('''Welcome to CoffeeMachine! What would you like? (espresso/latte/cappuccino/exit)\n''')
    menu_items = ("espresso", "latte", "cappuccino")
    if request_item == "report" or request_item == "Report":
        print(f'Resources:\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\n')
        return
    elif request_item in menu_items:
        if check_ingredients(request_item, costs, resources):
            handle_transaction(request_item, costs, resources)
    elif request_item == "exit" or request_item == "Exit":
        return "exit"
    else:
        input('''Invalid entry. What would you like? (espresso/latte/cappuccino/exit)''')
