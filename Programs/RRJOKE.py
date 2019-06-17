for i in range(int(input())):
    n = int(input())
    p = []
    for j in range(n):
        p.append(input().split())
    op = n
    for j in range(1,n):
        op ^=j
    print(op)
