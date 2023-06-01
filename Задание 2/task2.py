import json
import pprint
with open("C:\\Users\\oluwo\\OneDrive\\Desktop\\Задание7\\Задание 2\\recipes.txt", 'r', encoding="utf8") as file:
    cook_book = {}
    for meal_name in file:
        ingredient_count = int(file.readline())
        ingredients_list = []
        for i in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients_list.append({
                'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        file.readline()
        cook_book[meal_name.strip()] = ingredients_list
    res = json.dumps(cook_book, indent=2, ensure_ascii=False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list