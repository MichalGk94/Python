#!/bin/usr/python/
# -*- coding: utf-8 -*-

from math import sqrt
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other


class Vector(Point):
    """Klasa reprezentująca wektory na płaszczyźnie."""

    # __init__ dziedziczone
    # __str__ dziedziczone
    def __repr__(self):  # zwraca string "Vector(x, y)"
        return "Vector(%s, %s)" % (self.x, self.y)

    def __add__(self, other):  # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return sqrt(self.x * self.x + self.y * self.y)


# Kod testujący moduł.

p1 = Point(2, 3)
p2 = Point(3, 4)
v1 = Vector(2, 3)
v2 = Vector(3, 4)


class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(p1), "(2, 3)")
        self.assertEqual(str(v1), "(2, 3)")

    def test_repr(self):
        self.assertEqual(repr(p1), "Point(2, 3)")
        self.assertEqual(repr(v1), "Vector(2, 3)")

    def test_equal(self):
        self.assertTrue(p1 == Point(2, 3))
        self.assertTrue(v1 == Vector(2, 3))

    def test_notEq(self):
        self.assertTrue(p1 != p2)
        self.assertTrue(v1 != v2)

    def test_add(self):
        self.assertEqual(v1 + v2, Vector(5, 7))

    def test_sub(self):
        self.assertEqual(v1 - v2, Vector(-1, -1))

    def test_mul(self):
        self.assertEqual(v1 * v2, 18)

    def test_cross(self):
        self.assertEqual(v1.cross(v2), -1)
        self.assertEqual(v1.cross(Vector(3, 5)), 1)
        self.assertEqual(v1.cross(Vector(5, 6)), -3)

    def test_length(self):
        self.assertEqual(v2.length(), 5)

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPoint)
    unittest.TextTestRunner(verbosity=2).run(suite)
