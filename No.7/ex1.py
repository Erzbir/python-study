from math import pi


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * self.__width + 2 * self.__length


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * pi

    def circum(self):
        return self.__radius * 2 * pi


rectangle = Rectangle(1, 2)
print(f"长方形的面积为{rectangle.area()}")
print(f"长方形的周长为{rectangle.perimeter()}")
circle = Circle(3)
print(f"圆的面积为{circle.area()}")
print(f"圆的周长为{circle.circum()}")
