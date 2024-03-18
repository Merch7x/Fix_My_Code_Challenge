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

    def __init__(self, *args, **kwargs):
        """Instanciates a square object"""
        self.width = kwargs.get('width', 0)
        self.length = kwargs.get('length', 0)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.length

    def perimeter_Of_my_quare(self):
        """Permeter of the square"""
        return (self.width * 2) + (self.length * 2)

    def __str__(self):
        """String represenation of the squares dimensions"""
        return "{}/{}".format(self.width, self.length)


if __name__ == "__main__":

    s = square(width=12, length=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
