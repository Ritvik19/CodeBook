for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(n):
        count = 0
        for j in range(i+1, n):
            if A[j] > A[i]:
                count += 1
        B.append(count)
    print(*B)