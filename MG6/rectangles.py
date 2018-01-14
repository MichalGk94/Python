#!/usr/bin/python
# -*- coding: utf-8 -*-

from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[%s, %s]" % (self.pt1, self.pt2)

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(%s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):  # obsługa rect1 == rect2
        #    return self.pt1 == other.pt1 and self.pt2 == other.pt2
        return self.pt1.x - self.pt2.x == other.pt1.x - other.pt2.x and \
               self.pt1.y - self.pt2.y == other.pt1.y - other.pt2.y

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x - self.pt2.x) / 2, (self.pt1.y - self.pt2.y) / 2)

    def area(self):  # pole powierzchni
        return (self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y


# Kod testujący moduł.

r1 = Rectangle(3, 3, -1, 1)


class TestRectangle(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(r1), "[(3, 3), (-1, 1)]")

    def test_repr(self):
        self.assertEqual(repr(r1), "Rectangle(3, 3, -1, 1)")

    def test_eq(self):
        self.assertTrue(r1 == Rectangle(3, 3, -1, 1))
        self.assertTrue(r1 == Rectangle(6, 6, 2, 4))

    def test_ne(self):
        self.assertTrue(r1 != Rectangle(3, 3, -2, 1))

    def test_center(self):
        self.assertEqual(r1.center(), Point(2, 1))

    def test_area(self):
        self.assertEqual(r1.area(), 8)

    def test_zmove(self):
        r1.move(-5, 2)
        self.assertEqual(r1, Rectangle(-2, 5, -6, 3))

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRectangle)
    unittest.TextTestRunner(verbosity=2).run(suite)
