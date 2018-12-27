for t in range(int(input())):
    n = int(input())
    na = nb = 100   #max m
    for i in range(n):
        q = input()
        na = min(na, q.count('a'))
        nb = min(nb, q.count('b'))
    print(min(na, nb))
