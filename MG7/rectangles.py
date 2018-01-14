#!/usr/bin/python
# -*- coding: utf-8 -*-

from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        if not (isinstance(x1, (int, float, long)) or isinstance(y1, (int, float, long)) or isinstance(x2, (
                int, float, long)) or isinstance(y2, (int, float, long))):
            raise ValueError("Nieprawidlowy typ")
        if x1 > x2:
            x1, x2 = x2, x1
        elif y1 > y2:
            y1, y2 = y2, y1
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[(%s, %s), (%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(%s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):  # obsługa rect1 == rect2
        if isinstance(other, Rectangle):
            return self.pt1.x - self.pt2.x == other.pt1.x - other.pt2.x and \
                   self.pt1.y - self.pt2.y == other.pt1.y - other.pt2.y
        else:
            raise ValueError("Nieprawidlowy typ " + str(type(other)))

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point(self.pt1.x + (self.pt2.x - self.pt1.x) / 2., self.pt1.y + (self.pt2.y - self.pt1.y) / 2.)

    def area(self):  # pole powierzchni
        return (self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        if isinstance(x, (int, float, long)) and isinstance(y, (int, float, long)):
            self.pt1.x += x
            self.pt2.x += x
            self.pt1.y += y
            self.pt2.y += y
        else:
            raise ValueError("Oczekiwano liczby")

    def intersection(self, other):  # część wspólna prostokątów
        if isinstance(other, Rectangle):
            if self.pt2.x < other.pt1.x or other.pt2.x < self.pt1.x or self.pt2.y < other.pt1.y or other.pt2.y < \
                    self.pt1.y:
                return Rectangle()
            return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y),
                             min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
        else:
            raise ValueError("Nieprawdliwy typ. Oczekiwano Rectangle")

    def cover(self, other):  # prostąkąt nakrywający oba
        if isinstance(other, Rectangle):
            return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y),
                             max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
        else:
            raise ValueError("Nieprawidlowy typ. Oczekiwano Rectangle")

    def make4(self):  # zwraca listę czterech mniejszych
        return [Rectangle(self.pt1.x, self.pt1.y,
                          self.pt1.x + abs(self.pt2.x - self.pt1.x) / 2,
                          self.pt1.y + abs(self.pt2.y - self.pt1.y) / 2),
                Rectangle(self.pt1.x, self.pt1.y + abs(self.pt2.y - self.pt1.y) / 2,
                          self.pt1.x + abs(self.pt2.x - self.pt1.x) / 2, self.pt2.y),
                Rectangle(self.pt1.x + abs(self.pt2.x - self.pt1.x) / 2, self.pt1.y,
                          self.pt2.x, self.pt1.y + abs(self.pt2.y - self.pt1.y) / 2),
                Rectangle(self.pt1.x + abs(self.pt2.x - self.pt1.x) / 2,
                          self.pt1.y + abs(self.pt2.y - self.pt1.y) / 2,
                          self.pt2.x, self.pt2.y)
                ]


# Kod testujący moduł.

r1 = Rectangle(2, 2, 6, 8)


class TestRectangle(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(r1), "[(2, 2), (6, 8)]")

    def test_repr(self):
        self.assertEqual(repr(r1), "Rectangle(2, 2, 6, 8)")

    def test_eq(self):
        self.assertTrue(r1 == Rectangle(2, 2, 6, 8))

    def test_ne(self):
        self.assertTrue(r1 != Rectangle(2, 2, 5, 8))

    def test_center(self):
        self.assertEqual(r1.center(), Point(4, 5))

    def test_area(self):
        self.assertEqual(r1.area(), 24)

    def test_xmove(self):
        r2 = Rectangle(0, -2, 4, 4)
        r2.move(2, 4)
        self.assertEqual(r2, Rectangle(2, 2, 6, 8))

    def test_intersection(self):
        self.assertEqual(r1.intersection(Rectangle(4, 1, 8, 5)), Rectangle(4, 2, 6, 5))

    def test_cover(self):
        self.assertEqual(r1.cover(Rectangle(4, 1, 8, 5)), Rectangle(2, 1, 8, 8))

    def test_make4(self):
        self.assertEqual(r1.make4(),
                         [Rectangle(2, 2, 4, 5), Rectangle(2, 5, 4, 8), Rectangle(4, 2, 6, 5), Rectangle(4, 5, 6, 8)])

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRectangle)
    unittest.TextTestRunner(verbosity = 2).run(suite)
