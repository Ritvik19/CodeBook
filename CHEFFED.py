def s(k):
    sod = 0
    while k:
        sod += k%10
        k//=10
    return sod

n = int(input())
count = 0
for i in range(max(0,n-97), n):
    if i + s(i) +s(s(i)) == n:
        count += 1
print(count)
