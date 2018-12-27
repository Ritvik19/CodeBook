for t in range(int(input())):
    n = 2*int(input())
    A = list(map(int, input().split()))
    A = list(sorted(A))
    Alow = A[:n//2]
    Ahigh = A[n//2:]
    #print(Alow, Ahigh)
    median = Ahigh[n//4]
    B = []
    for i in range(n//2):
        B.append(Alow[i])
        B.append(Ahigh[i])
    print(median)
    print(*B)
