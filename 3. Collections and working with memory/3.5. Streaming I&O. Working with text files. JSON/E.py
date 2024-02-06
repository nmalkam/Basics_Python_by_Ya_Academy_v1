def pali_6():
    from sys import stdin
    words = []
    for line in stdin:
        words.extend(line.rstrip('\n').split())
    lst = [pali for pali in words if pali.lower() == pali[::-1].lower()]
    print(*[sorted(set(lst))], sep='\n')
    # res = []
    # for line in words:
    #     for word in line.split():
    #         if word.lower() == word[::-1].lower():
    #             res.append(word)
    # for word in sorted(set(res)):
    #     print(word)


def main():
    pali_6()


if __name__ == '__main__':
    main()
