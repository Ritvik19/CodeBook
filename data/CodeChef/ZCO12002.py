def just_smaller(a, e):
    pos = -1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (high+low)//2
        if a[mid] <= e:
            pos = a[mid]
            low = mid + 1
        else:
            high = mid - 1
    return pos

def just_greater(a, e):
    pos = -1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (high+low)//2
        if a[mid] >= e:
            pos = a[mid]
            high = mid - 1
        else:
            low = mid + 1
    return pos 

n, x, y = map(int, input().split())
events = []
for _ in range(n):
    events.append(tuple(map(int, input().split())))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
v.sort()
w.sort()
ans = 1000005
for i in range(n):
    t1 = just_smaller(v, events[i][0])
    t2 = just_greater(w, events[i][1])
    if not ( t1 == -1 or t2 == -1 ):
        ans = min(ans,(t2-t1)+1)
print(ans)