a = [500]*100001

for n in range(int(input())):
    x, y = map(int, input().split())
    a[x+1] = min(a[x+1],y)

s = []
tmp = 0
i = 1
ans = 0
while i <= 100000:
    if len(s) == 0 or a[s[-1]] <= a[i]:
        s.append(i)
        i += 1
    else:
        tp = s.pop(-1)
        tmp = a[tp] * (i-1 if len(s) == 0 else i - s[-1])
        if tmp > ans:
            ans = tmp
while len(s) > 0:
    tp = s.pop(-1)
    tmp = a[tp] * (i-1 if len(s) == 0 else i - s[-1])
    if tmp > ans:
        ans = tmp
print(ans)        