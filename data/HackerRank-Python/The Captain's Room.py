k = int(input())
rooms = list(map(int, input().split()))
seen = {}

for i in rooms:
    if not i in seen:
        seen[i] = 1
    else:
        seen[i] += 1

for key, val in seen.items():
    if val != k:
        print(key)
