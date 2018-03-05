#!/usr/bin/python
# -*- coding: utf-8 -*-


from random import randrange

"""Zadanie 1"""

def linear_search(L, left, right, y):
    print y
    i = left
    while i < right:
        if y == L[i]:
            return i
        i += 1
    return None


array = [randrange(0, 10) for x in range(100)]
"""print linear_search(array, 0, 100, 0)
print linear_search(array, 0, 100, 1)
print linear_search(array, 0, 100, 2)
print linear_search(array, 0, 100, 3)
print linear_search(array, 0, 100, 4)
print linear_search(array, 0, 100, 5)
print linear_search(array, 0, 100, 6)
print linear_search(array, 0, 100, 7)
print linear_search(array, 0, 100, 8)
print linear_search(array, 0, 100, 9)"""


def binarne_rek(L, left, right, y):
    if left > right:
        return None
    k = (left + right) / 2
    if y == L[k]:
        return k
    elif y > L[k]:
        return binarne_rek(L, k + 1, right, y)
    else:
        return binarne_rek(L, left, k - 1, y)


array.sort()
"""print array
print binarne_rek(array, 0, len(array), 1)"""

list = [6, 3, 7, 8, 5, 2, 1, 4, 9, 7]
list2 = [6, 3, 7, 7, 5, 2, 7, 1, 7, 4, 9, 7]
#print list


def mediana_sort(L, left, right):
    M = L[left:right]
    M.sort()
    S = L[0:left-1] + M
    S += L[right-1:len(L)]

    print "Lista przed sortowaniem: " + str(L)
    print "Lista po sortowaniu: " + str(S)

    return S[(right - left) / 2]

print "Mediana: " + str(mediana_sort(list, 2, len(list)-2))

#print "Mediana sort: " + str(mediana_sort(list, 2, len(list)-2))
#print "Mediana sort: " + str(mediana_sort(list, 0, len(list)-1))


def moda(L, left, right):
    """Wyszukiwanie mody w ciągu."""
    if left+1 > right:
        return None

    M = L[left:right]
    M.sort()
    i1 = None             # najlepszy kandydat (indeks)
    number1 = 0           # jego liczebność
    i2 = 0             # bieżący element (indeks)
    number2 = 1           # jego liczebność
    while i2 < len(M)-1:
        i2 += 1
        if M[i2] == M[i2-1]:    # jeżeli się powtórzył
            number2 += 1
            # na bieżąco uaktualniamy najlepszego kandydata
            if number2 > number1:  # jest lepszy kandydat
                number1 = number2
                i1 = i2
        else:                   # nowy bieżący element
            number2 = 1
    print "Lista przed posortowaniem: " + str(L)
    L[left:right] = M[0:(len(M))]
    print "Lista po posortowaniu: " + str(L)
    return i1


print "Moda sort: " + str(moda(list2, 2, len(list2)-2))


def moda_py(L, left, right):
    count = dict.fromkeys(L, 0)
    while left < right:
        count[L[left]] += 1
        left += 1
    return max(count, key = count.get)


#print "Moda py: " + str(array[moda_py(array, 5, len(array)-1)])
#print "Moda py: " + str(array[moda_py(array, 2, len(array)-3)])


def lider_py(L, left, right):
    count = dict.fromkeys(L, 0)
    while left < right:
        count[L[left]] += 1
        left += 1

    for x, y in count.viewitems():
        if y > len(L) / 2:
            return x
    return None


li = [1, 5, 5, 5, 5, 5, 5, 7, 8]
#print "Lider py: " + str(lider_py(li, 3, len(li)-3))
#print "Lider py: " + str(lider_py(li, 1, len(li)-2))
