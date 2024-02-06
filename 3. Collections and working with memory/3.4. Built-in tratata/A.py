def list_automation(s):
    # import itertools

    for index, value in enumerate(input().split(), 1):
        print(f'{index}. {value}')


assert list_automation('картина корзина картонка') == 3
print('comment the line!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


def main():
    strng = input()
    list_automation(strng)


if __name__ == '__main__':
    main()
