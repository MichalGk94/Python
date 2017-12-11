import random

def calc_pi(n):
    """Obliczanie liczby pi metoda Monte Carlo.
    n oznacza liczbe losowanych punktow."""

    pkt = n
    pktK = 0
    for i in range(n):
        x = random.random() * 2 -1
        y = random.random() * 2 -1
        if x*x + y*y <= 1:
            pktK +=1

    print "Liczba punktow: " + repr(pkt)
    print "Liczba punktow w kole: " + repr(pktK)
    pi = 4 * pktK/pkt
    print "Liczba pi wynosi: " + repr(pi)
    print " "


calc_pi(10)
calc_pi(100)
calc_pi(1000)
