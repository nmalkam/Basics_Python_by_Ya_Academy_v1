class Rectangle:

    def __init__(self, dot_1, dot_2):
        if dot_1[0] < dot_2[0]:
            self.base = dot_2[0] - dot_1[0]
        else:
            self.base = dot_1[0] - dot_2[0]
        if dot_1[1] < dot_2[1]:
            self.height = dot_2[1] - dot_1[1]
        else:
            self.height = dot_1[1] - dot_2[1]
        # self.x1 = dot_1[0]
        # self.y1 = dot_1[1]
        # self.x2 = dot_2[0]
        # self.y2 = dot_2[1]

    def perimeter(self):
        return round((self.height * 2 + self.base * 2), 2)

    def area(self):
        return round(self.height * self.base, 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
# 23.52
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
# 32.14
