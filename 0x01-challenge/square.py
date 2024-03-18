#!/usr/bin/python3
"""
    Defines a square class
"""


class Square():
    """Defines  a square object.

    Attributes:
        width (int): width of the square
        length (int): length of the square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Instanciates a square object"""
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Permeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String represenation of the squares dimensions"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
