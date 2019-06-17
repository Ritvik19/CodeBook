n, k = map(int, input().split())
A = list(map(int, input().split()))
if k == 0:
    pass
elif k %2 == 0:
    for i in range(2):
        x = max(A)
        A = [x-a for a in A]
else:
    x = max(A)
    A = [x-a for a in A]
print(*A)
