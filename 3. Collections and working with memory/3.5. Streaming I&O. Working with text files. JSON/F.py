def transliteration_2():
    TRANSLITERATION = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'kh',
        'ц': 'tc',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ы': 'y',
        'э': 'e',
        'ю': 'iu',
        'я': 'ia',
        'ъ': '',
        'ь': '',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'Kh',
        'Ц': 'Tc',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ы': 'Y',
        'Э': 'E',
        'Ю': 'Iu',
        'Я': 'Ia',
        'Ъ': '',
        'Ь': '',
    }
    with open('cyrillic.txt', 'r', encoding='UTF-8') as cyr:
        lines = cyr.readlines()
    with open('transliteration.txt', 'w', encoding='utf-8') as t:
        for line in lines:
            for letter in list(line):
                if letter in TRANSLITERATION:
                    t.write(''.join(TRANSLITERATION[letter]))
                else:
                    t.write(letter)


def main():
    transliteration_2()


if __name__ == '__main__':
    main()
