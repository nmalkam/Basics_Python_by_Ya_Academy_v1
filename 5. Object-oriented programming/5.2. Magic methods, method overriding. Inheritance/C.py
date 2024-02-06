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

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


point = PatchedPoint()
print(point)
# print(repr(point))
new_point = point + (2, -3)
print(point, new_point, point is new_point)
# (0, 0)
# (0, 0) (2, -3) False
first_point = second_point = PatchedPoint((2, -7))  # noqa
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
# (9, -4) (9, -4) True
