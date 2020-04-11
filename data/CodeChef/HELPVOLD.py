n = int(input())
room = [int(e) for e in input().split()]
room = sorted(room)
power = 0
for i in range(n-1):
    power += room[i]*room[i+1]
print(power)
