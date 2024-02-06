# моё решение не верное потому что я ставлю услвие на добавление в res char
# поэтому я могу пропустить какие-либо знаки не попадающие под это условие
# хотя по идее условие нормальное, очень и очень странно
def transliteration(strng: str) -> str:

    res = ''

    TRANSLITERATE_DICT = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''}

    for char in strng:
        if char.isalpha():
            if char.isupper():
                res += TRANSLITERATE_DICT[char].title()
            else:
                char = TRANSLITERATE_DICT[char.upper()]
                res += char.lower()
        else:
            res += char

    # print(res)

    return res


# assert transliteration('Привет, мир!') == "Privet, mir!"
# assert transliteration(
#     'Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное виденье, Как гений чистой красоты.') \
#        == "Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, Kak mimoletnoe videne, Kak genii chistoi krasoty."
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    strng = input()

    print(transliteration(strng))


if __name__ == '__main__':
    main()
