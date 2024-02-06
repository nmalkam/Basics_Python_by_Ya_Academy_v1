class Fraction:
    def __gcd(self, a, b):
        """Greatest common divisor Наибольший общий делитель"""
        c = b
        ch = a
        zn = b
        while b != 0:
            c = b
            a, b = b, a % b
        return int(ch / c), int(zn / a)

    def __lcm(self, a, b):
        """least common multiple наименьшее общее кратное"""
        a1, b1 = a, b
        while a != 0:
            a, b = b % a, a
        return a1 * b1 // (a + b)

    def __init__(self, *args) -> None:  # OR numerator, denominator OR str: '7/14' OR numerator
        match len(args):
            case 1:
                if isinstance(args[0], str):
                    if len(args[0]) == 1:
                        self.num = int(args[0])
                        self.denomr = 1
                    else:
                        n, d = map(int, args[0].split('/'))
                        self.num, self.denomr = self.__gcd(n, d)
                else:
                    self.num = int(args[0])
                    self.denomr = 1
            case 2:
                self.num, self.denomr = self.__gcd(args[0], args[1])
        # self.__reduction()
        # n, d = self.__ctf(*args)
        # self.num = n
        # self.denomr = d

    def __reduction(self) -> tuple:
        __gcd = self.__gcd(self.num, self.denomr)

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
        if type(other) != Fraction:
            return Fraction(self.num + other * self.denomr, self.denomr)
        else:
            lcm = self.__lcm(self.denomr, other.denomr)
            r_n_self = int(self.num * (lcm / self.denomr))  # result numerator self
            r_n_other = int(other.num * (lcm / other.denomr))  # result numerator other
            # res_num = self.num + other.num
            # res_denomr = self.denomr + other.denomr
            # return Fraction(Fraction.__gcd(self, r_n_self, r_n_other))
        return Fraction(r_n_self + r_n_other, lcm)

    def __sub__(self, other) -> 'Fraction':
        if type(other) != Fraction:
            return Fraction(self.num - other * self.denomr, self.denomr)
        else:
            lcm = self.__lcm(self.denomr, other.denomr)
            r_n_self = int(self.num * (lcm / self.denomr))  # result numerator self
            r_n_other = int(other.num * (lcm / other.denomr))  # result numerator other
            # res_num = self.num + other.num res_denomr = self.denomr + other.denomr
            # return Fraction(Fraction.__gcd(self, r_n_self, r_n_other))
        return Fraction(r_n_self - r_n_other, lcm)

    def __iadd__(self, other) -> 'Fraction':
        lcm = self.__lcm(self.denomr, other.denomr)
        self.num = int(self.num * (lcm / self.denomr))

        return self

    def __isub__(self, other) -> 'Fraction':
        lcm = self.__lcm(self.denomr, other.denomr)
        self.num, self.denomr = self.__gcd(int(self.num * (lcm / self.denomr)
                                               - other.num * (lcm / self.denomr)), lcm)
        return self

    def __mul__(self, other) -> 'Fraction':  # multiplication
        if type(other) != Fraction:
            return Fraction(self.num * other, self.denomr * other)
        else:
            r_n_self = int(self.num * other.num)  # result numerator self
            r_n_denomr = int(self.denomr * other.denomr)  # result denominator self
        return Fraction(r_n_self, r_n_denomr)

    def __truediv__(self, other) -> 'Fraction':  # division
        if type(other) != Fraction:
            # make other fraction
            return Fraction(self.num * other.denomr, self.denomr * other.num)
        else:
            r_n_self = int(self.num * other.denomr)  # result numerator self
            r_n_denomr = int(self.denomr * other.num)  # result denominator self
        return Fraction(r_n_self, r_n_denomr)

    def __imul__(self, other) -> 'Fraction':  # in-place multiplication
        if type(other) != Fraction:
            return Fraction(self.num * other, self.denomr * other)
        else:
            r_n_self = int(self.num * other.num)  # result numerator self
            r_n_denomr = int(self.denomr * other.denomr)  # result denominator self
        return Fraction(r_n_self, r_n_denomr)

    def __itruediv__(self, other) -> 'Fraction':  # in-place division
        if type(other) != Fraction:
            # make other fraction
            return Fraction(self.num * other.denomr, self.denomr * other.num)
        else:
            r_n_self = int(self.num * other.denomr)  # result numerator self
            r_n_denomr = int(self.denomr * other.num)  # result denominator self
        return Fraction(r_n_self, r_n_denomr)

    def reverse(self) -> 'Fraction':
        self.num, self.denomr = self.denomr, self.num
        return self


# a = Fraction(1, 3)
# b = Fraction(1, 2)
# c = a * b
# print(a, b, c, a is c, b is c)
pass
# 1/3 1/2 1/6 False False
a = Fraction(1, 3)
c = b = Fraction(2, 1).reverse()
b /= a
print(a, b, c, b is c)
# 1/3 3/2 3/2 True
