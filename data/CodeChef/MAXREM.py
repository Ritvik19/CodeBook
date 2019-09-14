n = int(input())
A = set(map(int, input().split()))
if len(A)==1:
    print(0)
else:
    A.remove(max(A))
    print(max(A))
