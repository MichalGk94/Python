def solve1(a, b, c):
    """Rozwiazywanie rownania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0:
        raise ValueError("A i B nie moga byc jednoczesnie rowne 0")
   
    if a == 0 and b != 0:
        print "Rozwiazaniem jest prosta rownolegla do osi OX y = " + repr(-c/b) + "."

    if a != 0 and b == 0:
        print "Rozwiazaniem jest prosta rownolegla do osi OY x = " + repr(-c/a) + "."

    if c == 0:
        print "Prosta przechodzi przez poczatek ukladu wspolrzednych."

    if a != 0 and b != 0:
        print "Rozwiazaniem jest prosta y = " + repr(-a/b) + "x + " + repr(-c/b) + "."


a = input("Podaj wspolczynnik A: ")
b = input("Podaj wspolczynnik B: ")
c = input("Podaj wspolczynnik C: ")

solve1(a, b, c)
