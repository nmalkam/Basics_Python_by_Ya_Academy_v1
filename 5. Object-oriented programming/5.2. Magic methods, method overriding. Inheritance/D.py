class Fraction:
    def _gcd(self, a, b):
        """Все поля и методы, не требуемые в задаче,
         следует инкапсулировать
         (называть с использованием ведущих символов нижнего подчёркивания)."""
        ch = a
        zn = b
        while b != 0:
            c = b
            a, b = b, a % b
        return int(ch / c), int(zn / a)

    def __init__(self, *args) -> None:  # numerator, denominator
        #     n, d = self.gcd(n, d)
        #     self.numer = n
        #     self.denomr = d
        if isinstance(args[0], str):
            # self.__num, self.__den = [int(c) for c in args[0].split('/')]
            n, d = map(int, args[0].split('/'))
            self.num, self.denomr = self._gcd(n, d)
        else:
            # first, last = args
            self.num, self.denomr = self._gcd(args[0], args[1])

    def numerator(self, *number):
        if not number:
            return self.num
        else:
            # self.numer = args
            self.num, self.denomr = self._gcd(number[0], self.denomr)
            return self.num, self.denomr

    def denominator(self, *number):
        if not number:
            return self.denomr
        else:
            # self.numer = args
            self.num, self.denomr = self._gcd(self.num, number[0])
            return self.num, self.denomr

    def __str__(self):
        return f'{self.num}/{self.denomr}'

    def __repr__(self):
        return f'Fraction{self.num, self.denomr}'


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))
# # 1/3 Fraction(1, 3)
# # 1/2 Fraction(1, 2)
fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
# # 1/70 Fraction(1, 70)
# # 1 7
# # 1 2
