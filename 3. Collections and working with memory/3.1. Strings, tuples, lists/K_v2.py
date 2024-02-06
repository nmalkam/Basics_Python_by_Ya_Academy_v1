def everything_will_be_found():

    text = []
    count = int(input())

    for i in range(count):
        text.append(input())
    f = input().lower()
    for j in text:
        if f in j.lower():
            print(j)


def main():
    everything_will_be_found()


if __name__ == '__main__':
    main()
