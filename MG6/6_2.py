from points import Point

point1 = Point(3, 7)
point2 = Point(-2, 1)
point1.__str__()
point2.__repr__()
print point1.eq(point2)
print point1.ne(point2)
print point1.add(point2)
print point1.sub(point2)
print point1.mul(point2)
print point2.mul(point1)
print point1.cross(point2)
print point2.cross(point1)
print point1.length()
print point2.length()