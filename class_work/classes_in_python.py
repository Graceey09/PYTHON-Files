# class Point:
#     # constructor
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     # Instance
#     def draw(self):
#         print(f"drawing from poit {self.a} to {self.b}")
#
#     def __str__(self):
#         return f"({self.a}, {self.b})"
#
#
# p1 = Point(1, 2)
# p2 = Point(5, 6)
# print(p1)
# print(p2)


class Point:
    color = "blue"

    def __init__(self, point_a, point_b):
        self.__point_a = point_a
        self.__point_b = point_b

        @property
        def point_a(self):
            return self.__point_a

        @point_a.setter
        def point_a(self, value):
            if value < 0:
                raise ValueError("value cannot be negative")
            self.__point_a = value

        def draw(self):
            print(f"drawing from point {self.point_a} to {self.point_b}")

        def __str__(self):
            return f"({self.__point_a}, {self.__point_b})"

        def __add__(self, other):
            return f"({self.__point_a + self.__point_a}, {self.__point_b + self.__point_b})"

    def __eq__(self, other):
        return self.__point_a == other.point_a and self.__point_b == other.__point_b

    @property
    def point_b(self):
        return self.__point_a

    @point_b.setter
    def point_b(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__point_b = value


Point.color = "red"
p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1.point_a)
print(p2.color)
print(p1 + p2)
