import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    # Initialize the Rectangle object with given length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculate and return the area of the rectangle using the formula: length * width
    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    