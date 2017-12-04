from triangles import Triangle

trg1 = Triangle(-2, 1, 0, 5, 3, -2)
trg2 = Triangle(-3, 0, 1, -4, 2, 1)

trg1.__str__()
trg2.__repr__()

print trg1._eq_(trg2)
print trg2._ne_(trg1)

