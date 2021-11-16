import math


def calculate_circumference(r: float) -> float:
    """ Computes the circumference of a circle with radius r """
    return 2 * math.pi * r


def circle_area(radius: float) -> float:
    """ Calculates the area of a circle with the given radius """
    return math.pi * (radius**2)


def rectangle_area(a, b):
    return a * b


def square_perimeter(side_length):
    """ Returns the perimeter of a square """
    return side_length * 4


def fibonacci(n):
    """ Calculates the nth number of the fibonacci sequence """
    if n < 0:
        raise ValueError("Invalid input")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
