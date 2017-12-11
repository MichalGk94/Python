from points import Point
import math

class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x, y, radius=1):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        print "Circle(" + repr(self.pt.x) + ", " + repr(self.pt.y) + ", " + repr(self.radius) + ")"       # "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius^^2           # pole powierzchni

    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y     # przesuniecie o (x, y)

    def cover(self, other): pass   # okrąg pokrywający oba
