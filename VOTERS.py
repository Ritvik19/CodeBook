n1, n2, n3 = map(int, input().split())
l1 = []
l2 = []
l3 = []
for i in range(n1):
    l1.append(int(input()))
for i in range(n2):
    l2.append(int(input()))
for i in range(n3):
    l3.append(int(input()))
a = set(l1)&set(l2)
b = set(l2)&set(l3)
c = set(l3)&set(l1)
z = set(a|b|c)
z = sorted(list(z))
print(len(z))
for i in z:
    print(i)
