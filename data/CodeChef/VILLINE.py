n = int(input())
powers = [0, 0]
m, c = map(int, input().split())
for _ in range(n):
    x, y, p = map(int, input().split())
    if y - (m*x) - c > 0:
        powers[0] += p
    else:
        powers[1] += p
print(max(powers))        