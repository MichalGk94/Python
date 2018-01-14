#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c = 0., n = 0):
        if n < 0 or not isinstance(c, (int, long, float)) or not isinstance(n, (int, long)):
            raise ValueError
        self.size = n + 1  # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size - 1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other):  # poly1+poly2
        if isinstance(other, (int, long, float, Poly)):
            if not isinstance(other, Poly):
                other = Poly(other)
            poly = Poly(0, max(self.size, other.size) - 1)
            for i in range(self.size):
                poly.a[i] += self.a[i]
            for i in range(other.size):
                poly.a[i] += other.a[i]
            return poly
        else:
            raise ValueError

    __radd__ = __add__

    def __sub__(self, other):  # poly1-poly2
        if isinstance(other, (int, long, float, Poly)):
            if not isinstance(other, Poly):
                other = Poly(other)
            poly = Poly(0, max(self.size, other.size) - 1)
            for i in range(self.size):
                poly.a[i] += self.a[i]
            for i in range(other.size):
                poly.a[i] -= other.a[i]
            return poly
        else:
            raise ValueError

    def __rsub__(self, other):
        if isinstance(other, (int, long, float, Poly)):
            if not isinstance(other, Poly):
                other = Poly(other)
            poly = Poly(0, max(self.size, other.size) - 1)
            for i in range(self.size):
                poly.a[i] -= self.a[i]
            for i in range(other.size):
                poly.a[i] += other.a[i]
            return poly
        else:
            raise ValueError

    def __mul__(self, other):  # poly1*poly2
        if isinstance(other, (int, long, float, Poly)):
            if not isinstance(other, Poly):
                other = Poly(other)
            poly = Poly(0, self.size + other.size - 1)
            for i in range(self.size):
                for j in range(other.size):
                    poly.a[i + j] += self.a[i] * other.a[j]
            return poly
        else:
            raise ValueError

    __rmul__ = __mul__

    def __pos__(self):  # +poly1
        return self

    def __neg__(self):  # -poly1
        for i in range(self.size):
            self.a[i] = -self.a[i]
        return self

    def is_zero(self):  # bool, True dla [0], [0, 0],...
        for x in self.a:
            if x != 0:
                return False
        return True

    def __eq__(self, other):  # obsługa poly1 == poly2
        if isinstance(other, (int, long, float, Poly)):
            if not isinstance(other, Poly):
                other = Poly(other)
            poly = self.a if self.size >= other.size else other.a
            m = min(self.size, other.size)
            for i in range(m, max(self.size, other.size)):
                if poly[i] != 0:
                    return False
            for i in range(m):
                if self.a[i] != other.a[i]:
                    return False
            return True
        else:
            raise ValueError

    def __ne__(self, other):  # obsługa poly1 != poly2
        return not self == other

    def eval(self, x):  # schemat Hornera
        if isinstance(x, (int, long, float)):
            if self.size == 1:
                return self.a[0]
            result = 0
            for i in self.a[::-1]:
                result = i + x * result
            return result
        else:
            raise ValueError

    def combine(self, other):  # złożenie poly1(poly2(x))
        if isinstance(other, Poly):
            poly = Poly(0, 0)
            tmp = Poly(0, 0)
            for i in self.a[::-1]:
                tmp.a[0] = i
                poly = tmp + other * poly
            return poly
        else:
            raise ValueError

    def __pow__(self, n):  # poly(x)**n lub pow(poly(x),n)
        if isinstance(n, (int, long, float)):
            poly = Poly(1, 0)
            for i in range(n):
                poly = self * poly
            return poly
        else:
            raise ValueError("Wrong n must be int, long or float")

    def diff(self):  # różniczkowanie
        if self.size == 1:
            return Poly(0, 0)
        poly = Poly(0, self.size - 1)
        for i in range(poly.size - 1):
            poly.a[i] = (i + 1) * self.a[i + 1]
        return poly

    def integrate(self):  # całkowanie
        poly = Poly(0, self.size + 1)
        for i in range(self.size):
            poly.a[i + 1] = 1 / float((i + 1)) * self.a[i]
        return poly

    def __len__(self):
        return self.size  # len(poly), rozmiar self.a

    def __getitem__(self, i):
        if not isinstance(i, int):
            raise ValueError
        return self.a[i]

    def __setitem__(self, i, value):
        if not isinstance(i, int) or isinstance(value, (int, long, float)):
            raise ValueError
        if i < 0 or i > self.size:
            raise IndexError
        self.a[i] = value

    def __call__(self, x):
        if isinstance(x, (int, long, float)):
            return self.eval(x)
        elif isinstance(x, Poly):
            return self.combine(x)
        else:
            raise ValueError

            # dla isinstance(x, (int,long,float)) odpowiada eval(),
            # dla isinstance(x, Poly) odpowiada combine()


