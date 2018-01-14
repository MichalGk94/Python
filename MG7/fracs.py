#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x = 0., y = 1.):
        if y == 0 or not isinstance(x, (int, long, float)) or not isinstance(y, (int, long, float)):
            raise ValueError
        i = 1.
        while not ((i * x).is_integer() and (i * y).is_integer()):
            i *= 10
        u, v = x * i, y * i
        while v:
            u, v = v, u % v
        u = abs(u)
        self.x = int(x * i / u)
        self.y = int(y * i / u)

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        return "%s/%s" % (self.x, self.y) if self.y != 1 else "%s" % self.x

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac(%s, %s)" % (self.x, self.y)

    def __cmp__(self, other):  # porównywanie
        if isinstance(other, (int, long, float, Frac)):
            if not isinstance(other, Frac):
                other = Frac(other)
            f = (self.x * other.y) / (float(self.y * other.x))
            if f == 1.0:
                return 0
            elif f > 1.0:
                return -1
            else:
                return 1
        else:
            raise ValueError

    def __add__(self, other):  # frac1+frac2
        if isinstance(other, (int, long, float, Frac)):
            if not isinstance(other, Frac):
                other = Frac(other)
            return Frac(self.x * other.y + self.y * other.x, self.y * other.y)
        else:
            raise ValueError

    __radd__ = __add__

    def __sub__(self, other):  # frac1-frac2
        if isinstance(other, (int, long, float, Frac)):
            if not isinstance(other, Frac):
                other = Frac(other)
            return Frac(self.x * other.y - self.y * other.x, self.y * other.y)
        else:
            raise ValueError

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        if isinstance(other, (int, long, float, Frac)):
            return Frac(self.y * other - self.x, self.y)
        else:
            raise ValueError

    def __mul__(self, other):  # frac1*frac2
        if isinstance(other, (int, long, float, Frac)):
            if not isinstance(other, Frac):
                other = Frac(other)
            return Frac(self.x * other.x, self.y * other.y)
        else:
            raise ValueError

    __rmul__ = __mul__

    def __div__(self, other):  # frac1/frac2
        if isinstance(other, (int, long, float, Frac)):
            if not isinstance(other, Frac):
                other = Frac(other)
            return Frac(self.x * other.y, self.y * other.x)
        else:
            raise ValueError

    def __rdiv__(self, other):  # int/frac
        if isinstance(other, (int, long, float, Frac)):
            return Frac(other * self.y, self.x)
        else:
            raise ValueError

    # operatory jednoargumentowe
    def __pos__(self):  # +frac
        return self

    def __neg__(self):  # -frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)


# Kod testujący moduł.

f1 = Frac(2, 3)


class TestFrac(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(f1), "2/3")
        self.assertEqual(str(Frac(0.5)), "1/2")
        self.assertEqual(str(Frac(0.25, 0.5)), "1/2")

    def test_repr(self):
        self.assertEqual(repr(f1), "Frac(2, 3)")

    def test_cmp(self):
        self.assertTrue(f1 == Frac(4, 6))
        self.assertFalse(f1 == Frac(4.5, 6))
        self.assertTrue(f1 == Frac(4.0, 6))
        self.assertFalse(f1 == Frac(5, 6))

    def test_add(self):
        self.assertEqual(f1 + Frac(3, 4), Frac(17, 12))
        self.assertEqual(f1 + 2, Frac(8, 3))
        self.assertEqual(f1 + 1.5, Frac(13, 6))

    def test_radd(self):
        self.assertEqual(2 + f1, Frac(8, 3))
        self.assertEqual(1.5 + f1, Frac(13, 6))

    def test_sub(self):
        self.assertEqual(f1 - Frac(4, 9), Frac(6, 27))
        self.assertEqual(f1 - 2, -Frac(4, 3))
        self.assertEqual(f1 - 1.5, -Frac(5, 6))

    def test_rsub(self):
        self.assertEqual(2 - f1, Frac(4, 3))
        self.assertEqual(1.5 - f1, Frac(5, 6))

    def test_mul(self):
        self.assertEqual(f1 * Frac(3, 4), Frac(6, 12))
        self.assertEqual(f1 * 2, Frac(8, 6))
        self.assertEqual(f1 * 1.5, Frac(1))

    def test_rmul(self):
        self.assertEqual(2 * f1, Frac(4, 3))
        self.assertEqual(1.5 * f1, Frac(1.0, 1.0))

    def test_div(self):
        self.assertEqual(f1 / Frac(3, 4), Frac(8, 9))
        self.assertEqual(f1 / 2, Frac(1, 3))
        self.assertEqual(f1 / 1.5, Frac(4, 9))

    def test_rdiv(self):
        self.assertEqual(2 / f1, Frac(3))
        self.assertEqual(1.5 / f1, Frac(18, 8))

    def test_pos(self):
        self.assertEqual(+f1, Frac(2, 3))

    def test_neg(self):
        self.assertEqual(-f1, Frac(-2, 3))

    def test_inv(self):
        self.assertEqual(~f1, Frac(3, 2))

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFrac)
    unittest.TextTestRunner(verbosity = 2).run(suite)
