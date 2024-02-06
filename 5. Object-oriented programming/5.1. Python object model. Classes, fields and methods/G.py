class Rectangle:
    def __init__(self, corner1, corner2) -> None:
        self.left_up = min(corner1[0], corner2[0]), max(corner1[1], corner2[1])
        # self.right_down = max(corner1[0], corner2[0]), min(corner1[1], corner2[1])
        self.width = round(abs(corner1[0] - corner2[0]), 2)
        self.height = round(abs(corner1[1] - corner2[1]), 2)
        self.center = round(self.left_up[0] + self.width / 2, 2), round(self.left_up[1] - self.height / 2, 2)

    def perimeter(self):
        return round(self.width * 2 + self.height * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):  # верхний левый угол
        return self.left_up

    def get_size(self):  # возвращает размеры в виде кортежа
        # print(tuple(round(self.get_pos()[1] - self.left_down[1], 2)))
        return self.width, self.height

    def move(self, dx, dy):
        self.left_up = round(self.left_up[0] + dx, 2), round(self.left_up[1] + dy, 2)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def turn(self):
        self.width, self.height = self.height, self.width
        self.left_up = round(self.center[0] - self.width / 2, 2), round(self.center[1] + self.height / 2, 2)

    def scale(self, factor):
        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)
        self.left_up = round(self.center[0] - self.width / 2, 2), round(self.center[1] + self.height / 2, 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
# (-3.14, 2.71)
# (6.28, 5.42)
# (-2.71, 3.14)
# (5.42, 6.28)
# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.scale(2.0)
# print(rect.get_pos(), rect.get_size(), sep='\n')
# (-3.14, 2.71)
# (6.28, 5.42)
# (-6.28, 5.42)
# (12.56, 10.84)
