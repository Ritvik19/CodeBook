def is_perm(A, n):
    for i in range(n-1):
        if A[i+1] - A[i] > 1:
            return False
    return True

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A = list(sorted(A))
    if(is_perm(A, n)):
        print("YES")
    else:
        print("NO")
