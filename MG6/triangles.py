#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[%s, %s, %s]" % (self.pt1, self.pt2, self.pt3)

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle(%s, %s, %s, %s, %s, %s)" % (
            self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):  # obsługa tr1 == tr2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3
        # wersja z przesunięciem
        # return self.pt1.x - self.pt2.x == other.pt1.x - other.pt2.x and \
        #       self.pt1.y - self.pt2.y == other.pt1.y - other.pt2.y and \
        #       self.pt2.x - self.pt3.x == other.pt2.x - other.pt3.x and \
        #       self.pt2.y - self.pt3.y == other.pt2.y - other.pt3.y and \
        #       self.pt3.x - self.pt1.x == other.pt3.x - other.pt1.x and \
        #       self.pt3.y - self.pt1.y == other.pt3.y - other.pt1.y'''

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    def center(self):  # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):  # pole powierzchni
        return 0.5 * ((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) -
                      (self.pt3.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt3.x += x
        self.pt1.y += y
        self.pt2.y += y
        self.pt3.y += y


t1 = Triangle(-1, 0, 3, 0, 1, 4)


# Kod testujący moduł.


class TestTriangle(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(t1), "[(-1, 0), (3, 0), (1, 4)]")

    def test_repr(self):
        self.assertEqual(repr(t1), "Triangle(-1, 0, 3, 0, 1, 4)")

    def test_eq(self):
        self.assertTrue(t1 == Triangle(-1, 0, 3, 0, 1, 4))
        # testy dla drugiej wersji
        # self.assertTrue(t1 == Triangle(0, 2, 4, 2, 2, 6))
        # self.assertTrue(t1 == Triangle(-4, 1, 0, 1, -2, 5))

    def test_ne(self):
        self.assertTrue(t1 != Triangle(-1, 0, 3, 2, 1, 4))

    def test_center(self):
        self.assertEqual(t1.center(), Point(1, 1))

    def test_area(self):
        self.assertEqual(t1.area(), 8)

    def test_zmove(self):  # nazwa taka, bo wywołuje alfabetycznie i str oraz repr wykona na zmodyfikowanym t1
        t1.move(2, 3)
        self.assertEqual(t1, Triangle(1, 3, 5, 3, 3, 7))

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangle)
    unittest.TextTestRunner(verbosity=2).run(suite)
