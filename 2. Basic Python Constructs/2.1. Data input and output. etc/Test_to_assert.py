# хочу написать функцию чтоыб избавиться от рутины и не делаеть самому
# изменение тестов от яндекса в assert
#


def my_func(x):
    return x


assert my_func(123) == 53
assert my_func(741) == 115
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


# если яндекс пишет ошибку:
# Вывод
# Пока нет данных
# Вывод чекера
# Completion status: ABNORMAL_EXIT
# Term sig: null
# Error code: 2
# то необходимо: 
# 1) верно указать type input
# чтобы проверить себя нужно запустить программу и ввести в неё данные МАНУАЛЬНО


def main():
    # t_room, t_cond = map(int, input().split())
    a, b, c = [int(input()) for _ in range(3)]
    x = int(input())
    print(my_func(x))


if __name__ == '__main__':
    main()
