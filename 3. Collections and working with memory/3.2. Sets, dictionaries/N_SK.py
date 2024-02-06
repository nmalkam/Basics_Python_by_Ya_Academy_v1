products = []
recipes = {}
menu = []

for _ in range(int(input())):
    products.append(input())

for _ in range(int(input())):
    name = input()
    ingredients = []
    for _ in range(int(input())):
        ingredients.append(input())
        recipes[name] = recipes.get(name, []) + ingredients

for name in recipes:
    if (set(recipes[name]) & set(products) == set(recipes[name])):
        menu.append(name)

if menu:
    menu.sort()
    for name in menu:
        print(name)
else:
    print('Готовить нечего')
