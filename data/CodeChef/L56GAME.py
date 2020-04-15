for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if l[i]%2 == 1:
            c += 1
    if (n == 1 and l[i] %2 == 1) or c %2 == 0:
        print(1)
    else:
        print(2)
    
            