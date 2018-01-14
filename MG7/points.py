#!/usr/bin/python
# -*- coding: utf-8 -*-

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x = 0, y = 0):  # konstuktor
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
