def masterpiece():

    list_products = []
    dishes_lst = []
    dishes_cooked = 0
    menu = []
    d_recipe_ingredients = {}

    for _ in range(int(input())):
        list_products.append(input())  # или set?

    for _ in range(n_recipes := int(input())):
        recipe = input()
        dishes_lst.append(recipe)
        list_recipe_ingredients = []
        for n in range(n_indgredients := int(input())):
            list_recipe_ingredients.append(recipe_ingredient := input())
        d_recipe_ingredients[recipe] = list_recipe_ingredients

    # for rcp in dishes_lst:
    #     if (set(d_recipe_ingredients[rcp]) & set(list_products) == set(d_recipe_ingredients[rcp])):
    #         menu.append(rcp)
    #
    # if menu:
    #     menu.sort()
    #     for name in menu:
    #         print(name)
    # else:
    #     print('Готовить нечего')
    for rcp in dishes_lst:
        count = 0
        for item in d_recipe_ingredients[rcp]:
            if item in list_products:
                count += 1
            if len(d_recipe_ingredients[rcp]) == count:
                print(rcp)
                dishes_cooked += 1

    if dishes_cooked < 1:
        print('Готовить нечего')


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    masterpiece()


if __name__ == '__main__':
    main()
