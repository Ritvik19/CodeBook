for i in range(int(input())):
    n = int(input())
    a = [int(e) for e in input().split(" ")]
    bor = a[0]
    for j in range(1,n):
        bor = bor|a[j]
    print(bor)
