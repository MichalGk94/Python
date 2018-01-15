#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


def genRand(N, length):
    return random.sample(xrange(N), length)


def genRandSort(N, length):
    array = genRand(N, length)
    array.sort()
    array[0], array[length / 2 - 1], array[length / 2 + 1], array[length - 1] = \
        array[length - 1], array[length / 2 + 1], array[length / 2 - 1], array[0]
    return array


def genRandSortRev(N, length):
    array = genRand(N, length)
    array.sort(reverse = True)
    array[0], array[length / 2 - 1], array[length / 2 + 1], array[length - 1] = \
        array[length - 1], array[length / 2 + 1], array[length / 2 - 1], array[0]
    return array


def genGauss(N):
    return [random.gauss(0, 1) for x in range(N)]


def genDupl(N, k):
    return [random.randint(0, k) for x in range(N)]

