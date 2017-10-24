x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
#kod poprawny skladniowo

#for i in "qwerty": if ord(i) < 100: print i
#kod niepoprawny skladniowo, powinno byc:
for i in "qwerty":
    if ord(i) < 100: print i

for i in "axby": print ord(i) if ord(i) < 100 else i
#kod poprawny skladniowo.
#Instrukcja print jako instrukcja prosta może znajdować się bezpośrednio po
#instrukcji for, instrukcja if jako złożona musi być w nowej linii z wcięciem.

