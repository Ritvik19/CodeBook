n = int(input())
C = list(map(int, input().split()))
T = list(map(int, input().split()))

min1 = min2 = min3 = float('inf')

for c, t in zip(C, T):
    if t == 1:
        min1 = min(min1, c)
    elif t == 2:
        min2 = min(min2, c)
    else:
        min3 = min(min3, c)

print(min(min1 + min2, min3))        