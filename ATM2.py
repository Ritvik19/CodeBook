for t in range(int(input())):
    out = ""
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    for a in A:
        if a <= k:
            out += '1'
            k -= a
        else:
            out += '0'
    print(out)
