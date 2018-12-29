for t in range(int(input())):
    n = int(input())
    A = [[0 for i in range(n)] for j in range(n)]
    count = 1
    for i in range(n):
        for j in range(i+1):
            A[j][i-j] = count
            count += 1
    for i in range(1,n):
        for j in range(i, n):
            A[j][n+i-j-1] = count
            count += 1
    for i in range(n):
        print(*A[i])
