from rectangles import Rectangle

rect1 = Rectangle(-2, 1, 4, -3)
rect2 = Rectangle(4, -2, 0, 2)

rect1.__str__()
rect2.__repr__()

print rect1.eq(rect2)
print rect2.ne(rect1)

print str(rect1.center())

print rect2.area()

rect1.move(2, -2)
rect1.__str__()

