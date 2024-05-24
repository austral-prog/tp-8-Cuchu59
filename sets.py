from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name, drink_ingredients):
    for x in drink_ingredients:
        if x in ALCOHOLS:
            return drink_name + " Mocktail"
    return drink_name + " Cocktail"
