days = [ "mon", "tues", "wed", "thurs", "fri", "sat", "sun"]

t = int(input())
for i in range(t):
    n, d = input().split()
    nw = [4, 4, 4, 4, 4, 4, 4]
    for i in range(int(n)-28):
        nw[(days.index(d)+i)%7] += 1
    print(*nw)
