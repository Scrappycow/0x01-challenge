#!/usr/bin/python3
""" Defines Square class"""

class square():
    """ Square class"""
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ instantatiate square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ printable rep of square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Creates square object """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
