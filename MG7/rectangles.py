from points import Point

class Rectangle:
    #"""Klasa reprezentujaca prostokat na plaszczyznie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        print "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"         # "[(x1, y1), (x2, y2)]"

    def __repr__(self):
        print "Rectangle(" + repr(self.pt1.x) + ", " + repr(self.pt1.y) + ", " + repr(self.pt2.x) + ", " + repr(self.pt2.y) + ")"          # "Rectangle(x1, y1, x2, y2)"

    def eq(self, other):
        return self == other   # obsluga rect1 == rect2

    def ne(self, other):        # obsluga rect1 != rect2
        return not self == other

    def center(self):
        x = (self.pt1.x + self.pt2.x)/2
        y = (self.pt1.y + self.pt2.y)/2
        pt = Point(x, y)
        return pt       # zwraca srodek prostokata

    def area(self):
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y) # pole powierzchni

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y      # przesuniecie o (x, y)


    def intersection(self, other): pass # czesc wspolna prostokatow

    def cover(self, other): 
        minX = min(self.pt1.x, other.pt1.x)
        minY = min(self.pt1.y, other.pt1.y)
        maxX = max(self.pt2.x, other.pt2.x)
        maxY = max(self.pt2.y, other.pt2.y)
        return Rectangle(minX, minY, maxX, maxY)     # prostokat nakrywajacy oba

    def make4(self):
        R = []
        ptc = self.center()
        R[0] = Rectangle(ptc.x, ptc.y, self.pt2.x, self.pt2.y)
        R[1] = Rectangle(self.pt1.x, ptc.y, ptc.x, self.pt2.y)
        R[2] = Rectangle(self.pt1.x, self.pt1.y, ptc.x, ptc.y)
        R[3] = Rectangle(ptc.x, self.pt1.y, self.pt2.x, ptc.y)
        return R  # zwraca liste czterech mniejszych
