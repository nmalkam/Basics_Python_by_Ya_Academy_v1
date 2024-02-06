class Point:
    def __init__(self, x, y) -> None:
        # self.dist_y = 0
        # self.dist_x = 0
        self.x = x
        self.y = y

    def move(self, move_x: int, move_y: int):
        self.x = self.x + move_x
        self.y = self.y + move_y

    def length(self, point_arr) -> int:  # : Callable[[int, int], Point, PatchedPoint]
        return round(((point_arr.x - self.x)**2 + (point_arr.y - self.y)**2)**0.5, 2)


class PatchedPoint(Point):
    def __init__(self, x=0, y=0) -> None:
        super().__init__(x=x, y=y)
        if isinstance(x, tuple):
            self.x, self.y = x[0], x[1]

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y}'


point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))
# (0, 0)
# PatchedPoint(2, -3)
first_point = PatchedPoint((2, -7))  # noqa
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
# (2, -7) (7, 9)
# PatchedPoint(2, -7) PatchedPoint(7, 9)
