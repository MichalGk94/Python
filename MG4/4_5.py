def odwracanie(l, left, right):
    right += len(l) if right < 0 else 1
    l[left:right] = l[left:right][::-1]


def odwracanie_iter(l, left, right):
    if right >= len(l):
        right = len(l) - 1
    if left < 0:
        left = 0
    for x in range(left, right + 1):
        l.insert(x, l.pop(right))


def odwracanie_rec(l, left, right):
    if right >= len(l):
        right = len(l) - 1
    if left < 0:
        left = 0
    if left is not right:
        l.insert(left, l.pop(right))
        odwracanie_rec(l, left + 1, right)


L = [1, 2, 3, 4, 5, 6, 7, 8]
print L
odwracanie(L, 0, 7)
print L
