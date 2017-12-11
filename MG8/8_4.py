import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trojkata za pomoca wzoru
    Herona. Dlugosci bokow trojkata wynosza a, b, c."""

    if a + b > c and a + c > b and b + c > a:
        p = math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4
        print "Pole trojkata wynosi: " + repr(p)
    else:
        raise ValueError("Boki nie spelniaja nierownosci trojkata!")

a = input("Podaj dlugosc boku a: ")
b = input("Podaj dlugosc boku b: ")
c = input("Podaj dlugosc boku c: ")

heron(a, b, c)
