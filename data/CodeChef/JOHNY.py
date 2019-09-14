for t in range(int(input())):
    n = int(input())
    a = [int(e) for e in input().split()]
    k = int(input())
    j = a[k-1]
    print(sorted(a).index(j)+1)
