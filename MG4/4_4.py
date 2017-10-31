def fibonacci(n):
    wynik = 0
    liczba = 0
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        f1 = 1
        f2 = 2
        wynik = 0;
        for i in range(2, n-1):
            wynik = f1 + f2
            f1 = f2
            f2 = wynik
        return wynik

x = input("Ktory wyraz chcesz otrzymac? ")
print fibonacci(x)
