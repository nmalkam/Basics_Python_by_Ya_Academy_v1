def elochka_gori():
    while input() != "Три!":
        print("Режим ожидания...")
    print("Ёлочка, гори!")
    return "Ёлочка, гори!"


def main():
    # x = input()
    elochka_gori()


if __name__ == '__main__':
    main()

# while (name := input("Введите имя: ")) != "СТОП":
#     print(f"Привет, {name}!")
# print("Программа завершена.")
