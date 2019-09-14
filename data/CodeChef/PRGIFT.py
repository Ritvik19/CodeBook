for t in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for a in A:
        if a %2 == 0:
            count += 1
    if k = 0:
        print("NO")
    elif count >= k:
        print("YES")
    else:
        print("NO")
