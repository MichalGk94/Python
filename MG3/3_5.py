miara = '|'
liczba = '0'
x = input("Podaj dlugosc: ")
for i in range(1, x+1):
    miara = miara + '....|'
    if i < 10:
        liczba = liczba + '    ' + str(i)
    else:
        liczba = liczba + '   ' + str(i)
linijka = miara + '\n' + liczba
print linijka
