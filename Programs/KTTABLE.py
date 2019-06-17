for i in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split(" ")]
    B = [int(e) for e in input().split(" ")]
    C = [A[0]]
    for i in range(1,len(A)):
        C.append(A[i]-A[i-1])
    op = 0
    for b, c in zip(B,C):
        if b <= c:
            op += 1
    print(op)
