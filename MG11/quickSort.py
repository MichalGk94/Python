#!/usr/bin/python
# -*- coding: utf-8 -*-

import genSort
import timeit


def quicksort(L, left, right, cmpfunc = cmp):
    if left >= right:
        return
    swap(L, left, (left + right) / 2)
    pivot = left
    for i in range(left + 1, right + 1):
        if cmpfunc(L[left], L[i]) > 0:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)  # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)


def swap(L, left, right):
    L[left], L[right] = L[right], L[left]


k = genSort.genRand(100, 20)
j = list(k)
quicksort(k, 0, 19)
quicksort(j, 0, 19, lambda a, b: 1 if a <= b else 0)
print k, '\n', j

print timeit.Timer("quicksort(l,0,199)",
                   "import genSort; from __main__ import quicksort; l = genSort.genRand(1000, 200)").timeit(100)
print timeit.Timer("quicksort(l,0,199)", "import genSort; from __main__ import quicksort; l = "
                                         "genSort.genRandSort(1000, 200)").timeit(100)
print timeit.Timer("quicksort(l,0,199)", "import genSort; from __main__ import quicksort; l = "
                                         "genSort.genRandSortRev(1000, 200)").timeit(100)
print timeit.Timer("quicksort(l,0,199)",
                   "import genSort; from __main__ import quicksort; l = genSort.genGauss(200)").timeit(100)
print timeit.Timer("quicksort(l,0,199)",
                   "import genSort; from __main__ import quicksort; l = genSort.genDupl(200, 50)").timeit(100)
