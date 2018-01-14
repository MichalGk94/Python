#!/usr/bin/python
# -*- coding: utf-8 -*-

from points import Point
from math import pi
from math import sqrt
import unittest


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x = 0, y = 0, radius = 1):
        if isinstance(x, (int, long, float) and isinstance(y, (int, long, float)) and isinstance(radius, (
                int, long, float))):
            if radius < 0:
                raise ValueError("promień ujemny")
            self.pt = Point(x, y)
            self.radius = radius
        else:
            raise ValueError

    def __repr__(self):  # "Circle(x, y, radius)"
        return "Circle(%s, %s, %s)" % (self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.pt == other.pt and self.radius == other.radius
        else:
            raise ValueError

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return pi * self.radius ** 2

    def move(self, x, y):  # przesuniecie o (x, y)
        if isinstance(x, (int, long, float)) and isinstance(y, (int, long, float)):
            self.pt.x += x
            self.pt.y += y
        else:
            raise ValueError

    def cover(self, other):  # okrąg pokrywający oba
        if isinstance(other, Circle):
            return Circle(min(self.pt.x, other.pt.x) + abs(self.pt.x - other.pt.x) / 2,
                          min(self.pt.y, other.pt.y) + abs(self.pt.y - other.pt.y) / 2,
                          (self.radius + other.radius + sqrt((self.pt.x - other.pt.x) ** 2 +
                                                             (self.pt.y - other.pt.y) ** 2)) / 2)
        else:
            raise ValueError


# Kod testujący moduł.

c1 = Circle(2, 4, 3)


class TestCircle(unittest.TestCase):
    def setUp(self): pass

    def test_repr(self):
        self.assertEqual(repr(c1), "Circle(2, 4, 3)")

    def test_eq(self):
        self.assertTrue(c1 == Circle(2, 4, 3))

    def test_ne(self):
        self.assertTrue(c1 != Circle(2, 5, 3))

    def test_area(self):
        self.assertEqual(c1.area(), pi * 9)

    def test_xmove(self):
        c1.move(-2, -4)
        self.assertEqual(c1, Circle(0, 0, 3))

    def test_cover(self):
        self.assertEqual(c1.cover(Circle(5, 8, 2)), Circle(3, 6, 5))

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCircle)
    unittest.TextTestRunner(verbosity = 2).run(suite)
