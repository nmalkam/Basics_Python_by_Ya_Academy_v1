class Rectangle:
    def __init__(self, corner1, corner2) -> None:
        self.left_up = min(corner1[0], corner2[0]), max(corner1[1], corner2[1])
        self.width = round(abs(corner1[0] - corner2[0]), 2)
        self.height = round(abs(corner1[1] - corner2[1]), 2)

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

# изменяет размер (положение верхнего левого угла остаётся неизменным).
    def resize(self, width, height):
        self.width = width
        self.height = height


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
# (3.2, 3.14) (4.32, 7.44)
# (4.52, -1.86) (4.32, 7.44)
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
# (3.2, 3.14) (4.32, 7.44)
# (3.2, 3.14) (23.5, 11.3)
