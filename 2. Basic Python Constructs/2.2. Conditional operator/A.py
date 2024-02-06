def my_func(username, mood):
    print("Как Вас зовут?")
    print(f"Здравствуйте, {username}!")
    print("Как дела?")
    if mood == "хорошо":
        print("Я за вас рада!")
    elif mood == "плохо":
        print("Всё наладится!")

# assert my_func(1, 2.2.Conditional operator) == 3


def main():
    username = input()
    mood = input()
    my_func(username, mood)


if __name__ == '__main__':
    main()
