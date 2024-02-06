def zaika3():
    count = 0
    while (string := input()) != "Приехали!":
        if "зайка" in string:
            count += 1
    # print(count)
    return count

    # while (name := input("Введите имя: ")) != "СТОП":
    #     print(f"Привет, {name}!")
    # print("Программа завершена.")


def main():
    # x = input()
    print(zaika3())


if __name__ == '__main__':
    main()
