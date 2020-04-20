def nSmall():
    l = []
    for i in range(n):
        end = min(n,10001//(i+1))
        for j in range(end):
            l.append(a[i]+b[j])
    return l

for t in range(int(input())):
    n, q = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    arr = sorted(nSmall())
    for _ in range(q):
        print(arr[int(input())-1])