for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().strip().split()))
    zer, one = A.count(0), A.count(1)
    two, thr = A.count(2), A.count(3)
    x = n-zer-one
    count = x*(x-1)//2
    count -= (two)(two-1)//2 + two*thr
    print(count)
