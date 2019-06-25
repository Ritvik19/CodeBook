for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = []
    last = 0
    for a in A[::-1]:
        if a %2 == 0:
            B.append(last)
        else:
            last += 1
            B.append(0)
    print(sum(B))
