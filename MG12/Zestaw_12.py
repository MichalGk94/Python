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
print list


def mediana_sort(L, left, right):
    L.sort()
    return L[(right - left) / 2] if (right - left) % 2 == 1 else (
                                                                     L[(right - left) / 2] + L[
                                                                         (right - left) / 2 + 1]) / 2.

print "Mediana sort: " + str(mediana_sort(list, 2, len(list)-2))
print "Mediana sort: " + str(mediana_sort(list, 0, len(list)-1))


def moda_sort(L, left, right):
    if left + 1 > right:
        return None
    L.sort()
    mod = None
    modcount = 0
    value = left
    valuecount = 1
    while value < right:
        value += 1
        if L[value] == L[value - 1]:
            valuecount += 1
            if valuecount > modcount:
                modcount = valuecount
                mod = value
        else:
            valuecount = 1
    return L[mod]


print "Moda sort: " + str(moda_sort(list, 1, len(list)-1))


def moda_py(L, left, right):
    count = dict.fromkeys(L, 0)
    while left < right:
        count[L[left]] += 1
        left += 1
    return max(count, key = count.get)


print "Moda py: " + str(array[moda_py(array, 5, len(array)-1)])
print "Moda py: " + str(array[moda_py(array, 2, len(array)-3)])


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
print "Lider py: " + str(lider_py(li, 3, len(li)-3))
print "Lider py: " + str(lider_py(li, 1, len(li)-2))
