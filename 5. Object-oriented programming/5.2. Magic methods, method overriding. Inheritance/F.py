"""FFFFFFFFFFFFFFFFFFFFF"""


class Fraction:
    def __gcd(self, a, b):
        ch = a
        zn = b
        while b != 0:
            c = b
            a, b = b, a % b
        return int(ch / c), int(zn / a)

    def __lcm(self, a, b):
        a1, b1 = a, b
        while a != 0:
            a, b = b % a, a
        return a1 * b1 // (a + b)

    def __init__(self, *args) -> None:  # OR numerator, denominator OR str: '7/14'
        if isinstance(args[0], str):
            n, d = map(int, args[0].split('/'))
            self.num, self.denomr = self.__gcd(n, d)
        else:
            self.num, self.denomr = self.__gcd(args[0], args[1])
        self.__reduction()

    def __reduction(self) -> tuple:
        __gcd = self.__gcd(self.num, self.denomr)
        # self.num //= __gcd
        # self.denomr //= __gcd

        if self.denomr < 0:
            self.num = -self.num
            self.denomr = abs(self.denomr)
        return self.num, self.denomr

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

    def __str__(self):
        return f"{self.num}/{self.denomr}"

    def __repr__(self):
        return f"Fraction('{self.num}/{self.denomr}')"

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.num, self.denomr)

    def __add__(self, other) -> 'Fraction':
        lcm = self.__lcm(self.denomr, other.denomr)
        r_n_self = int(self.num * (lcm / self.denomr))  # result numerator self
        r_n_other = int(other.num * (lcm / other.denomr))  # result numerator other
        # res_num = self.num + other.num
        # res_denomr = self.denomr + other.denomr
        # return Fraction(Fraction.__gcd(self, r_n_self, r_n_other))
        return Fraction(r_n_self + r_n_other, lcm)

    def __sub__(self, other) -> 'Fraction':
        lcm = self.__lcm(self.denomr, other.denomr)
        r_n_self = int(self.num * (lcm / self.denomr))  # result numerator self
        r_n_other = int(other.num * (lcm / other.denomr))  # result numerator other
        # res_num = self.num + other.num
        # res_denomr = self.denomr + other.denomr
        # return Fraction(Fraction.__gcd(self, r_n_self, r_n_other))
        return Fraction(r_n_self - r_n_other, lcm)

    def __iadd__(self, other) -> 'Fraction':
        lcm = self.__lcm(self.denomr, other.denomr)
        self.num = int(self.num * (lcm / self.denomr))
        # self.denomr = int(other.num * (lcm / other.denomr))
        # self.num += self.num + other.num
        return Fraction(self.num, lcm)

    def __isub__(self, other) -> 'Fraction':
        lcm = self.__lcm(self.denomr, other.denomr)
        self.num = int(self.num * (lcm / self.denomr) - other.num * (lcm / self.denomr))
        # self.denomr = int(other.num * (lcm / other.denomr))
        # self.num += self.num + other.num
        return Fraction(self.num, lcm)


a = Fraction(1, 3)
b = Fraction(1, 2)
# d = Fraction(7, 5)
# c = Fraction(1, 3) + Fraction(1, 2)
c = a + b
# k = a - d
print(a, b, c, a is c, b is c)
# 1/3 1/2 5/6 False False
a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)
# 1/8 1/4 1/4 True
