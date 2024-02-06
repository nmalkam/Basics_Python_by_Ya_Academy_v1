# return ['YES' if new_clean == clean_phone_num(book_item) else 'NO' for book_item in book]


def adding_num(new, book):
    default_code = '495'

    def clean_phone_num(phone_num):
        digits = ''.join([num for num in phone_num if num.isdigit()])
        # digits = (''.join(num for num in phone_num if num.isdigit()))
        if len(digits) == 7:
            return default_code, digits
        else:
            return digits[1:4], digits[4:]

    new_clean = clean_phone_num(new)
    return ['YES' if new_clean == clean_phone_num(book_item) else 'NO' for book_item in book]
    # return ['YES' if clean_phone_num(new) == clean_phone_num(book_item) else 'NO' for book_item in book]


assert adding_num("86406361642",
                  ["83341994118",
                   "86406361642",
                   "83341994118"]) == ['NO', 'YES', 'NO']

assert adding_num("+78047952807",
                  ["+78047952807",
                   "+76147514928",
                   "88047952807"]) == ['YES', 'NO', 'YES']


# assert adding_num("8(495)430-23-97", ["+7-4-9-5-43-023-97", "4-3-0-2-3-9-7", "8-495-430"]) == ['YES', 'YES', 'NO']


def main():
    new = input()
    book = [input(), input(), input()]
    result = adding_num(new, book)
    print(result[0])
    print(result[1])
    print(result[2])


if __name__ == '__main__':
    main()


dic(int())
