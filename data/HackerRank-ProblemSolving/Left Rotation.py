a = (input().split())
n = a[0]
d = a[1]
d = int(d)

a = [x for x in input().split()]
l1 = a[:d]
l2 = a[d:]
l3 = l2+l1
print(*l3)
