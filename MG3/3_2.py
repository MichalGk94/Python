#L = [3, 5, 4] ; L = L.sort()
#operacja L = L.sort() jest bledem, wystarczy L.sort()
L = [3, 5, 4] ; L.sort()
print L

#x, y = 1, 2, 3
#dwie zmienne, 3 wartosci
x, y = 1, 2
print x
print y

#X = 1, 2, 3 ; X[1] = 4
#X nie jest lista tylko tzw. "tuple", wiec nie moze byc zmieniony.

#X = [1, 2, 3] ; X[3] = 4
#Listy numerujemy od 0, wiec ostatni index X to 2 

#X = "abc" ; X.append("d")
#X jest stringiem. Stringi nie maja funkcji append

#map(pow, range(8))
#pow potrzebuje dwoch argumentow
map(pow, range(8), range(8))
