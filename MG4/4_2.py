def ruler(x):

    miara = '|'
    liczba = '0'
    for i in range(1, x+1):
        miara = miara + '....|'
        if i < 10:
            liczba = liczba + '    ' + str(i)
        else:
            liczba = liczba + '   ' + str(i)
    linijka = miara + '\n' + liczba
    return linijka

def table(x,y):
    
    x1 = '+'
    x2 = '|'

    for i in range(x):      #konstrukcja kolumn
        x1 = x1 + '---+'
        x2 = x2 + '   |'

    tabela = x1
    for i in range(y):      #konstrukcja wierszy
        tabela = tabela + '\n' + x2 + '\n' + x1

    return tabela

x = input("Podaj dlugosc linijki: ")
linijka = ruler(x)
print linijka

y = input('Ile kolumn tabeli: ')
z = input('Ile wierszy tabeli: ')
tabela = table(y,z)
print tabela
