def my_func(len_a, len_b, len_c):
    list_side = [len_a, len_b, len_c]
    big = max(list_side)
    list_side.remove(max(list_side))
    if big**2 > (list_side[0]**2 + list_side[1]**2):
        return "велика"
    elif big**2 < (list_side[0]**2 + list_side[1]**2):
        return "крайне мала"
    elif big**2 == (list_side[0]**2 + list_side[1]**2):
        return "100%"


assert my_func(3, 5, 4) == "100%"
assert my_func(6, 3, 4) == "велика"
assert my_func(1, 2, 2) == "крайне мала"
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    len_a = int(input())
    len_b = int(input())
    len_c = int(input())
    print(my_func(len_a, len_b, len_c))


if __name__ == '__main__':
    main()
