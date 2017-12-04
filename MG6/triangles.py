from points import Point

class Triangle:
    #"""Klasa reprezentujaca trojkat na plaszczyznie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        print "[(" +  str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + "), (" + str(self.pt3.x) + ", " + str(self.pt3.y) + ")]"         # "[(x1, y1), (x2, y2), (x3, y3)]"

    def __repr__(self):
        print "Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ", " + str(self.pt3.x) + ", " + str(self.pt3.y) + ")"        # "Triangle(x1, y1, x2, y2, x3, y3)"

    def _eq_(self, other):
        return self == other   # obsluga tr1 == tr2

    def _ne_(self, other):        # obsluga tr1 != tr2
        return not self == other

    def center(self): pass          # zwraca srodek trojkata

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesuniecie o (x, y)
