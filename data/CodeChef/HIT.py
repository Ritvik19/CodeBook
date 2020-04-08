for t in range(int(input())):
    n = int(input())
    a = n//4
    b = a + a
    c = a + a + a
    A = list(map(int, input().split())) 
    A.sort()
    if A[a] == A[a-1] or A[b] == A[b-1] or A[c] == A[c-1]:
        print(-1)
    else:
        print(A[a], A[b], A[c])