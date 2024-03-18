#!/usr/bin/python3
"""
    Defines a square class
"""
class square():
    """Defines  a square object
        Attributes:
        width = width of the square
        length = length of the square
    """
    width = 0
    length = 0

    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.length

    def PermiterOfMySquare(self):
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
