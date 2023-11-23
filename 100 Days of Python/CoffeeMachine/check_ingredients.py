def check_ingredients(item, costs, resources):
    available = True
    selected_item = costs[item]
    ingredients = selected_item["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"There is not enough {ingredient}")
            available = False
    if available:
        return True
    else:
        return False
