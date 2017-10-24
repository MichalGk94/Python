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

print tabela
