#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


def genRand(N, length):
    return random.sample(xrange(N), length)

#zmienna degree to stopie pomieszania - im mniejsza, tym bardziej przemieszana lista
def genRandSort(N, length, degree):
    array = genRand(N, length)
    array.sort()
    count = length/degree
    for i in range(0, count):
	rand1 = random.randint(0, length-1)
	rand2 = random.randint(0, length-1)
	temp = array[rand1]
	array[rand1] = array[rand2]
	array[rand2] = temp
    return array


def genRandSortRev(N, length, degree):
    array = genRand(N, length)
    array.sort(reverse = True)
    count = length/degree
    for i in range(0, count):
	rand1 = random.randint(0, length-1)
	rand2 = random.randint(0, length-1)
	temp = array[rand1]
	array[rand1] = array[rand2]
	array[rand2] = temp
    return array


def genGauss(N):
    return [random.gauss(0, 1) for x in range(N)]


def genDupl(N, k):
    return [random.randint(0, k) for x in range(N)]

