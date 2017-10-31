def odwracanie(L, left, right):
    temp = 0;
    while(left < right):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1
    print L

L = [0,1,2,3,4,5,6,7,8]
odwracanie(L, 2, 6)
