for t in range(int(input())):
    n = int(input())
    if n <= 3:
        print(1)
        print(n, *list(range(1, n+1)))
    else:
        print(n//2)
        print(3, 1, 2, 3)
        for i in range(4, n+1, 2):
            print(2, i, i+1) if i+1 <= n else print(1, i)