for t in range(int(input())):
    n = int(input())
    perm = list(range(n))
    gperm = []
    if n%2 == 0:
        for i in range(n):
            if perm[0] != i:
                gperm.append(perm[0]+1)
                perm.remove(perm[0])
            else:
                gperm.append(perm[1]+1)
                perm.remove(perm[1])
    else:
        for i in range(n-1):
            if perm[0] != i:
                gperm.append(perm[0]+1)
                perm.remove(perm[0])
            else:
                gperm.append(perm[1]+1)
                perm.remove(perm[1])
        gperm.insert(n-2,n)
    print(*gperm)
