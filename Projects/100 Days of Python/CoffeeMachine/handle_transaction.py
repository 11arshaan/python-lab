def handle_transaction(item, costs, resources):
    cost = costs[item]["cost"]
    ingredients = costs[item]["ingredients"]
    print(f"{item} is available. Cost: ${cost}. Please Insert Coins below.")
    num_quarters = int(input("How many quarters? ")) * .25
    num_dimes = int(input("How many dimes? ")) * .1
    num_nickles = int(input("How many nickles? ")) * .05
    num_pennies = int(input("How many pennies? ")) * .01

    payment = num_quarters + num_dimes + num_nickles + num_pennies
    if payment < cost:
        print("Sorry, that is not enough money. Returning to menu...")
        return
    if payment >= cost:
        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]
        change = round(payment - cost, 2)
        print(f"Payment successful. Here is your change: ${change}")
        print("Enjoy your coffee!")
        return
