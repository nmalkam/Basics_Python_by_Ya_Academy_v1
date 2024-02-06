def promotion():
    full_price = 0
    # price = float(input())
    while (price := float(input())) != 0:  # while price := float(input()) != 0:
        #  будет совсем другой результат. price будет bool
        # print(price)
        if price >= 500:
            price = price * 0.9
            # print(price)
            # print(type(price))
        full_price += price
    return full_price


def main():
    print(promotion())


if __name__ == '__main__':
    main()
