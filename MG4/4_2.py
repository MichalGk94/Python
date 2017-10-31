def ruler():

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
    return linijka

def table():
    x = input('Ile kolumn: ')
    y = input('Ile wierszy: ')
    
    x1 = '+'
    x2 = '|'

    for i in range(x):      #konstrukcja kolumn
        x1 = x1 + '---+'
        x2 = x2 + '   |'

    tabela = x1
    for i in range(y):      #konstrukcja wierszy
        tabela = tabela + '\n' + x2 + '\n' + x1

    return tabela



linijka = ruler()
print linijka
tabela = table()
print tabela
