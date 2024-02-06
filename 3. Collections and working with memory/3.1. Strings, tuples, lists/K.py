# попробовать find или через format (найти способ)

def everything_will_be_found():

    n = int(input())
    count = 0
    r_list = []
    r_dict = {}
    # r = request

    while count != n:
        r = input()
        r_list.append(r.lower().split(' '))
        r_dict[count] = r
        count += 1
    r_word = input().lower()
    for key, request in enumerate(r_list):
        for word in request:
            if word[:len(r_word)] == r_word:
                print(r_dict[key])
                break


# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    everything_will_be_found()


if __name__ == '__main__':
    main()