# Kod testujący moduł.
p1 = Poly(3, 4) + Poly(2, 2)


class TestPoly(unittest.TestCase):
    def setUp(self):
        self.p2 = Poly(0, 6)
        self.p2.a[4] = 3
        self.p2.a[2] = 2

    def test__str(self):
        self.assertEqual(str(p1), "[0, 0, 2, 0, 3]")

    def test_add(self):
        self.assertEqual(Poly(2, 2) + Poly(3, 4), self.p2)
        self.assertEqual(self.p2 + 2, self.p2 + Poly(2, 0))
        self.assertEqual(self.p2 + 2.5, self.p2 + Poly(2.5, 0))
        self.assertEqual(2 + self.p2, Poly(2, 0) + self.p2)
        self.assertEqual(2.5 + self.p2, Poly(2.5, 0) + self.p2)

    def test_sub(self):
        self.assertEqual(Poly(3, 4) - Poly(-2, 2), self.p2)
        self.assertEqual(self.p2 - 2, self.p2 - Poly(2, 0))
        self.assertEqual(self.p2 - 2.5, self.p2 - Poly(2.5, 0))
        self.assertEqual(2 - self.p2, Poly(2, 0) - self.p2)
        self.assertEqual(2.5 - self.p2, Poly(2.5, 0) - self.p2)

    def test_mul(self):
        poly = Poly(0, 8)
        poly.a[7] = 12
        poly.a[5] = 8
        self.assertEqual(Poly(3, 5) * Poly(4, 3), Poly(12, 8))
        poly = Poly(7.5, 4) + Poly(5, 2)
        self.assertEqual(self.p2 * 2, self.p2 + self.p2)
        self.assertEqual(self.p2 * 2.5, poly)

    def test_pos(self):
        self.assertEqual(+self.p2, self.p2)

    def test_neg(self):
        self.assertEqual(-Poly(-2, 2), Poly(2, 2))

    def test_eq(self):
        self.assertTrue(Poly(2, 2) == Poly(2, 2))
        self.assertTrue(Poly(2, 0) == 2)
        self.assertTrue(-2.5 == Poly(-2.5, 0))
        self.assertFalse(Poly(2, 2) == Poly(-2, 2))

    def test_ne(self):
        self.assertFalse(Poly(2, 2) != Poly(2, 2))
        self.assertFalse(Poly(2, 0) != 2)
        self.assertFalse(-2.5 != Poly(-2.5, 0))
        self.assertTrue(Poly(2, 2) != Poly(-2, 2))

    def test_pow(self):
        poly = Poly(27, 12)
        poly.a[10] = 54
        poly.a[8] = 36
        poly.a[6] = 8
        self.assertEqual(Poly(2, 2) ** 3, Poly(8, 6))
        self.assertEqual(self.p2 ** 3, poly)

    def test_eval(self):
        self.assertEqual(Poly(3, 4).eval(2), 48)
        self.assertEqual(self.p2.eval(2), 56)

    def test_comb(self):
        self.assertEqual(Poly(3, 4).combine(Poly(2, 2)), Poly(48, 8))

    def test_diff(self):
        self.assertEqual(Poly(3, 4).diff(), Poly(12, 3))

    def test_integrate(self):
        self.assertEqual(Poly(8, 3).integrate(), Poly(2, 4))

    def test_zero(self):
        self.assertFalse(Poly(2, 2).is_zero())
        self.assertFalse(self.p2.is_zero())
        self.assertTrue(Poly(0, 8).is_zero())

    def test_len(self):
        self.assertEqual(len(p1), 5)

    def test_get(self):
        self.assertEqual(p1[0], 0)
        self.assertEqual(p1[2], 2)
        self.assertEqual(p1[4], 3)

    def test_set(self):
        p1[2] = 3
        self.assertEqual(p1[2], 3)
        p1[3] = 1
        self.assertEqual(p1[2], 3)
        p1[4] = 2
        self.assertEqual(p1[2], 3)

    def test_call(self):
        self.assertEqual(Poly(3, 4)(2), 48)
        self.assertEqual(self.p2(2), 56)

    def tearDown(self): pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPoly)
    unittest.TextTestRunner(verbosity = 2).run(suite)
