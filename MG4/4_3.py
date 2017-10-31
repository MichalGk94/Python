def factorial(n):
    wynik = 1
    if n == 0 or n == 1:
        print wynik
    else:
        for i in range(1, n+1):
            wynik *= i
        print wynik

x = input("Podaj liczbe, dla ktorej chcesz obliczyc silnie: ")
factorial(x)            
        
