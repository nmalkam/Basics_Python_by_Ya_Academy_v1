def bicycle_race_counter(n):
    count = 1
    seconds = 3
    while count != n + 1:
        while seconds != 0:
            print(f'До старта {seconds} секунд(ы)')
            seconds -= 1
        else:
            print(f'Старт {count}!!!')
            seconds = 3 + count
            count += 1


# assert bicycle_race_counter(3) == "NO"
# assert bicycle_race_counter(4) == "YES"
# assert bicycle_race_counter("23132") == "YES"
# print("Успешно! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    n = int(input())
    bicycle_race_counter(n)


if __name__ == '__main__':
    main()
# До старта 3 секунд(ы)
# До старта 2 секунд(ы)
# До старта 1 секунд(ы)
# Старт 1!!!
# До старта 4 секунд(ы)
# До старта 3 секунд(ы)
# До старта 2 секунд(ы)
# До старта 1 секунд(ы)
# Старт 2!!!
# До старта 5 секунд(ы)
# До старта 4 секунд(ы)
# До старта 3 секунд(ы)
# До старта 2 секунд(ы)
# До старта 1 секунд(ы)
# Старт 3!!!
