import heapq as heap

for t in range(int(input())):
    n, a, b, x, y, z = map(int,input().split( ))
    h = list(map(int,input().split( )))
    for i in range(n):
        h[i] *= -1
    heap.heapify(h)
    extra = (z - b - 1) // y
    a += x * extra
    b += y * extra
    ans = 0
    while a < z and h:
        maximum = -1 * heap.heappop(h)
        a += maximum
        ans += 1
        maximum //= 2
        if maximum:
            heap.heappush(h,-1 * maximum)
    if a < z:
        print("RIP")
    else:
        print(ans)