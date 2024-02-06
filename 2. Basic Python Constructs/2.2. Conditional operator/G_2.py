def my_func(x):
    reversed = x[::-1]
    if x == reversed:
        return "YES"
    else:
        return "NO"
    # index = 0
    # min_index = -1
    # for item in range(len(str(x))):
    #     if x[index] == x[min_index]:
    #         if index + 1 == len(str(x)):
    #             return "YES"
    #         index += 1
    #         min_index -= 1
    #     else:
    #         return "NO"


assert my_func("1234") == "NO"
assert my_func("2332") == "YES"
assert my_func("23132") == "YES"
# print("Успешно! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = input()
    print(my_func(x))


if __name__ == '__main__':
    main()
