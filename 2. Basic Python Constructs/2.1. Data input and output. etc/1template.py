# from typing import Optional
#
# def get_some_date(some_argument: int=None) -> Optional[datetime]:
#     # as defined
# def foo(arg: Optional[int] = None) -> None:

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


# Решение с вложенными циклами

# dim = int(input())
#
# count = 1
# num = 1
#
# while num <= dim:
#     for i in range(count):
#         if num <= dim:
#             print(num, end=' ')
#             num += 1
#         else:
#             break
#     print()
#     count += 1

# # Решение с одни циклом
#
# dim = int(input())
#
# num = 1
# pos = 1
#
# for i in range(dim):
#     print(i + 1, end=' ')
#     if pos == num:
#         print()
#         pos = 1
#         num += 1
#     else:
#         pos += 1


max(hash, key=hash.get)
max(hash.values())
