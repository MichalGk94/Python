#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt
from random import uniform

"ZADANIE 1"


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0:
        return "Rownanie nie posiada rozwiazan"
    elif a == 0:
        return "Rozwiazaniem rownania jest zbior wszystkich par postaci (x, %s)" % (c / float(b))
    elif b == 0:
        return "Rozwiazaniem rownania jest zbior wszystkich par postaci (x, %s)" % (c / float(a))
    else:
        return "Rozwiazaniem rownania jest zbior wszystkich par postaci (%s, %s)" % (a / float(b), c / float(b))


"ZADANIE 2"


def solve2(a, b, c):
    """Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
    if a == 0:
        return "To nie jest rownanie kwadratowe (a = 0)"
    delta = b * b - 4 * a * c
    if delta == 0:
        return "Rownanie ma 1 rozwiazanie x = %s" % (-b / 2. * a)
    elif delta < 0:
        return "Rownanie nie ma rozwiazan"
    else:
        delta = sqrt(delta)
        return "Rownanie ma 2 rozwiazania x1 = %s oraz x2 = %s" % ((-b + delta) / 2. * a, (-b - delta) / 2. * a)


"ZADANIE 3"


def calc_pi(n = 100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    count = 0.
    for i in range(n):
        x, y = uniform(0, 1), uniform(0, 1)
        if x * x + y * y <= 1:
            count += 1
    return 4. * count / float(n)


"ZADANIE 4"


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b < c or a + c < b or b + c < a:
        raise ValueError("Nie mozna utworzyc trojkata")
    p = 0.5 * (a + b + c)
    return sqrt(p * (p - a) * (p - b) * (p - c))


"ZADANIE 5"


def ackermann(n, p):
    """Funkcja Ackermanna, n i p to liczby naturalne.
    Zachodzi A(0, p) = 1, A(n, 1) = 2n, A(n, 2) = 2 ** n,
    A(n, 3) = 2 ** A(n-1, 3).
    """
    if n == 0:
        return 1
    if p == 0 and n >= 0:
        return 2 if n == 1 else n + 2
    if p >= 0 and n >= 1:
        return ackermann(ackermann(n - 1, p), p - 1)


def ack():
    a = {}
    for x in range(4):
        for y in range(1, 4):
            a[(x, y)] = ackermann(x, y)
    print a


#ack()

"ZADANIE 6"

import timeit

p = {(0, 0): 0.5}


def P_Dyn(i, j):
    global p
    if i < 0 or j < 0:
        raise ValueError
    elif i > 0 and j == 0 and (i, 0) not in p:
        p[(i, 0)] = 0.
    elif i == 0 and j > 0 and (0, j) not in p:
        p[(0, j)] = 1.
    elif (i, j) not in p:
        p[(i, j)] = 0.5 * (P_Dyn(i - 1, j) + P_Dyn(i, j - 1))
    return p[(i, j)]


def P_Rec(i, j):
    if i < 0 or j < 0:
        raise ValueError
    if i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (P_Rec(i - 1, j) + P_Rec(i, j - 1))

print timeit.Timer("P_Dyn(13,11)", "from __main__ import P_Dyn").timeit(1)
print timeit.Timer("P_Rec(13,11)", "from __main__ import P_Rec").timeit(1)
