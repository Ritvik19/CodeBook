for t in range(int(input())):
    n = int(input())
    delayed = 0
    for i in range(n):
        s, j = map(int, input().split())
        if j-s > 5:
            delayed += 1
    print(delayed)
