n = int(input())
R = set(int(e) for e in input().split())
killers = set(range(1, n+1))
print(*sorted(killers-R))
