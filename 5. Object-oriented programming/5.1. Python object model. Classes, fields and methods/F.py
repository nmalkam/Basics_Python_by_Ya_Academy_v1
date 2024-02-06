class Rectangle:
    def __init__(self, corner1, corner2) -> None:
        self.left_down = min(corner1[0], corner2[0]), min(corner1[1], corner2[1])
        self.right_up = max(corner1[0], corner2[0]), max(corner1[1], corner2[1])

    def perimeter(self):
        return round((self.right_up[0] - self.left_down[0]) * 2 +
                     (self.right_up[1] - self.left_down[1]) * 2, 2)

    def area(self):
        return round((self.right_up[0] - self.left_down[0]) *
                     (self.right_up[1] - self.left_down[1]), 2)

    def get_pos(self):  # верхний левый угол
        return round(self.left_down[0], 2), round(self.right_up[1], 2)

    def get_size(self):  # возвращает размеры в виде кортежа
        # print(tuple(round(self.get_pos()[1] - self.left_down[1], 2)))
        return round(self.right_up[0] - self.left_down[0], 2), \
               round(self.get_pos()[1] - self.left_down[1], 2),

    def move(self, dx, dy):
        self.left_down = (self.left_down[0] + dx), (self.left_down[1] + dy)
        self.right_up = (self.right_up[0] + dx), (self.right_up[1] + dy)

# изменяет размер (положение верхнего левого угла остаётся неизменным).
    def resize(self, width, height):
        self.left_down = self.left_down[0], self.get_pos()[1] - height
        self.right_up = self.get_pos()[0] + width, self.right_up[1]
# ОШИБКА !!!!!!!!!     (-0.0, 23.5)
# должно получиться         # (3.2, 3.14) (23.5, 11.3)


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
