for t in range(int(input())):
    n, m = map(int, input().split())
    dishes = [0]*(m+1)
    for i in range(n):
        d, v = map(int, input().split())
        dishes[d] = max(dishes[d], v)
    dishes.sort()
    print(dishes[-2]+dishes[-1])
