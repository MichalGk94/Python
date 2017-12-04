import math

class Point:
    #"""Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): 
        print "(" + str(self.x) + ", " + str(self.y) + ")" # zwraca string "(x, y)"

    def __repr__(self): 
        print "Point(" + repr(self.x) + ", " + repr(self.y) + ")" #zwraca string "Point(x, y)"

    def eq(self, other):
        if self == other:
            return True
        else:
            return False # obsluga point1 == point2

    def ne(self, other):        # obsluga point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def add(self, other):
        return (self.x + other.x, self.y + other.y) # v1 + v2

    def sub(self, other):
        return (self.x - other.x, self.y - other.y) # v1 - v2

    def mul(self, other):
        return self.x * other.x + self.y * other.y # v1 * v2, iloczyn skalarny

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y) # dlugosc wektora

