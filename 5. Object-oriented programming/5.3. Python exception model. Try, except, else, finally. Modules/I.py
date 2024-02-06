class Fraction:
    # требуется изменить систему инициализации,
    # чтобы она могла воспринимать и целые числа (причём и в виде строк).

    # требуется переработать операторы арифметических действий и сравнения
    def __gcd(self, a, b):
        c = b
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

    # def __ctf(self, *args) -> 'Fraction':  # convert_to_fraction
    #     match len(args):
    #         case 1:
    #             if isinstance(args[0], str):
    #                 if len(args[0]) == 1:
    #                     args.num = int(args[0])
    #                     args.denomr = 1
    #                 else:
    #                     n, d = map(int, args[0].split('/'))
    #                     args.num, args.denomr = self.__gcd(n, d)
    #             else:
    #                 args.num = int(args[0])
    #                 args.denomr = 1
    #         case 2:
    #             args.num, args.denomr = self.__gcd(args[0], args[1])
    #     return Fraction(args.num, args.denomr)

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
        elif type(self) == int:
            return Fraction(self * other.denomr - other.num, other.denomr)
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

    def reverse(self) -> 'Fraction':
        self.num, self.denomr = self.denomr, self.num
        return self


a = Fraction(1, 2)
b = Fraction('2/3')
# c, d = map(Fraction.reverse, (3 - a, 2 / b))
# print(a, b, c, d)
# 1/2 2/3 2/5 1/3
# -----------------------------J
a = Fraction(1)
b = Fraction('2')
# bb = Fraction('2/3')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
# 1/1 2/1 1/3 1/1
# False False
# True True False True
a = Fraction(1, 2)
b = Fraction('2/3')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
# 1/2 2/3 2/5 -3/1
# False True
# False False False False


# Для того чтобы модифицировать наш класс
# чтобы он воспринимал целое число в качестве единсвтенного аргумента необьходимо:
#
# требуется изменить систему инициализации,
# чтобы она могла воспринимать и целые числа (причём и в виде строк).
