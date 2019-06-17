for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = [0]
    count = 0
    for i in range(n):
        pos = B.index(A[i])
        count += min(pos, len(B)-pos-1)
        B.insert(pos+1, i+1)
    print(count)
