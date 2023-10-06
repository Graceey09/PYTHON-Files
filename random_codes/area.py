import math


def area(radius):
    if type(radius) is not int and type(radius) is not float:
        raise TypeError("Pass only number values")
    if radius < 0:
        raise ValueError("Do not input negative values")
    return math.pi * (radius ** 2)


area(5)
