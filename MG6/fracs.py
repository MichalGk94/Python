#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        return "%s/%s" % (self.x, self.y) if self.y != 1 else "%s" % self.x

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac(%s, %s)" % (self.x, self.y)

    def __cmp__(self, other):  # porównywanie
        if self.y == 0 or other.y == 0:
            raise ValueError
        f = (self.x * other.y) / (float(self.y * other.x))
        if f == 1.0:
            return 0
        elif f > 1.0:
            return -1
        else:
            return 1

    def __add__(self, other):  # frac1+frac2
        if self.y == 0 or other.y == 0:
            raise ValueError
        return Frac(self.x + other.x, self.y) if self.y == other.y \
            else Frac(self.x * other.y + self.y * other.x, self.y * other.y)

    def __sub__(self, other):  # frac1-frac2
        if self.y == 0 or other.y == 0:
            raise ValueError
        return Frac(self.x - other.x, self.y) if self.y == other.y \
            else Frac(self.x * other.y - self.y * other.x, self.y * other.y)

    def __mul__(self, other):  # frac1*frac2
        if self.y == 0 or other.y == 0:
            raise ValueError
        return Frac(self.x * other.x, self.y * other.y)

    def __div__(self, other):  # frac1/frac2
        if self.y == 0 or other.y == 0:
            raise ValueError
        return Frac(self.x * other.y, self.y * other.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac
        return self

    def __neg__(self):  # -frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    # dwa razy cmp??
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    def __float__(self):  # float(frac)
        if self.y == 0:
            raise ValueError
        return self.x / float(self.y)


# Kod testujący moduł.

f1 = Frac(2, 3)


class TestFrac(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(f1), "2/3")

    def test_repr(self):
        self.assertEqual(repr(f1), "Frac(2, 3)")

    def test_cmp(self):
        print f1 == Frac(4, 6)
        self.assertTrue(f1 == Frac(4, 6))
        self.assertFalse(f1 == Frac(5, 6))

    def test_add(self):
        self.assertEqual(f1 + Frac(3, 4), Frac(17, 12))

    def test_sub(self):
        self.assertEqual(f1 - Frac(4, 9), Frac(6, 27))

    def test_mul(self):
        self.assertEqual(f1 * Frac(3, 4), Frac(6, 12))

    def test_div(self):
        self.assertEqual(f1 / Frac(3, 4), Frac(8, 9))

    def test_pos(self):
        self.assertEqual(+f1, Frac(2, 3))

    def test_neg(self):
        self.assertEqual(-f1, Frac(-2, 3))

    def test_inv(self):
        self.assertEqual(~f1, Frac(3, 2))

    def test_float(self):
        self.assertEqual(float(Frac(-3, 4)), -0.75)

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFrac)
    unittest.TextTestRunner(verbosity=2).run(suite)
