class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, move_x, move_y):
        self.x = self.x + move_x
        self.y = self.y + move_y

    def length(self, point_arr):
        return round(((point_arr.x - self.x)**2 + (point_arr.y - self.y)**2)**0.5, 2)


# point = Point(3, 5)
# print(point.x, point.y)
# point.move(2, -3)
# print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))

