for t in range(int(input())):
    n = int(input())
    row = list(range(1, n+1))[n//2+1:] + list(range(1, n+1))[:n//2+1]
    for i in range(n):
        print(*row[i:]+row[:i])
