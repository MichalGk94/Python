s = [[],[4],(1,2),[3,4],(5,6,7)]
L = []
l = 0

for i in range(len(s)):
    for j in range(len(s[i])):
        l += s[i][j]
    L.append(l)
    l = 0

print L
