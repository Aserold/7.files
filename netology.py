import json
import pprint
with open("recipes.txt", 'r', encoding="utf8") as file:
    meal = {}
    for meal_name in file:
        ingredient_count = int(file.readline())
        ingredients_list = []
        for i in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients_list.append({
                'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        meal[meal_name.strip()] = ingredients_list
    res = json.dumps(meal, indent=2, ensure_ascii=False)

pp = pprint.PrettyPrinter(indent=2)

print("cook_book = {")
for recipe, ingredients in meal.items():
    print(f"  '{recipe}': [")
    for ingredient in ingredients:
        ingredient_name = ingredient['ingredient_name']
        quantity = ingredient['quantity']
        measure = ingredient['measure']
        print(f"    {{'ingredient_name': '{ingredient_name}', 'quantity': {quantity}, 'measure': '{measure}'}},")
    print("  ],")
print("}")