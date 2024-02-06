"""EEEEEEEEEEEEEEEEEEEEEEEEE"""
class Fraction:
    # def gcd(self, a, b):
    #     ch = a
    #     zn = b
    #     while b != 0:
    #         c = b
    #         a, b = b, a % b
    #     return int(ch / c), int(zn / a)

    def __gcd(self, a, b):
        ch = a
        zn = b
        while b != 0:
            c = b
            a, b = b, a % b
        return int(ch / c), int(zn / a)

    def __init__(self, *args) -> None:  # OR numerator, denominator OR str: '7/14'
        if isinstance(args[0], str):
            n, d = map(int, args[0].split('/'))
            self.num, self.denomr = self.__gcd(n, d)
        else:
            self.num, self.denomr = self.__gcd(args[0], args[1])
    # достаточно сделать два точечных изменения в логике работы алгоритма:
    # при запросе числителя возвращать его абсолютную величину.
    # при замене числителя, запоминать знак ДО операции, а потом умножить то, что они вам дали на этот знак.
    # дальше можно работать по человеческой схеме и забыть про это мягко скажем странное требование.

    def numerator(self, *number):
        if not number:
            return self.num
        else:
            self.num, self.denomr = self.__gcd(number[0], self.denomr)
            return self.num, self.denomr

    def denominator(self, *number):
        if not number:
            return self.denomr
        else:
            self.num, self.denomr = self.__gcd(self.num, number[0])
            return self.num, self.denomr
    # А также перепишите методы __str__ и __repr__ таким образом,
    # чтобы информация об объекте согласовывалась с инициализацией строкой.

    def __str__(self):
        return f"{self.num}/{self.denomr}"

    def __repr__(self):
        return f"Fraction('{self.num}/{self.denomr}')"

    def __neg__(self):
        return Fraction(-self.num, self.denomr)


# e = Fraction.gcd(3, 4)
a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))
# 1/3 1/3 -1/3 -1/3
# Fraction('1/3') Fraction('1/3') Fraction('-1/3') Fraction('-1/3')
a = Fraction('-1/2')
b = -a
print(a, b, a is b)
a.numerator()
# -b.numerator()
g = -b.numerator()
# f = b.numerator(-b.numerator())
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
# -1/2 1/2 False
# 1/3 -1/2
# 1 3
# 1 2
