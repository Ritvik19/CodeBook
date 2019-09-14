n, m = map(int, input().split())
Ar = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for a in Ar:
    if a in A:
        happiness += 1
    if a in B:
        happiness -= 1
print(happiness)
