n, q = input().split()
n, q = int(n), int(q)
a = [int(e) for e in input().split()]
mn = min(a)
mx = max(a)+1
for i in range(q):
    if int(input()) in range(mn, mx):
        print("Yes")
    else:
        print("No")
