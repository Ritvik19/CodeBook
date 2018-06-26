def amb(per, n):
    for i in range(n):
        if per[per[i]-1] != (i+1):
            return "not ambiguous"
    return "ambiguous"
n = int(input())
while n != 0:
    perm = [int(e) for e in input().split()]
    print(amb(perm, n))
    n = int(input())
