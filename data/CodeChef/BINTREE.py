from math import log2, floor
for t in range(int(input())):
    i, j = map(int, input().split())
    hi, hj = floor(log2(i)), floor(log2(j))
    t1 , t2 = i, j
    #until they dont meet at a point
    while t1 != t2:
        if t1 > t2:
            t1 //= 2
        else:
            t2 //= 2
    h0 = floor(log2(t1)) #height of the same parent
    print(hi-h0+hj-h0)
