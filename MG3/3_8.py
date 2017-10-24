t = 'a', 'c', 5, 1, 'z', 6, 8, 2
u = 'z', 'a', 4, 0, 'b', 'a', 8

L = []

for i in range(len(t)):
    for j in range(len(u)):
        if t[i] == u[j]:
            L.append(t[i])

for i in range(len(L)-1):
    c = L[i]
    for j in range(L.count(c) -1):
        L.remove(c)

print L
