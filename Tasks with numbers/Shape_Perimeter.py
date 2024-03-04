from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.redius = radius

    def area(self):
        return self.redius ** 2 * math.pi

    def perimeter(self):
        return 2 * math.pi * self.redius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


if __name__ == "__main__":
    rectangle = Rectangle(4, 6)
    print("Rectangle - Area:", rectangle.area(), "Perimeter:", rectangle.perimeter())

    circle = Circle(5)
    print("Circle - Area:", circle.area(), "Perimeter:", circle.perimeter())

    triangle = Triangle(3, 4, 5)
    print("Triangle - Area:", triangle.area(), "Perimeter:", triangle.perimeter())
