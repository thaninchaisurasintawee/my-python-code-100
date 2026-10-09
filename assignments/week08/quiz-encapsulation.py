"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return 2 * (self.__length + self.__width)

    def isSquare(self):
        return self.__length == self.__width

myrectangle = Rectangle(5, 10)
print(myrectangle.getArea())

myrectangle2 = Rectangle(5, 5)
print(myrectangle2.isSquare())