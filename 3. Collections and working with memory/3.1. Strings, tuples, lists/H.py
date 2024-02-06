def zaika7():

    res = 0
    count = 0
    find = 0

    n = int(input())
    while count != n:
        string = input()
        words_list = string.split(' ')
        for i, word in enumerate(words_list):
            if 'зайка' in word:
                print(int(string.index('зайка')) + 1)
                res = i + 1
            if res != 0:
                # print(res)
                find = 1
                res = 0
                break
        if find == 0:
            print('Заек нет =(')
        find = 0
        count += 1
# НУЭНО ВЫВОДИТЬ ИНДЕКС ПЕРВОЙ БУКВЫ СЛОВА ЗАЙКА!!!!!!!!!!!!!!!!!!!!

# я хочу создать список в котором будут постоянно обновляться первая и последняя значение
# например "а зай" добавляем след значение в конец и удаляем первое -> " зайк"
# когда мы получаем в строке "зайка" то

# assert zaika7("березка елочка зайка волк березка") == "YES"
# assert zaika7("сосна сосна сосна елочка грибочки медведь") == "NO"


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    zaika7()


if __name__ == '__main__':
    main()
