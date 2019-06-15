for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] %2 == 0 and a[j]%2 == 1:
                c += 1
    print(c)
