#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1 = 0., y1 = 0., x2 = 0., y2 = 0., x3 = 0., y3 = 0.):
        if not (isinstance(x1, (int, long, float)) or isinstance(x1, (int, long, float)) or isinstance(x1, (
                int, long, float)) or isinstance(x1, (int, long, float)) or isinstance(x1, (
                int, long, float)) or isinstance(x1, (int, long, float))):
            raise ValueError
        try:
            if x1 == x2 == x3 or y1 == y2 == y3 or (y2 - y1) / float(x2 - x1) == (y3 - y1) / float(x3 - x1):
                raise ValueError("Punkty sa wspolliniowe")
        except ZeroDivisionError:
            pass
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[%s, %s, %s]" % (self.pt1, self.pt2, self.pt3)

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle(%s, %s, %s, %s, %s, %s)" % (
            self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):  # obsługa tr1 == tr2
        if isinstance(other, Triangle):
            return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3
        else:
            raise ValueError("Nieprawidłowy typ " + str(type(other)) + " Oczekiwano Rectangle")

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    def center(self):  # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3., (self.pt1.y + self.pt2.y + self.pt3.y) / 3.)

    def area(self):  # pole powierzchni
        return abs(0.5 * float((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) -
                               (self.pt3.x - self.pt1.x) * (self.pt2.y - self.pt1.y)))

    def move(self, x, y):  # przesunięcie o (x, y)
        if isinstance(x, (int, long, float)) and isinstance(y, (int, long, float)):
            self.pt1.x += x
            self.pt2.x += x
            self.pt3.x += x
            self.pt1.y += y
            self.pt2.y += y
            self.pt3.y += y
        else:
            raise ValueError

    def make4(self):  # zwraca listę czterech mniejszych
        x1 = min(self.pt1.x, self.pt2.x) + abs(self.pt1.x - self.pt2.x) / 2.
        y1 = min(self.pt1.y, self.pt2.y) + abs(self.pt1.y - self.pt2.y) / 2.
        x2 = min(self.pt2.x, self.pt3.x) + abs(self.pt2.x - self.pt3.x) / 2.
        y2 = min(self.pt2.y, self.pt3.y) + abs(self.pt2.y - self.pt3.y) / 2.
        x3 = min(self.pt3.x, self.pt1.x) + abs(self.pt3.x - self.pt1.x) / 2.
        y3 = min(self.pt3.y, self.pt1.y) + abs(self.pt3.y - self.pt1.y) / 2.
        return [
            Triangle(self.pt1.x, self.pt1.y, x1, y1, x3, y3),
            Triangle(x1, y1, self.pt2.x, self.pt2.y, x2, y2),
            Triangle(x3, y3, x2, y2, self.pt3.x, self.pt3.y),
            Triangle(x1, y1, x3, y3, x2, y2)
        ]


# Kod testujący moduł.
t1 = Triangle(-1, 0, 3, -1, 4, 7)


class TestTriangle(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(t1), "[(-1, 0), (3, -1), (4, 7)]")

    def test_repr(self):
        self.assertEqual(repr(t1), "Triangle(-1, 0, 3, -1, 4, 7)")

    def test_eq(self):
        self.assertTrue(t1 == Triangle(-1, 0, 3, -1, 4, 7))

    def test_ne(self):
        self.assertTrue(t1 != Triangle(-1, 0, 3, 2, 1, 4))

    def test_center(self):
        self.assertEqual(t1.center(), Point(2, 2))

    def test_area(self):
        self.assertEqual(t1.area(), 16.5)

    def test_zmove(self):
        t1.move(2, 3)
        self.assertEqual(t1, Triangle(1, 3, 5, 2, 6, 10))

    def test_make4(self):
        l = [Triangle(-1, 0, 1, -0.5, 1.5, 3.5), Triangle(1, -0.5, 3, -1, 3.5, 3), Triangle(1.5, 3.5, 3.5, 3, 4, 7),
             Triangle(1, -0.5, 1.5, 3.5, 3.5, 3)]
        self.assertEqual(t1.make4(), l)

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangle)
    unittest.TextTestRunner(verbosity = 2).run(suite)
