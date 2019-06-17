for t in range(int(input())):
    for g in range(int(input())):
        i, n, q = map(int, input().split())
        if n %2 == 0:
            print(n//2)
        else:
            if i == q:
                print(n//2)
            else:
                print(n//2+1)
